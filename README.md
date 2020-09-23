# Labenbacher Michael 1.0.3.nightly.001000000010002
Have fun. Please report bugs to michael@labenbacher.at or m.labenbacher@tum.de. (It's not perfect I know, but it was a starting point for the Bachelor Thesis.) Empty: [main.pdf](main.pdf), Example: [main-example.pdf](main-example.pdf)<br /><br />

## Compile (MiKTeX/TeXstudio):<br />
1/2x (pdf/lua)latex, biber, bib2gls, 2/3x (pdf/lua)latex<br /><br />

Befehle:<br />
(Pdf/Lua)LaTeX: (pdf/lua)latex.exe --shell-escape -synctex=1 -interaction=nonstopmode %.tex<br />
Biber: biber.exe %<br />
Makeindex: bib2gls.exe --group %<br /><br />

Erzeugen:<br />
Standardcompiler: txs:///(pdf/lua)latex<br />
Standard Bibliographieprogramm: txs:///biber --validate_datamodel<br />
Standard Index Tool: txs:///bib2gls<br /><br />

TeX memory for tikz-externalize (if there are to many datapoints (normally one should instead use python/matlab...)):<br />
1. Run: initexmf --edit-config-file=(pdf/lua)latex<br />
2. Write+Save into file (* is normally sufficient to increase only this)<br />
extra_mem_top 	= 1000000000<br />
extra_mem_bot 	= 1000000000<br />
main_memory 	= 100000000 (*)<br />
3. Run: initexmf --dump=(pdf/lua)latex<br /><br />

## Compile WINDOWS: (Commandline)<br />
cd C:\\{path...}<br />
set TEXINPUTS=.;.\images\\\\;.\tables\\\\;.\chapters\\\\;.\files\\\\;.\listings\\\\;.\packges\\\\;%TEXINPUTS%<br />
set BIBINPUTS=.;.\references\\\\;.\glossaries\\\\;%BIBINPUTS%<br /> 

(pdf/lua)latex --shell-escape main.tex<br />
biber --validate_datamodel main<br />
bib2gls.exe --group main<br />
{...}<br />

## Compile UNIX:<br />
export TEXINPUTS=.:$HOME/{path...}//;$TEXINPUTS<br />
{...}<br /><br />

### Changes in 1.0.3.nightly.001000000010002:<br />
It's optimized for pdflatex, but one can also use lualtex now without any problems (font).<br /><br />

### Changes in 1.0.3.nightly.001000000010001:<br />
Implemented chapter-toc ((alpha) Package {scrwfile}, Command: \TUMchaptertableofcontents).<br />
Some small changes/improvements.<br /><br />

### Changes in 1.0.2.nightly.001000000020002:<br />
Added example for List of Abbreviations.<br />
Small changes.<br /><br />

### Changes in 1.0.2.nightly.001000000010009:<br />
Changed Appendix to chapter and implemented seperated TOC for Appendix.<br />
Some small changes/improvements.<br /><br />

### Changes in 1.0.2.nightly.001000000010008:<br />
Added hypersetup [pdflang].<br />
Some small changes/improvements.<br /><br />

### Changes in 1.0.2.nightly.001000000010003:<br />
Implementation of {glossaries(-extra)}. Removed {imakeidx/idxlayout}. Now one can make an Index (and List of Abbreviations, -Symbols, etc.) with bib2gls (best option available).<br />
Small changes and improvements.<br /><br />

### Changes in 1.0.1.nightly.001000000020016:<br />
Extended the macro \TUM@ifpackageloaded for check for multiple packages (and/or).<br />
Added autoref for theorems (normally one should only use ref...).<br />
Added another theorem-style example (Ex-) package.<br />
Added -r option to imakeidx.<br />
Added microtype implementations (toc, lof, etc.).<br />
Small changes and shorten compilation time.<br /><br />

### Changes in 1.0.1.nightly.001000000020013:<br />
Bug with {tikz/pgf}-externalize library and {nicematrix, chemformula} fixed.<br />
Shifted [bookmarks]-option from {hyperref} to {bookmark}.<br />
Extended the macro \TUM@ifpackageloaded for check for multiple packages.<br />
Added (PoC) {scrlayer-notecolumn}. (Optional with [notecolumn=true], because not everybody needs this, it's a "Proof of Concept" but way better then {marginnote}.) Furthermore I have given an example to change the right/left margin from 1-1 to 2-3 (for example) with typearea.<br />
Improved tumheader.sty, (Long headmark works now (see example), if it realy can not be avoided to shorten it...)<br />
Small minor changes and more examples.<br /><br />

### Changes in 1.0.1.nightly.001000000010001:<br />
Bug with {tikz/pgf}-externalize-library and {imakeidx, todonotes, showframe, (geometry, pdfpages)} fixed.<br />
Added some (requested) TikZ-examples.<br />
Small minor changes and white spaces removed.<br /><br />

### Changes in 1.0.0.nightly.001000000010024:<br />
Added {todonotes}.<br />
Small minor changes.