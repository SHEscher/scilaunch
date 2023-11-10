"""
Configuration file for `scilaunch`.

Relevant paths and links are stored in the form of a json file, which is loaded into a `box.Box` object.

```python
_paths_json = {
    "templates": {
        "local": {
            "research_project": "~/.cookiecutters/research-project",
            "cookiecutterrc": f"{Path(__file__).parent}/templates/cookiecutterrc",
        },
        "remote": {"research_project": "https://github.com/SHEscher/research-project.git"},
    }
}
```
"""

# %% Imports
from pathlib import Path

from box import Box

# %% Config class & functions & objects  o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

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

# o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
