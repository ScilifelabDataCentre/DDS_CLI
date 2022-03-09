"""Directory module. Creates the DDS directory during delivery."""

###############################################################################
# IMPORTS ########################################################### IMPORTS #
###############################################################################

# Standard library
import errno
import logging
import pathlib
import sys

# Installed

# Own modules

###############################################################################
# START LOGGING CONFIG ################################# START LOGGING CONFIG #
###############################################################################

LOG = logging.getLogger(__name__)

###############################################################################
# CLASSES ########################################################### CLASSES #
###############################################################################


class DDSDirectory:
    """Data Delivery System directory class."""

    def __init__(self, path=pathlib.Path, add_file_dir: bool = True):

        dirs = {
            "ROOT": path,
            "META": path / pathlib.Path("meta/"),
            "LOGS": path / pathlib.Path("logs/"),
        }

        if add_file_dir:
            dirs["FILES"] = path / pathlib.Path("files/")

        for dir in dirs.values():
            try:
                dir.mkdir(parents=True, exist_ok=False)
            except OSError as e:
                if e.errno == errno.EEXIST:
                    sys.exit(
                        f"Directory '{dir}' already exists. Please specify a path where a new folder can be created."
                    )
                else:
                    sys.exit(f"The temporary directory '{dir}' could not be created: {e}")

        self.directories = dirs
