"""
Tests for scilaunch package.

Run with:

    pytest --cov --cov-report=html

"""

# %% Import
import shutil
from pathlib import Path

import pytest
import toml
import yaml
from scilaunch import configs, project

# %% Set global vars & paths >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o


@pytest.fixture()
def temp_scilaunch_cache():
    """Create temp cache dir."""
    scilaunch_cache = Path.home() / ".cache/scilaunch"
    test_project_name = "testproject"

    yield scilaunch_cache, test_project_name

    # Tear down
    # Remove the test project
    if (scilaunch_cache / test_project_name).exists():
        shutil.rmtree(scilaunch_cache / test_project_name)

    # Check if cache dir is empty, if so remove it
    if not list(scilaunch_cache.iterdir()):
        scilaunch_cache.rmdir()


@pytest.fixture()
def temp_cookiecutterrc():
    """Create temporary ~/.cookiecutterrc file."""
    if project.COOKIECUTTERRC.exists():
        # Make backup
        project.COOKIECUTTERRC.rename(project.COOKIECUTTERRC.with_suffix(".bak"))

    # Create dir
    project.COOKIECUTTERRC.parent.mkdir(parents=True, exist_ok=True)

    # Create temporary cookiecutterrc file (use different 'boolean' styles)
    cookiecutterrc = {
        "default_context": {
            "full_name": "Test Author",
            "email": "pytest@author.me",
            "create_conda_env": "y",
            "init_git": "no",
            "use_black": False,
            "linting": "ruff",
        },
        "abbreviations": {
            "gh": "https://github.com/{0}.git",
            "rp": "https://github.com/SHEscher/research-project.git",
        },
    }
    # Write temporary file
    with project.COOKIECUTTERRC.open("w") as f:
        yaml.dump(cookiecutterrc, f)

    # Read updated file
    with project.COOKIECUTTERRC.open() as f:
        cookiecutterrc = yaml.safe_load(f)

    yield cookiecutterrc

    # Tear down
    if project.COOKIECUTTERRC.exists():
        project.COOKIECUTTERRC.unlink()
    if project.COOKIECUTTERRC.with_suffix(".bak").exists():
        # Restore backup
        project.COOKIECUTTERRC.with_suffix(".bak").rename(project.COOKIECUTTERRC)


# %% Test Functions o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o


# scilaunch.configs
def test_configs():
    """Test create_config()."""
    assert Path(configs.path_to.templates.local.cookiecutterrc).exists()


# scilaunch.project
def test__check_str_to_bool():
    """Test _check_str_to_bool()."""
    for val in ["n", "No", "False", "f", "0", "off"]:
        assert not project._check_str_to_bool(val)

    for val in ["y", "Yes", "true", "T", "1", "on"]:
        assert project._check_str_to_bool(val)

    for val in ["a", "b0", "D", "TR", "fA", "g"]:
        assert project._check_str_to_bool(val) is None


def test__check_int_to_bool():
    """Test _check_int_to_bool()."""
    for val in [0, 0.0]:
        assert not project._check_int_to_bool(val)
    for val in [1, 1.0]:
        assert project._check_int_to_bool(val)
    for val in [2, 2.0, -1, -1.0]:
        assert project._check_int_to_bool(val) is None


def test_check_booleans_in_cookiecutterrc(capsys, temp_cookiecutterrc):
    """Test check_booleans_in_cookiecutterrc()."""
    # Create temporary cookiecutterrc file
    _ = temp_cookiecutterrc

    # Update boolean values
    project.check_booleans_in_cookiecutterrc()
    out, _ = capsys.readouterr()  # _ = err

    # Read updated file
    with project.COOKIECUTTERRC.open() as f:
        cookiecutterrc = yaml.safe_load(f)

    # Check if boolean values are updated
    assert cookiecutterrc["default_context"]["create_conda_env"] is True
    assert cookiecutterrc["default_context"]["init_git"] is False
    assert cookiecutterrc["default_context"]["use_black"] is False
    assert ".cookiecutterrc boolean default values ..." in out

    # Check in valid case
    cookiecutterrc["default_context"]["create_conda_env"] = "invalid"
    with project.COOKIECUTTERRC.open("w") as f:
        yaml.dump(cookiecutterrc, f)

    with pytest.raises(TypeError, match="Invalid type for 'create_conda_env':"):
        project.check_booleans_in_cookiecutterrc()


def test_create_cookiecutterrc(capsys, temp_cookiecutterrc):
    """Test create_cookiecutterrc()."""
    # Create temporary cookiecutterrc file
    _ = temp_cookiecutterrc

    # Test case when .cookiecutterrc file is present
    project.create_cookiecutterrc(verbose=True)
    out, _ = capsys.readouterr()  # _ = err
    assert f"Using existing {project.COOKIECUTTERRC} to fill defaults." in out
    assert f"Updating {project.COOKIECUTTERRC} boolean default values" in out

    # Test case when no file is present
    # Remove .cookiecutterrc file temporarily
    project.COOKIECUTTERRC.unlink()  # if there was a file before, it will be restored in teardown

    project.create_cookiecutterrc(no_input=True)
    assert project.COOKIECUTTERRC.exists()


def test_create(temp_scilaunch_cache):
    """Test create()."""
    scilaunch_cache, test_project_name = temp_scilaunch_cache

    project.create(
        out_dir=scilaunch_cache,
        create_cc_rc=False,
        no_input=True,
        extra_context={
            "full_name": "test_author",
            "email": "test@test.ts",
            "project_name": test_project_name,
            "create_conda_env": False,
            "init_git": False,
        },
    )
    assert (scilaunch_cache / test_project_name).exists()
    assert toml.load(scilaunch_cache / test_project_name / "pyproject.toml")["project"]["name"] == test_project_name


# o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
