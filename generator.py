from rpy2.rinterface import RRuntimeError
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
import rpy2.robjects.packages as r
import re

utils = r.importr("utils")


def import_r_package(package_name, devtools_package=None):

    try:
        if devtools_package is None:
            r_package = importr(package_name)
        else:
            r_package = importr(re.findall("/(.+)", package_name)[0])

    except RRuntimeError:

        if devtools_package is None:
            utils.install_packages(package_name)
        else:
            devtools_package.install_github(package_name)
            package_name = re.findall("/(.+)", package_name)[0]

        r_package = importr(package_name)

    return r_package


devtools = import_r_package("devtools")
import_r_package("ykang/gratis", devtools)

ro.r('write.csv(generate_msts(seasonal.periods = c(7, 365), n = 108, nComp = 2), "output/ts.csv")')
