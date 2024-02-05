# Contributing

Contributions are very welcome, and credit will always be given!

## Templating

`scilaunch` is a wrapper around the template engine [`cookiecutter`](https://github.com/cookiecutter/cookiecutter).
That means, that the development of `scilaunch` is closely related to the development of the template [`research-project`](https://github.com/SHEscher/research-project).

To build your own templates, check out the `cookiecutter` [docs](https://cookiecutter.readthedocs.io/en/stable/index.html).
Feel free to fork & adapt the [research-project](https://github.com/SHEscher/research-project) template.
It is planned to optionally use other research-related templates in the future as well.

## Setup for development

Fork &/or clone the repo:

```shell
git clone https://github.com/SHEscher/scilaunch.git
```

Install the dependencies for development,
ideally in a virtual environment in editable mode:

```shell
cd scilaunch
pip install -e ".[develop,docs]"
```

At this stage, the project is small. Contributions via pull requests are welcome.
A more comprehensive contribution guide will be added in the future, in case the project grows.

## Future directions & ToDo's

- [ ] extend `docs/`
- [ ] allow passing other `cookiecutter` templates
- [ ] add files in `/.github/ISSUE_TEMPLATE/`
- [ ] *midterm ideas*: `scilaunch` methods after project is initialized, e.g.:
  - [ ] `scilaunch docs`  create docs website
  - [ ] `scilaunch add` e.g. LICENSE (runs only LICENSE template)
  - [ ] ...
