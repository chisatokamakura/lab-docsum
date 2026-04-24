# lab-docsum 

[![doctests](https://github.com/chisatokamakura/lab-docsum/actions/workflows/doctest.yml/badge.svg)](https://github.com/chisatokamakura/lab-docsum/actions/workflows/doctest.yml)
[![integration-tests](https://github.com/chisatokamakura/lab-docsum/actions/workflows/integration-tests.yml/badge.svg)](https://github.com/chisatokamakura/lab-docsum/actions/workflows/integration-tests.yml)
[![flake8](https://github.com/chisatokamakura/lab-docsum/actions/workflows/flake8.yaml/badge.svg)](https://github.com/chisatokamakura/lab-docsum/actions/workflows/flake8.yaml)
[![PyPI version](https://img.shields.io/pypi/v/cmc-cs040-chisatokamakura.svg)](https://pypi.org/project/cmc-cs040-chisatokamakura/)
[![coverage](https://codecov.io/gh/chisatokamakura/lab-docsum/branch/main/graph/badge.svg)](https://codecov.io/gh/chisatokamakura/lab-docsum)

This project is a command-line LLM assistant. It contains a variety of tools that is able to be called both automatically and manually.

This is a demo of the LLM assistant.

![Demo of lab-docsum](images/demo.gif)

## Examples

This example shows how the model can analyze a website project and its structure, identifying individual files that include HTML files, styling files, and images.

```
$ cd test_projects/chisatokamakura.github.io
$ chat
chat> what files are in this project?
The project contains the following files: README.md, aljonaandbruno.jpg, anna.jpg, gabbiandgui.jpg, hanyu.jpg, icedance.html, index.html, javi.jpeg, kaori.jpg, mao.jpg, men.html, milanmascot.png, pairs.html, shoma.jpg, style.css, suiandhan.jpg, virtuemoir.jpg, and women.html.
```

This shows how the model can analyze the structure of a code-based project, determining properties such as the number of files contained.

```
$ cd test_projects/project01
$ chat
chat> how many files are in this project?
There are 8 files in this project.
```

This example shows how the model inspect the files used in the project and determine if specific libraries are used by searching for relevant files.
```
$ cd test_projects/project02_webscraping
$ chat
chat> chat> is the requests lib used in this project?
No, the requests library does not appear to be used in this project, as there are no files suggesting its use.
```

### More examples

My program can optionally take a command line argument that is a message and pass it to the LLM. 
```
$ chat 'what files are in test_projects?'
The files in the test_projects directory are test_projects/chisatokamakura.github.io, test_projects/project01, and test_projects/project02_webscraping.
```

### Agent in Action
These are examples of the LLM agent in action, where it can create and delete files and create git commits.

#### Creating a File
This example demonstrates that ```chat``` can can create files when asked and these files are automatically added to the git repo.

```
$ ls
__pycache__                             pyproject.toml
chat.py                                 README.md
cmc_cs040_chisatokamakura.egg-info      test_projects
dist                                    tools
htmlcov                                 venv
images
$ git log --oneline -n 3
b3c0df5 (HEAD -> main) [docchat] Initial hello world commit
1425b2f [docchat] Initial commit
78814f8 [docchat] Initial commit
$ chat
chat> create a hello_world python file
Created the file hello_world.py
chat> ^C
$ ls
__pycache__                             images
chat.py                                 pyproject.toml
cmc_cs040_chisatokamakura.egg-info      README.md
dist                                    test_projects
hello_world.py                          tools
htmlcov                                 venv
$ git log --oneline -n 3
ac3660f (HEAD -> main) [docchat] Initial hello world commit
b3c0df5 [docchat] Initial hello world commit
1425b2f [docchat] Initial commit
```

#### Deleting a File

