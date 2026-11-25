"""Run the 14 AI-tell heuristics of PROSE_CHECKLIST.md §B on a .tex body.
Usage: python ai_tell_heuristics.py file.tex [--show N]
Body = \\begin{document} .. \\begin{thebibliography} (or \\end{document}).
Math stripped ($..$, \\(..\\), \\[..\\], display envs) -> X, except heuristics 10 and 13 which
need the raw '$'. Comments removed."""
import re, sys
src = open(sys.argv[1]).read()
show = int(sys.argv[sys.argv.index('--show')+1]) if '--show' in sys.argv else 0
b = src.find('\\begin{document}'); e = src.find('\\begin{thebibliography}')
if e < 0: e = src.find('\\end{document}')
body = src[b:e]
body = re.sub(r'(?<!\\)%.*', '', body)
raw = body
nomath = re.sub(r'\\begin\{(equation|align|gather|multline|eqnarray)\*?\}.*?\\end\{\1\*?\}', ' X ', body, flags=re.S)
nomath = re.sub(r'\\\[.*?\\\]', ' X ', nomath, flags=re.S)
nomath = re.sub(r'\$\$.*?\$\$', ' X ', nomath, flags=re.S)
nomath = re.sub(r'\$[^$]*\$', 'X', nomath)
text_words = re.sub(r'\\[a-zA-Z]+\*?', ' ', nomath)
words = len(re.findall(r'[A-Za-z]{2,}', text_words))
lines = [l for l in nomath.split('\n') if l.strip()]
I = re.I
res = {}
def count(name, pat, s=nomath, flags=I|re.M):
    m = list(re.finditer(pat, s, flags)); res[name] = m; return len(m)
count('1 bold', r'\*\*[^*]+\*\*|\\textbf\{')
count('2 list lines', r'^\s*([-*•]|\d+\.)\s|\\item\b')
count('3 bold-header items', r'^\s*([-*]|\d+\.|\\item)\s+(\*\*[^*]+\*\*|\\textbf\{[^}]*\}):')
count('4 em-dash', r'—|---')
count('5 excess vocab', r'\b(delv(e|es|ed|ing)|underscor(e|es|ed|ing)|showcas(e|es|ed|ing)|crucial(ly)?|notabl(e|y)|pivotal|intricate|comprehensive|additionally|insights?|enhanc(e|es|ed|ing)|leverag(e|es|ed|ing)|robust(ly)?|seamless(ly)?|furthermore|moreover|testament|landscape|realm|tapestry|foster(s|ed|ing)?)\b')
count('6 significance', r'\b(plays? an? (crucial|pivotal|vital|key|significant) role|serves as an?|stands as|is a testament|setting the stage|evolving landscape|focal point|indelible|deeply rooted|reflects broader)\b')
count('7 hedges', r'\b(it is (important|worth|crucial) (to note|noting)|it should be noted|in (summary|conclusion), |not only\b.*\bbut also)\b')
count('8 participle tail', r',\s+(highlighting|underscoring|emphasizing|ensuring|reflecting|showcasing|symbolizing|contributing to|fostering)\b')
# 9: tricolon per paragraph >=2
paras = re.split(r'\n\s*\n', nomath)
tri = [p for p in paras if len(re.findall(r'\b[\w-]+, [\w-]+,? and [\w-]+\b', p)) >= 2]
res['9 tricolon paras(>=2)'] = tri
# 10 sentence starts with symbol: raw text, outside displays
rawnodisp = re.sub(r'\\begin\{(equation|align|gather|multline)\*?\}.*?\\end\{\1\*?\}', ' DISPLAY ', raw, flags=re.S)
rawnodisp = re.sub(r'\\\[.*?\\\]', ' DISPLAY ', rawnodisp, flags=re.S)
rawnodisp = re.sub(r'\\begin\{(tabular|tabularx|xltabular)\}.*?\\end\{\1\}', ' TABLE ', rawnodisp, flags=re.S)
count('10 sentence starts $', r'(^|[.!?]\s+)\$', s=rawnodisp)
count('11 empty assurance', r'\b(clearly|obviously|trivially|it is easy to see|straightforward(ly)?)\b')
count('12 we have that', r'\bwe have that\b')
count('13 symbolic logic', r'\$\\(forall|exists|therefore|Rightarrow)\$', s=rawnodisp)
count('14 bare eq ref', r'\b(eq(uation)?\.?|\\eqref)\s*\(?\d+\)?', s=raw)
print(f'body words ~{words}, nonblank body lines {len(lines)}')
for k, v in res.items():
    extra = ''
    if k.startswith('1 '): extra = f'  ({1000*len(v)/max(words,1):.2f}/1000w)'
    if k.startswith('4 '): extra = f'  ({1000*len(v)/max(words,1):.2f}/1000w)'
    if k.startswith('2 '): extra = f'  ({100*len(v)/max(len(lines),1):.1f}% of lines)'
    print(f'{k}: {len(v)}{extra}')
    if show:
        for m in v[:show]:
            if isinstance(m, str): print('   ..', m.strip()[:160].replace('\n',' '))
            else:
                s = m.string; i = m.start(); print('   ..', s[max(0,i-60):i+80].replace('\n',' '))
