#!/usr/bin/env python3
"""Convert the v93.1 manuscript Markdown to Overleaf-compatible XeLaTeX."""
import re, html

SRC = '/home/hatch/workspace/irh_v931/paper_v931.md'
DST = '/home/hatch/workspace/irh_v931/IRH_v93_1.tex'

src = open(SRC, encoding='utf-8').read()
lines = src.split('\n')

# ---------- helpers ----------
def esc_text(s):
    """Escape LaTeX specials in a text-mode fragment (no math, no commands)."""
    s = s.replace('\\', r'\textbackslash{}')
    for a, b in [('{', r'\{'), ('}', r'\}'), ('$', r'\$'), ('&', r'\&'),
                 ('%', r'\%'), ('#', r'\#'), ('_', r'\_'),
                 ('~', r'\textasciitilde{}'), ('^', r'\textasciicircum{}')]:
        s = s.replace(a, b)
    return s

def protect_math(line):
    """Split line into (is_math, fragment) pieces on $...$ and $$...$$."""
    parts = []
    # handle $$ first
    tokens = re.split(r'(\$\$.+?\$\$|\$[^$]+?\$)', line, flags=re.S)
    for tok in tokens:
        if not tok:
            continue
        if tok.startswith('$$') and tok.endswith('$$'):
            parts.append((True, tok, 'display'))
        elif tok.startswith('$') and tok.endswith('$'):
            parts.append((True, tok, 'inline'))
        else:
            parts.append((False, tok, None))
    return parts

URLPAT = r'https?://(?:[^()\s]|\([^)]*\))+'
TOKEN_RE = re.compile(r'(\[.+?\]\(%s\))|(<a href="#ref-\d+">\[\d+\]</a>)|(`[^`]+?`)|(\*\*.+?\*\*)|((?<!\*)\*(?!\*).+?(?<!\*)\*(?!\*))' % URLPAT)

def conv_inline_frag(s):
    """Run TOKEN_RE over s; used recursively for nested formatting."""
    out = []
    pos = 0
    for m in TOKEN_RE.finditer(s):
        out.append(esc_text(s[pos:m.start()]))
        tok = m.group(0)
        if tok.startswith('['):
            mm = re.match(r'\[(.+?)\]\((%s)\)' % URLPAT, tok)
            out.append(r'\href{%s}{%s}' % (mm.group(2), esc_text(mm.group(1))))
        elif tok.startswith('<a'):
            mm = re.match(r'<a href="#ref-(\d+)">\[(\d+)\]</a>', tok)
            out.append(r'\hyperref[ref%s]{[%s]}' % (mm.group(1), mm.group(2)))
        elif tok.startswith('`'):
            out.append(r'\texttt{%s}' % esc_text(tok[1:-1]))
        elif tok.startswith('**'):
            out.append(r'\textbf{%s}' % conv_inline_frag(tok[2:-2]))
        else:
            out.append(r'\textit{%s}' % conv_inline_frag(tok[1:-1]))
        pos = m.end()
    out.append(esc_text(s[pos:]))
    return ''.join(out)

def conv_text_fragment(s):
    return conv_inline_frag(s)

# Unicode math symbols that Noto Sans text lacks -> render via math mode.
# Applied to the raw line BEFORE math-span extraction, so they become math.
UNIMATH_SUBS = [
    ('\u2192', r'$\to$'),
    ('\u2208', r'$\in$'),
    ('\u2212', r'$-$'),
    ('\u223c', r'$\sim$'),
    ('\u2248', r'$\approx$'),
    ('\u2273', r'$\gtrsim$'),
    ('\U0001D52C', r'$\mathfrak{o}$'),
    ('\U0001D530', r'$\mathfrak{s}$'),
]
SQRT_RE = re.compile('\u221a(\\w)')

def apply_unimath(line):
    for uni, latex in UNIMATH_SUBS:
        line = line.replace(uni, latex)
    line = SQRT_RE.sub(r'$\\sqrt{\1}$', line)
    line = line.replace('\u221a', r'$\surd$')
    return line

MATHPH = 'ZZMATHPLACEHOLDER'

def conv_line_math(line):
    """Convert a line: unimath subs, hide math spans as placeholders, format text, restore."""
    line = apply_unimath(line)
    maths = []
    def hide(m):
        maths.append(m.group(0))
        return '%s%dZZ' % (MATHPH, len(maths) - 1)
    # single combined pass, display-first: two sequential passes let the
    # display pattern match the '$$' formed by adjacent inline spans
    # ('$\\mathfrak{s}$$\\mathfrak{o}$'), swallowing text between them.
    tmp = re.sub(r'\$\$(.+?)\$\$|(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', lambda m: hide(m), line, flags=re.S)
    tmp = conv_inline_frag(tmp)
    def restore(m):
        idx = int(m.group(1))
        raw = maths[idx]
        if raw.startswith('$$'):
            return r'\[' + raw[2:-2] + r'\]'
        return raw
    tmp = re.sub(r'%s(\d+)ZZ' % MATHPH, restore, tmp)
    return tmp

# ---------- block parsing ----------
out = []
i = 0
n = len(lines)
in_table = False
table_rows = []

def split_row(r):
    """Split a table row on |, ignoring | inside $...$ math."""
    cells, cur, inmath = [], [], False
    i = 0
    body = r.strip()
    if body.startswith('|'):
        body = body[1:]
    if body.endswith('|'):
        body = body[:-1]
    while i < len(body):
        ch = body[i]
        if ch == '$':
            # toggle on unescaped $
            inmath = not inmath
            cur.append(ch)
        elif ch == '|' and not inmath:
            cells.append(''.join(cur))
            cur = []
        else:
            cur.append(ch)
        i += 1
    cells.append(''.join(cur))
    return [c.strip() for c in cells]

def flush_table():
    global in_table, table_rows
    if not table_rows:
        in_table = False
        return
    # parse header/align
    rows = []
    for r in table_rows:
        rows.append(split_row(r))
    ncol = max(len(r) for r in rows)
    # drop separator row (index 1 if it looks like ---)
    body = [rows[0]]
    for r in rows[1:]:
        if all(re.fullmatch(r':?-{2,}:?', c or '') for c in r):
            continue
        body.append(r)
    colspec = 'l' * ncol
    # long-text tables (retraction ledger, claim ledger) overflow the text
    # block with plain l columns; wrap the last column via tabularx.
    long_table = any(len(c) > 45 for r in body for c in r)
    out.append(r'\begin{center}')
    if long_table:
        out.append(r'\begin{xltabular}{\linewidth}{%sX}' % ('l' * (ncol - 1)))
    else:
        out.append(r'\begin{tabular}{%s}' % colspec)
    out.append(r'\hline')
    for j, r in enumerate(body):
        while len(r) < ncol:
            r.append('')
        cells = [conv_line_math(c) for c in r]
        out.append(' & '.join(cells) + r' \\')
        if j == 0:
            out.append(r'\hline')
    out.append(r'\hline')
    if long_table:
        out.append(r'\end{xltabular}')
    else:
        out.append(r'\end{tabular}')
    out.append(r'\end{center}')
    table_rows = []
    in_table = False

while i < n:
    ln = lines[i]
    stripped = ln.strip()
    # table row?
    if stripped.startswith('|') and stripped.endswith('|'):
        in_table = True
        table_rows.append(ln)
        i += 1
        continue
    else:
        if in_table:
            flush_table()
    # headings
    m = re.match(r'^(#{1,4})\s+(.*)$', stripped)
    if m:
        level = len(m.group(1))
        title = conv_line_math(m.group(2))
        cmd = {1: 'section', 2: 'subsection', 3: 'subsubsection', 4: 'paragraph'}[level]
        out.append(r'\%s*{%s}' % (cmd, title))
        i += 1
        continue
    # images: caption is the next paragraph (skip blanks); consume it
    m = re.match(r'!\[(.*?)\]\((.*?)\)', stripped)
    if m:
        cap, path = m.group(1), m.group(2)
        j = i + 1
        while j < n and not lines[j].strip():
            j += 1
        caplines = []
        while j < n and lines[j].strip() and not lines[j].strip().startswith('![') and not lines[j].strip().startswith('#'):
            caplines.append(lines[j].strip())
            j += 1
        fullcap = ' '.join(caplines).strip() or cap
        out.append(r'\begin{figure}[htbp]')
        out.append(r'\centering')
        out.append(r'\includegraphics[width=0.92\linewidth]{%s}' % path)
        out.append(r'\caption{%s}' % conv_line_math(fullcap))
        out.append(r'\end{figure}')
        i = j
        continue
    # bullet lists
    if stripped.startswith('- '):
        out.append(r'\begin{itemize}')
        while i < n and lines[i].strip().startswith('- '):
            out.append(r'\item ' + conv_line_math(lines[i].strip()[2:]))
            i += 1
        out.append(r'\end{itemize}')
        continue
    # numbered lists
    if re.match(r'^\d+\.\s', stripped):
        out.append(r'\begin{enumerate}')
        while i < n and re.match(r'^\d+\.\s', lines[i].strip()):
            out.append(r'\item ' + conv_line_math(re.sub(r'^\d+\.\s', '', lines[i].strip())))
            i += 1
        out.append(r'\end{enumerate}')
        continue
    # horizontal rule
    if stripped == '---':
        out.append(r'\medskip\hrule\medskip')
        i += 1
        continue
    # blank
    if not stripped:
        out.append('')
        i += 1
        continue
    # reference anchor lines
    m = re.match(r'<a id="ref-(\d+)"></a>(.*)$', stripped)
    if m:
        rest = m.group(2)
        out.append(r'\phantomsection\label{ref%s}' % m.group(1))
        out.append(r'\noindent ' + conv_line_math(rest))
        out.append('')
        i += 1
        continue
    out.append(conv_line_math(ln))
    i += 1
if in_table:
    flush_table()

body = '\n'.join(out)

preamble = r'''\documentclass[a4paper,11pt]{article}
\usepackage[a4paper,margin=2.4cm]{geometry}
\usepackage{amsmath}
\usepackage{fontspec}
\usepackage{unicode-math}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{xltabular}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{enumitem}
% Bundled fonts (fonts/) so the source compiles on Overleaf as-is.
\setmainfont{NotoSans-Regular.ttf}[Path=fonts/,BoldFont=NotoSans-Bold.ttf,ItalicFont=NotoSans-Italic.ttf,BoldItalicFont=NotoSans-BoldItalic.ttf]
\setmonofont{NotoSansMono-Regular.ttf}[Path=fonts/]
% Math: Latin Modern Math supplies the OpenType MATH table (layout);
% Noto Sans Math supplies the visible glyphs (this build's Noto Sans Math
% has no MATH table, so it is overlaid by range on the LM base).
\setmathfont{Latin Modern Math}
\setmathfont{NotoSansMath-Regular.ttf}[Path=fonts/,range={up/{latin,Latin,num},it/{latin,Latin},up/{greek,Greek},it/{greek,Greek},bfup/{latin,Latin,greek,Greek,num},bfit/{latin,Latin,greek,Greek},"2192,"2208,"2212,"223C,"2248,"2273}]
\hypersetup{colorlinks=true,linkcolor=blue!60!black,citecolor=blue!60!black,urlcolor=blue!60!black}
\setlength{\parskip}{0.6em}
\setlength{\parindent}{0pt}
\setlength{\emergencystretch}{2em}
\begin{document}
'''

title_block = r'''\title{\textbf{\Huge Intrinsic Resonance Holography:}\\[0.8em]
\Large Dynamical Selection of a D$_4$ Substrate from Interference Dynamics\\[0.5em]
\large Version 93.1}
\vspace{1.5cm}
\author{\textbf{Brandon D. McCrary}\\[0.25em]
\textit{Independent Theoretical Physics Researcher}\\[0.5em]
\href{https://orcid.org/0009-0008-2804-7165}{ORCID: 0009-0008-2804-7165}\\[0.5em]
Independent Verification Data\\[0.25em]
{\small\colorbox{pink}{\href{https://drive.google.com/file/d/1Sxkginzo_UmNrNETfunLK8_XUq4tbuXb/view?usp=drivesdk}{https://drive.google.com/file/d/1Sxkginzo\_UmNrNETfunLK8\_XUq4tbuXb/view?usp=drivesdk}}}}

\date{September 17, 2026}

\maketitle

\begin{abstract}
Intrinsic Resonance Holography proposes that the structure of physical reality rests on a self-organizing oscillatory substrate whose stable interference pattern is the D$_4$ root lattice. This document is the complete consolidated statement of the framework following five independent verification cycles, in which every load-bearing claim was either re-derived by executed computation, validated against a known limiting case, confirmed by simulation, excluded by theorem, or --- new in this version --- machine-checked in Lean~4.

The framework in this version differs from v92 in kind, not merely in detail. Its central ontological commitment has changed: D$_4$ is no longer a postulated static lattice but the nodal interference pattern of a field obeying tension--relaxation dynamics. That reformulation removes a primitive, dissolves a standing circularity objection at its root rather than patching it, and supplies the selection mechanism the static formulation never possessed.

\textbf{What is now established.} The D$_4$ pattern is selected dynamically rather than assumed, by a parameter-free criterion $S=\tau^2/q_4$ derived symbolically, validated by recovering the Alexander--McTague BCC result in three dimensions \hyperref[ref-1]{[1]}, applied in four where D$_4$ wins at $S=0.454$ with selection quantities that are exact rationals and simple radicals ($64/141$, $16/45$, $73/423$, $\tau_{D_4}/\tau_{\mathrm{BCC}}=\sqrt{2}$) rather than fitted decimals, confirmed by direct simulation from random initial conditions, and independently corroborated by a published molecular-dynamics result obtained by an unrelated method \\hyperref[ref-40]{[40]}. An independent mechanism-level reproduction finds $77.1\%$ of spectral power on D$_4$ with triads active versus $21.1\%$ with triads removed, rising to $89.5\%$ under annealing --- establishing the cubic triad term as the causal selection mechanism. The full 24-mode standing wave is a genuine dynamical attractor with relaxed free energy $F/V=-0.0077276$, reproduced independently at $-0.007728$. The resonance maximum is unique modulo lattice periodicity (32 periodic maxima on the $16^4$ grid); the transition is first order. The lattice constant $a_0=2\pi/q_0$ is derived rather than postulated. Four-dimensionality acquires a new structural argument: the Swift--Hohenberg \hyperref[ref-2]{[2]} curvature term is exactly scale-invariant at $d=4$. The gauge algebra is identified as $E_6$, read off the pattern's own group structure via the binary tetrahedral group and the McKay correspondence \hyperref[ref-3]{[3]} rather than imposed to fit a target. The geometric core is now machine-checked: eight Lean~4 modules compile cleanly with no \texttt{sorry}, \texttt{admit}, or \texttt{axiom}.

\textbf{What is excluded by theorem.} SO(8) cannot be the gauge algebra, by two independent proofs. The Standard Model algebra does not embed in $\mathfrak{so}(8)$ by any route. The anisotropy coefficient $\xi_2=-1/384$ is not derivable from the stated lattice. Both time-step values stated in v92 violate the framework's own stability bound. Three generations is \textbf{not} a derived result: five candidate mechanisms were tested and all five are closed. Monopole absence, claimed in earlier versions, is inconsistent with an $E_6$ gauge group.

\textbf{What remains open} is stated exhaustively in \S~IX, classified by the type of work each item requires. Every correction made during verification --- including corrections to the author's own prior output --- is recorded in the appendices, and every externally attributable claim carries a linked numerical citation.

The framework claims substantially less than v92 did. What it now claims has been checked --- by hand, by simulation, by independent reproduction, and now by machine.
\end{abstract}
\vspace{1.2cm}
\hrule
\vspace{1.4cm}
'''

# Remove the markdown title block lines from body (first ~12 lines hold title metadata)
# Find where "How to Read This Document" starts and drop everything before it
idx = body.find('How to Read This Document')
assert idx > 0
cut = body.rfind('\\subsection*{', 0, idx)
assert cut >= 0
body = body[cut:]

doc = preamble + title_block + body + '\n\\end{document}\n'
open(DST, 'w', encoding='utf-8').write(doc)
print('wrote', DST, len(doc), 'chars')
