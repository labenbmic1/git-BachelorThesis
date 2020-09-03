# Labenbacher Michael 1.0.0.nightly.001000000010024
Have fun. Please report bugs to michael@labenbacher.at or m.labenbacher@tum.de. (It's not perfect I know, but it was a starting point for the Bachelor Thesis.)<br /><br />

Compile (MiKTeX/TeXstudio):<br />
1/2x pdflatex, biber, 2/3x pdlfatex<br /><br />
Befehle:<br />
PdfLaTeX: pdflatex.exe -synctex=1 -interaction=nonstopmode --shell-escape --main-memory=100000000 --extra-mem-top=100000000 --extra-mem-bot=100000000 %.tex<br />
Biber: biber.exe %<br /><br />
Erzeugen:<br />
Standard Bibliographieprogramm: txs:///biber --validate_datamodel<br />
Standard Index Tool: txs:///makeindex<br /><br />

Changes:<br />
Added todonotes.<br />
Small minor changes.