#!/bin/bash
cd ~/workspace/research/irh-v95-wt/programme/v95; source ~/miniconda3/bin/activate jacobian-conjecture-2d
for i in 1 2 3; do lualatex -interaction=nonstopmode IRH_v95_draft.tex > /tmp/irh_run$i.out 2>&1; echo "pass $i EXIT $?"; done
L=IRH_v95_draft.log
echo "errors: $(grep -c '^!' $L)"; echo "undefined: $(grep -ci 'undefined' $L)"; echo "missing chars: $(grep -c 'Missing character' $L)"; echo "overfull: $(grep -c Overfull $L)"; pdfinfo IRH_v95_draft.pdf | grep Pages
