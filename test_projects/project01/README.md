# Markdown to HTML compiler

![](https://github.com/chisatokamakura/project01/actions/workflows/doctests.yaml/badge.svg)&nbsp;
![](https://github.com/chisatokamakura/project01/actions/workflows/flake8.yaml/badge.svg)&nbsp;
![](https://github.com/chisatokamakura/project01/actions/workflows/command_line.yaml/badge.svg)&nbsp;

A simple project for converting markdown files to HTML.

Basic usage:
```
$ markdown-compiler example/README.md 
```

<img src='screenshot_no_css.png' width=300px> 

Fancy CSS formatting can be included with the flag `--add_css`: 
```
$ markdown-compiler example/README.md --add_css 
```

<img src='screenshot_yes_css.png' width=300px> 