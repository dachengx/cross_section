# cross_section
[![DOI](https://zenodo.org/badge/662117505.svg)](https://zenodo.org/badge/latestdoi/662117505)
[![Test package](https://github.com/dachengx/cross_section/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/dachengx/cross_section/actions/workflows/pytest.yml)
[![PyPI version shields.io](https://img.shields.io/pypi/v/xsectron.svg)](https://pypi.python.org/pypi/xsectron/)
[![CodeFactor](https://www.codefactor.io/repository/github/dachengx/cross_section/badge)](https://www.codefactor.io/repository/github/dachengx/cross_section)
[![Documentation Status](https://readthedocs.org/projects/xsectron/badge/?version=latest)](https://xsectron.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/dachengx/cross_section/main.svg)](https://results.pre-commit.ci/latest/github/dachengx/cross_section/main)

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

## The short-term plan: processes to cover

1. neutrino - lepton
2. neutrino - quark & nucleus
3. WIMP - nucleon
4. dark photon - electron
5. axion - electron

## How to generate the handbook

inside `note` folder, run

```
latexmk -C && latexmk --lualatex main.tex --shell-escape
```

## How to install the package

```
pip install xsectron
```

## Credit of template usage

The template used in LaTex codes is modified based on [Physics Book Template](https://www.overleaf.com/latex/templates/physics-book-template/ncpnbrqpttwv), published at Overleaf under [Creative Commons CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/), by [Charles Averill](https://github.com/CharlesAverill).
