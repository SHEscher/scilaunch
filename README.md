# scilaunch

A tiny program for you that lays the foundation for great discoveries.

![scilaunch](https://github.com/SHEscher/scilaunch/raw/main/scilaunch_logo.png)

![Environment](https://github.com/SHEscher/scilaunch/actions/workflows/tests.yaml/badge.svg)
![Python](https://img.shields.io/badge/python->=3.8-blue.svg)
[![license: BSD](https://img.shields.io/badge/license-BSD-purple.svg)](https://github.com/shescher/scilaunch/blob/master/LICENSE)
[![documentation](https://img.shields.io/badge/docs-scilaunch-yellow.svg?style=flat)](https://shescher.github.io/scilaunch)
[![GitHub package version](https://img.shields.io/github/v/tag/shescher/scilaunch)](https://github.com/shescher/scilaunch/tags)
![Last update](https://img.shields.io/badge/last_update-Dec_20,_2025-green)

## Description

`scilaunch` helps you to set up your research project:

1. it creates a canonical directory structure tailored for research projects
    ```
    🚀 yourgreatstudy/
    ├── 📄 README.md
    ├── 📂 code
    │   ├── 📁 Rscripts
    │   ├── 📁 configs
    │   ├── 📂 notebooks
    │   │   └── 🐍 yourgreatstudy.ipynb
    │   ├── 📁 tests
    │   └── 📂 yourgreatstudy
    │       ├── 🐍 __init__.py
    │       └── 📁 preprocessing
    ├── 📂 data
    │   ├── 📋 participants.tsv
    │   ├── 📁 sub-01
    │   ├── 📁 sub-02
    │   └── 📁 sub-03
    ├── 📂 literature
    │   ├── 📁 pdfs
    │   └── 📙 yourgreatstudy.bib
    ├── 📂 organisation
    │   ├── 📁 ethics
    │   ├── 📁 participation_forms
    │   ├── 📁 preregistration
    ├── 📂 publications
    │   ├── 📁 articles
    │   ├── 📁 poster
    │   └── 📁 presentations
    ├── 📄 pyproject.toml
    ├── 📂 results
    │   └── 📁 datavisualization
    └── 🐍 setup.py
    ```
2. `scilaunch` prepares your research code as `Python` package ready for `import`

3. `scilaunch` offers to set up a `conda` environment, and prepares it as `jupyter` kernel

4. and `scilaunch` can init your `git` repository

---

The project structure can be populated with other programming languages (`R`, `matlab`, etc.) as well.

Check out the `scilaunch` [documentation](https://shescher.github.io/scilaunch) 🚀 for more information.

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

### 🚀 Run `scilaunch`

Simply run `scilaunch` via the command line:

```shell
# Assuming you are in the parent directory that should host your research project
scilaunch
```

or provide the parent directory of your project by running:

```shell
scilaunch  PATH/TO/PARENT/DIR
```

Then, you will be asked to provide some information relevant to your project.


When running `scilaunch` the first time, you will set some default values, which will ease your life for upcoming launches of research projects.

You can still change these default values in `~/.cookiecutterrc` at a later stage.

---

## Cookiecutter templates

`scilaunch` is a wrapper around the great [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) package
and is mainly built around this template: [`research-project`](https://github.com/SHEscher/research-project).

For how to build your own template(s) and to contribute to this project, please check out: `CONTRIBUTING.md`.

Note, after running `scilaunch` the first time, you can adapt your default values in `~/.cookiecutterrc` at any time.
Check out the `cookiecutter` [documentation](https://cookiecutter.readthedocs.io/en/stable/index.html) for more information on the `~/.cookiecutterrc`.
