"""
Create project module for scilaunch.

Author:  Simon M. Hofmann
Contact: simon.[lastname][at]pm.me
Years:   2023
"""

# %% Import
import json
from pathlib import Path

from cookiecutter.main import cookiecutter
from git import Repo
from git.exc import GitCommandError

from scilaunch.configs import path_to

# %% Set global vars & paths  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

COOKIECUTTERRC = Path.home() / ".cookiecutterrc"  # destination for cookiecutterrc file


# %% Functions  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o


def create_cookiecutterrc(**kwargs):
    """Create the .cookiecutterrc file."""
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
        print(f"\nUsing existing {COOKIECUTTERRC} to fill defaults.\n")


def is_git_repo_up_to_date(path):
    """Check whether the local git repository is up-to-date."""
    repo = Repo(path)
    upstream = repo.remotes.origin
    try:
        upstream.fetch(kill_after_timeout=10)  # run git fetch to update the remote-tracking branches
    except GitCommandError as e:
        additionaL_err_msg = (
            "\033[31mUnable to fetch data from remote repository! Check your internet connection!\033[0m"
        )
        raise GitCommandError(str(e) + additionaL_err_msg) from e
    return repo.head.commit == upstream.refs.main.commit


def create(out_dir, create_cc_rc=True, **kwargs):
    """Create the research project structure."""
    # Create cookiecutterrc file (if not existing)
    if create_cc_rc:
        create_cookiecutterrc()

    # Create project
    print(f"\033[34m\nStart creating research project structure in {out_dir} ...\n\033[0m")
    template = Path(path_to.templates.local.research_project).expanduser()
    if not template.exists():
        template = path_to.templates.remote.research_project
    else:
        # Check whether template is up-to-date
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


# %% __main__ o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

if __name__ == "__main__":
    # Run main
    pass

#  o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
