import os

env = Environment(
    tools=['pdflatex', 'pdftex', 'tex'],
    )

# Look in standard directory ~/texmf for .sty files
env['ENV']['TEXMFHOME'] = os.path.join(os.environ['HOME'],'texmf')

env.AppendUnique(
    #PDFLATEXFLAGS=['-file-line-error', '-interaction=batchmode'],
    #BIBTEXFLAGS='-terse',
    )

env.PrependENVPath('PATH', '/s/texlive-2010/bin')

pdf = env.PDF('main.tex')[0]


ps = env.Command('main.ps', pdf, 'pdftops $SOURCE $TARGET')
Default(ps)
Depends(pdf, [
	 Glob('section/*.tex'),
#        Glob('figures/*.c'),
#        Glob('figures/why-merge/*.txt'),
#        Glob('figures/traps/*.c'),
#        Glob('figures/traps/*.pdf'),
#        Glob('figures/traps/*.tex'),
        'sig-alternate.cls',
        ])
