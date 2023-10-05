"""
Main module for scilaunch.

Author:  Simon M. Hofmann
Contact: simon.[lastname][at]pm.me
Years:   2023
"""

# %% Import
import argparse
import sys
from pathlib import Path

from scilaunch.project import create

# %% Set global vars & paths  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o
pass


# %% Functions  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o


def main():
    """Run main function of scilaunch."""
    # Parse arguments
    parser = argparse.ArgumentParser(description="Create a research project structure.")
    parser.add_argument("out", type=str, nargs="?", help="Target parent / output directory", default=Path.cwd())
    parser.add_argument("-o", "--out_dir", type=str, help="Target parent / output directory")

    # Extract arguments with flags
    FLAGS, _ = parser.parse_known_args()

    # We use this to allow for both positional and flag arguments (since we just have this one argument)
    if FLAGS.out_dir:
        FLAGS.out = FLAGS.out_dir

    # Create a directory structure for a research project
    create(out_dir=FLAGS.out)

    return 0


# %% __main__ o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

if __name__ == "__main__":
    # Run main
    sys.exit(main())

#  o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
