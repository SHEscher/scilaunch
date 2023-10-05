"""
Configuration for scilaunch.

Author: Simon M. Hofmann | <simon.[lastname][at]pm.me> | 2023
"""

# %% Imports
from pathlib import Path

from box import Box

# %% Config class & functions & objects < o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

_paths_json = {
    "templates": {
        "local": {
            "research_project": "~/.cookiecutters/research-project",
            "cookiecutterrc": f"{Path(__file__).parent}/templates/cookiecutterrc",
        },
        "remote": {"research_project": "https://github.com/SHEscher/research-project.git"},
    }
}

path_to = Box(_paths_json)

#  o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
