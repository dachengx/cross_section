import os
import pkg_resources
from warnings import warn

import numpy as np
from scipy.interpolate import interp1d


def interp1d_positive(x0, y0):
    inter = interp1d(x0, y0, bounds_error=False, fill_value="extrapolate")
    return lambda x: np.clip(inter(x), 0, np.inf)


def _package_path(sub_directory):
    """Get the abs path of the requested sub folder."""
    return pkg_resources.resource_filename("xsectron", f"{sub_directory}")


def _get_abspath(file_name):
    """Get the abspath of the file.

    Raise FileNotFoundError when not found in any subfolder

    """
    for sub_dir in ("data", "configs"):
        p = os.path.join(_package_path(sub_dir), file_name)
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f"Cannot find {file_name}")


def get_file_path(fname):
    """Find the full path to the resource file
    Try 5 methods in the following order
    1. fname begin with '/', return absolute path
    2. can get file from _get_abspath, return appletree internal file path
    """
    if not fname:
        warn(f"A file has value False, assuming this is intentional.")
        return

    # 1. From absolute path
    # Usually Config.default is a absolute path
    if fname.startswith("/"):
        return fname

    # 2. From xsectron internal files
    try:
        return _get_abspath(fname)
    except (FileNotFoundError, ValueError, NameError, AttributeError):
        warn(f"Can not find {fname}!")
