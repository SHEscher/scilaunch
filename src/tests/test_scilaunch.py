"""Tests for scilaunch package."""

# %% Import
import shutil
from pathlib import Path

# import pytest
import toml
from scilaunch import configs, project

# %% Set global vars & paths  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

SCILAUNCH_CACHE = Path.home() / ".cache/scilaunch"


# %% Test Functions  o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o


# scilaunch.configs
def test_configs():
    """Test create_config()."""
    assert Path(configs.path_to.templates.local.cookiecutterrc).exists()


# scilaunch.project
def test_create_cookiecutterrc():
    """Test create_cookiecutterrc()."""
    if project.COOKIECUTTERRC.exists():
        # Make backup
        project.COOKIECUTTERRC.rename(project.COOKIECUTTERRC.with_suffix(".bak"))
    project.create_cookiecutterrc(no_input=True)
    assert project.COOKIECUTTERRC.exists()
    if project.COOKIECUTTERRC.with_suffix(".bak").exists():
        # Restore backup
        project.COOKIECUTTERRC.with_suffix(".bak").rename(project.COOKIECUTTERRC)


def test_create():
    """Test create()."""
    test_project_name = "testproject"
    project.create(
        out_dir=SCILAUNCH_CACHE,
        create_cc_rc=False,
        no_input=True,
        extra_context={
            "full_name": "test_author",
            "email": "test@test.ts",
            "github_username": "Tester",
            "project_name": test_project_name,
            "create_conda_env": "n",
            "init_git": "n",
        },
    )
    assert (SCILAUNCH_CACHE / test_project_name).exists()
    assert toml.load(SCILAUNCH_CACHE / test_project_name / "pyproject.toml")["project"]["name"] == test_project_name

    # Remove test project
    if (SCILAUNCH_CACHE / test_project_name).exists():
        shutil.rmtree(SCILAUNCH_CACHE / test_project_name)

    # Check if cache dir is empty, if so remove it
    if not list(SCILAUNCH_CACHE.iterdir()):
        SCILAUNCH_CACHE.rmdir()
