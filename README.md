# cross_section
A cross section calculation handbook for students

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

The python codes in this repository are licensed under MIT license.

## What are the goals of this handbook?

0. Unified notation system
1. Derivation of cross section, tree-level and a bit loop
2. Electromagnetism and weak interaction covered
3. Reference of textbooks for each step
4. Reference of literatures for final numerical results
5. Comparison to latest experiment results
6. Focus on simplified theory
7. Python codes provided

## The short-term plan: process to cover

1. WIMP - nucleus
2. dark photon - electron
3. axion - electron
4. neutrino - quark & nucleus
5. neutrino - lepton

## How to generate the handbook

```
latexmk -C && latexmk --lualatex main.tex --shell-escape
```

## Credit of template usage

The template used in LaTex codes is modified based on [Physics Book Template](https://www.overleaf.com/latex/templates/physics-book-template/ncpnbrqpttwv), published at Overleaf under [Creative Commons CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/), by [Charles Averill](https://github.com/CharlesAverill).
