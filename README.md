# scilaunch

A tiny program for you that lays the foundation for great discoveries.

![scilaunch](scilaunch_logo.png)

![License](https://img.shields.io/badge/license-BSD-blue.svg)
![Python](https://img.shields.io/badge/python->=3.8-blue.svg)
![Environment](https://github.com/SHEscher/scilaunch/actions/workflows/tests.yaml/badge.svg)

`[Last update 2023-11-03 | v.0.1.1]`

## Description

`scilaunch` helps you to set up your research project:

1. it creates a canonical directory structure tailored for research projects

2. it prepares your research code as `Python` package ready for `import`

3. `scilaunch` offers to set up a `conda` environment, and prepares it as `jupyter` kernel

4. and `scilaunch` can init your `git` repository

---

The project structure can be populated with other programming languages (`R`, `matlab`, etc.) as well.

## Getting started

### Install `scilaunch`

Ideally install `scilaunch` into your global/base `Python` environment, which should be `python>=3.8`.

Install from PyPI:
```shell
pip install -U scilaunch
```

Alternatively, install from the GitHub repo:
```shell
pip install -U git+https://github.com/SHEscher/scilaunch.git
```

It is also recommended to have [`conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed.

### Run `scilaunch`

Simply run `scilaunch` via the command line:

```shell
# Assuming you are in the parent directory that hosts your research project
scilaunch

# or provide the parent dir by running
scilaunch PATH/TO/PARENT/DIR
```

Then, you will be asked to provide some information relevant to your project.


When running `scilaunch` the first time, you will set some default values, which will ease your life for upcoming launches of research projects.

You can still change these default values in `~/.cookiecutterrc` at a later stage.

---

## Cookiecutter templates

`scilaunch` is a wrapper around the great [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) package and is mainly built around this template: [research-project](https://github.com/SHEscher/research-project).

To build your own templates, check out the `cookiecutter` [docs](https://cookiecutter.readthedocs.io/en/stable/index.html). Feel free to fork & adapt the [research-project](https://github.com/SHEscher/research-project) template.

Check out the `cookiecutter` [documentation](https://cookiecutter.readthedocs.io/en/stable/index.html) for more information on the `~/.cookiecutterrc`.

---

## TODO's

- [ ] allow to pass other `cookiecutter` templates
- [ ] add proper docs
- [ ] add files in `/.github/ISSUE_TEMPLATE/`
- [ ] add `CONTRIBUTING.md`
