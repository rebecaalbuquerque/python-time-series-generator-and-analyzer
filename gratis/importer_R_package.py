from rpy2.rinterface import RRuntimeError
from rpy2.robjects.packages import importr
import re


def import_r_package(utils_r, package_name, devtools_package=None):
    try:
        if devtools_package is None:
            r_package = importr(package_name)
        else:
            r_package = importr(re.findall("/(.+)", package_name)[0])

    except RRuntimeError:

        if devtools_package is None:
            utils_r.install_packages(package_name)
        else:
            devtools_package.install_github(package_name)
            package_name = re.findall("/(.+)", package_name)[0]

        r_package = importr(package_name)

    return r_package