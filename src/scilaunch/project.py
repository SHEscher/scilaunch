"""Create project module for `scilaunch`."""

# %% Import
import json
from pathlib import Path

import yaml
from cookiecutter.main import cookiecutter
from git import Repo
from git.exc import GitCommandError

from scilaunch.configs import path_to

# %% Set global vars & paths >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

COOKIECUTTERRC = Path.home() / ".cookiecutterrc"  # destination for cookiecutterrc file


# %% Functions >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o


def _check_str_to_bool(val: str):
    """
    Check whether the given string can be converted to a boolean.

    :param str val: String to be checked.
    :return: True if the string can be converted to a boolean, False otherwise.
    :rtype: bool
    """
    if val.lower() in ["n", "no", "false", "f", "0", "off"]:
        return False
    if val.lower() in ["y", "yes", "true", "t", "1", "on"]:
        return True
    return None


def _check_int_to_bool(val: int):
    """
    Check whether the given integer can be converted to a boolean.

    :param int val: Integer to be checked.
    :return: True if the integer can be converted to a boolean, False otherwise.
    :rtype: bool
    """
    if val == 0:
        return False
    if val == 1:
        return True
    return None


def check_booleans_in_cookiecutterrc():
    """Check the validity of the `.cookiecutterrc` file."""
    # Read .cookiecutterrc file (YAML)
    with COOKIECUTTERRC.open() as f:
        cookiecutterrc = yaml.safe_load(f)

    # Read cookiecutter.json file (JSON)
    with Path(path_to.templates.local.cookiecutterrc, "cookiecutter.json").open() as f:
        cookiecutter_json = json.load(f)

    # Check whether the cookiecutterrc file has the correct boolean types
    updated = False
    for key, default_val in cookiecutter_json.items():
        if isinstance(default_val, bool):
            crc_val = cookiecutterrc["default_context"].get(key)
            if isinstance(crc_val, bool):
                continue

            # Overwrite "n" -> False and "y" -> True
            if isinstance(crc_val, str):
                crc_val = _check_str_to_bool(crc_val)
            if isinstance(crc_val, int):
                crc_val = _check_int_to_bool(crc_val)
            if not isinstance(crc_val, bool):
                msg = (
                    f"Invalid type for '{key}': {crc_val} of type {type(crc_val)}."
                    f"\nPlease check '{COOKIECUTTERRC}' and fill with valid boolean value."
                )
                raise TypeError(msg)

            # Set updated boolean default value
            cookiecutterrc["default_context"][key] = default_val if crc_val is None else crc_val
            updated = True

    # Write updated .cookiecutterrc file (YAML)
    if updated:
        print(f"\033[33m\nUpdating {COOKIECUTTERRC} boolean default values ...\033[0m")
        with COOKIECUTTERRC.open("w") as f:
            yaml.dump(cookiecutterrc, f, sort_keys=False, indent=4)


def create_cookiecutterrc(**kwargs):
    """
    Create the `.cookiecutterrc` file.

    The `.cookiecutterrc` file is stored in the home directory "`~`"
    and contains default values for the `research-project` template.

    Fore more information on the `.cookiecutterrc` file check out the `cookiecutter`
    [documentation](https://cookiecutter.readthedocs.io/en/stable/index.html).

    :param dict kwargs: Keyword arguments passed to `cookiecutter`.
    """
    # Check whether .cookiecutterrc file exists in the home directory
    if not COOKIECUTTERRC.exists():
        # Create cookiecutterrc file
        # Create cache dir
        cache_dir = Path.home() / ".cache/scilaunch"
        cache_dir.mkdir(parents=True, exist_ok=True)

        print(f"\033[34m\nSetting default values in {COOKIECUTTERRC}. This should be done only once ...\n\033[0m")
        cookiecutter(template=path_to.templates.local.cookiecutterrc, output_dir=str(cache_dir), **kwargs)

        # Move file to home directory
        # Read cache dir from json
        with Path(path_to.templates.local.cookiecutterrc, "cookiecutter.json").open() as f:
            cache_dir = cache_dir / json.load(f).get("_cache_dir")
        (cache_dir / COOKIECUTTERRC.name).rename(COOKIECUTTERRC)

        # Remove cache dir
        cache_dir.rmdir()

        # Report
        print(f"\033[32m\nCreated {COOKIECUTTERRC}\n\033[0m")

        # Print content
        with COOKIECUTTERRC.open() as f:
            print(f.read())

        print(
            f"\033[33m\nIf you want to revise your defaults settings at a later stage, "
            f"just edit the file: {COOKIECUTTERRC}.\n\033[0m"
        )

    else:
        check_booleans_in_cookiecutterrc()
        print(f"\nUsing existing {COOKIECUTTERRC} to fill defaults.\n")


def is_git_repo_up_to_date(path):
    """
    Check whether the local git repository at the given path is up to date.

    :param path: Path to the local git repository.
    :type path: str or pathlib.Path
    :return: True if the local git repository is up to date, False otherwise.
    :rtype: bool
    """
    repo = Repo(path)
    upstream = repo.remotes.origin
    try:
        upstream.fetch(kill_after_timeout=10)  # run git fetch to update the remote-tracking branches
    except GitCommandError as e:
        additional_err_msg = (
            "\033[31mUnable to fetch data from remote repository! Check your internet connection!\033[0m"
        )
        raise GitCommandError(str(e) + additional_err_msg) from e
    return repo.head.commit == upstream.refs.main.commit


def create(out_dir, create_cc_rc=True, **kwargs):
    """
    Create the research project structure based on the `research-project` template.

    :param out_dir: Path to the output directory.
    :type out_dir: str or pathlib.Path
    :param bool create_cc_rc: Whether to create the `.cookiecutterrc` file.
    :param dict kwargs: Keyword arguments passed to `cookiecutter`.
    """
    # Create cookiecutterrc file (if not existing)
    if create_cc_rc:
        create_cookiecutterrc()

    # Create project
    print(f"\033[34m\nStart creating research project structure in {out_dir} ...\n\033[0m")
    template = Path(path_to.templates.local.research_project).expanduser()
    if not template.exists():
        template = path_to.templates.remote.research_project
    else:
        # Check whether the template is up to date
        print(f"Checking whether '{template.name}' template is up-to-date ...")
        if not is_git_repo_up_to_date(path=template):  # run git fetch
            answer = input(
                f"\033[33m\nYour local version of the '{template.name}' template is not up-to-date.\n"
                f"Do you want to update it now [y/n]: \033[0m"
            )
            if "y" in answer.lower():
                # Run git pull
                _ = Repo(template).remotes.origin.pull()
                print(f"\033[32m\nUpdated local version of the '{template.name}' template.\n\033[0m")
            else:
                print(f"\033[33m\nUsing local version of the '{template.name}' template.\n\033[0m")
        else:
            print(f"Your local version of the '{template.name}' template seems to be up-to-date.\n")

    # Run cookiecutter on template
    print("\033[4m\033[34m\nProvide information about your research project:\n\033[0m")
    cookiecutter(template=str(template), overwrite_if_exists=False, output_dir=str(out_dir), **kwargs)


# o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
