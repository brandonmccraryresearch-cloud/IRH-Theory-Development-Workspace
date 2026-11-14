from fontTools.ttLib import TTFont
import glob
paths = {
 "FiraMath": glob.glob("/home/hatch/miniconda3/envs/jacobian-conjecture-2d/texlive/2026/texmf-dist/fonts/opentype/public/firamath/FiraMath-Regular.otf")[0],
 "FiraSans": "/home/hatch/miniconda3/envs/jacobian-conjecture-2d/texlive/2026/texmf-dist/fonts/opentype/public/fira/FiraSans-Regular.otf",
 "NotoSansMath": "/usr/share/fonts/truetype/noto/NotoSansMath-Regular.ttf",
 "NotoSans": "/home/hatch/miniconda3/envs/jacobian-conjecture-2d/texlive/2026/texmf-dist/fonts/truetype/google/noto/NotoSans-Regular.ttf",
}
for name, p in paths.items():
    try:
        f = TTFont(p)
        cmap = f.getBestCmap()
        print(name, {hex(c): (c in cmap) for c in [0x2208, 0x2090, 0x2216, 0x03C4, 0x2211]})
    except Exception as e:
        print(name, "ERR", repr(e))
