# Labenbacher Michael 1.0.1.nightly.001000000020016
Have fun. Please report bugs to michael@labenbacher.at or m.labenbacher@tum.de. (It's not perfect I know, but it was a starting point for the Bachelor Thesis.)<br /><br />

Compile (MiKTeX/TeXstudio):<br />
1/2x pdflatex, biber, 2/3x pdlfatex<br /><br />

Befehle:<br />
PdfLaTeX: pdflatex.exe -synctex=1 -interaction=nonstopmode --shell-escape --main-memory=100000000 --extra-mem-top=100000000 --extra-mem-bot=100000000 %.tex<br />
Biber: biber.exe %<br /><br />

Erzeugen:<br />
Standard Bibliographieprogramm: txs:///biber --validate_datamodel<br />
Standard Index Tool: txs:///makeindex<br /><br />

Changes in 1.0.1.nightly.001000000020016:<br />
Extended the macro \TUM@ifpackageloaded for check for multiple packages (and/or).<br />
Added autoref for theorems (normally one should only use ref...).<br />
Added another theorem-style example (Ex-) package.<br />
Added -r option to imakeidx.<br />
Added microtype implementations (toc, lof, etc.).<br />
Small changes and shorten compilation time.<br /><br />

Changes in 1.0.1.nightly.001000000020013:<br />
Bug with {tikz/pgf}-externalize library and {nicematrix, chemformula} fixed.<br />
Shifted [bookmarks]-option from {hyperref} to {bookmark}.<br />
Extended the macro \TUM@ifpackageloaded for check for multiple packages.<br />
Added {scrlayer-notecolumn}. (Optional with [notecolumn=true], because not everybody needs this, it's a "Proof of Concept" but way better then {marginnote}.) Furthermore I have given an example to change the right/left margin from 1-1 to 2-3 (for example) with typearea.<br />
Improved tumheader.sty, (Long headmark works now (see example), if it realy can not be avoided to shorten it...)<br />
Small minor changes and more examples.<br /><br />

Changes in 1.0.1.nightly.001000000010001:<br />
Bug with {tikz/pgf}-externalize-library and {imakeidx, todonotes, showframe, (geometry, pdfpages)} fixed.<br />
Added some (requested) TikZ-examples.<br />
Small minor changes and white spaces removed.<br /><br />

Changes in 1.0.0.nightly.001000000010024:<br />
Added {todonotes}.<br />
Small minor changes.