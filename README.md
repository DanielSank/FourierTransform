# FourierTransform
Pedagogical document on the Fourier transform (and more generally on linear algebra)

## Downloading

This repository uses a git submodule, so you have to use the `--recursive` flag when cloning:

```
git clone --recursive https://github.com/DanielSank/FourierTransform.git
```

## Building

Presently, the full document does not build.
To build a chapter:

1. In the chapter's directory, conver the svg images to pdf.
The python script `make_figures.py` does this for you if you have Inkscape installed.

1. Run pdflatex on that chapter's `main.tex`.

