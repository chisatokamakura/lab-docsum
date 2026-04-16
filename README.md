# lab-docsum 

[![doctests](https://github.com/chisatokamakura/lab-docsum/actions/workflows/doctest.yml/badge.svg)](https://github.com/chisatokamakura/lab-docsum/actions/workflows/doctest.yml)
[![integration-tests](https://github.com/chisatokamakura/lab-docsum/actions/workflows/integration-tests.yml/badge.svg)](https://github.com/chisatokamakura/lab-docsum/actions/workflows/integration-tests.yml)
[![flake8](https://github.com/chisatokamakura/lab-docsum/actions/workflows/flake8.yaml/badge.svg)](https://github.com/chisatokamakura/lab-docsum/actions/workflows/flake8.yaml)
[![PyPI version](https://img.shields.io/pypi/v/cmc-cs040-chisatokamakura.svg)](https://pypi.org/project/cmc-cs040-chisatokamakura/)
[![coverage](https://codecov.io/gh/chisatokamakura/lab-docsum/branch/main/graph/badge.svg)](https://codecov.io/gh/chisatokamakura/lab-docsum)

This project is a command-line LLM assistant. It contains a variety of tools that is able to be called both automatically and manually.

## This project demonstrates: 

1. How to write "test cases for your test cases"
2. How to get LLMs working in github actions
3. How to let other people "pip install" your projects

Link to my PYPI project: https://pypi.org/project/cmc-cs040-chisatokamakura/

## Animated GIF Demo: 

![Demo of lab-docsum](images/demo.gif)

### Webpage Project

This example is good because it shows how the model can analyze a website project and its structure, identifying individual files that include HTML files, styling files, and images.

```
$ cd test_projects/chisatokamakura.github.io
$ chat
chat> what files are in this project?
The project contains the following files: README.md, aljonaandbruno.jpg, anna.jpg, gabbiandgui.jpg, hanyu.jpg, icedance.html, index.html, javi.jpeg, kaori.jpg, mao.jpg, men.html, milanmascot.png, pairs.html, shoma.jpg, style.css, suiandhan.jpg, virtuemoir.jpg, and women.html.
```

### Markdown Project

This example is good because it shows how the model can analyze a code-based project and identify its components, which include configuration files and output images.

```
$ cd test_projects/project01
$ chat
chat> how many files are in this project?
There are 8 files in this project.
```

### Webscraping Project

This is a good example because it shows how the model can interpret multiple types of files
from an external webpage.
```
$ cd test_projects/project02_webscraping
$ chat
chat> chat> is the requests lib used in this project?
No, the requests library does not appear to be used in this project, as there are no files suggesting its use.
```