import pandas as pd
import rpy2.robjects.packages as r
from matplotlib import pyplot as plt

from generator import generate_multi_seasonal_ts, generate_ts_with_controllable_features, generate_diverse_ts
from importer_R_package import import_r_package

utils = r.importr("utils")
devtools = import_r_package(utils, "devtools")
import_r_package(utils, "doParallel")
import_r_package(utils, "ykang/gratis", devtools)

# ====================================================================== #
#    Frequency = número de repetições antes do padrão sazonal se repetir
#        1 (annual), 4 (quarterly), 12 (monthly), 52 (weekly)            #
# ====================================================================== #

generate_diverse_ts(q=1, frequency=12, components=2, size=60)
# generate_multi_seasonal_ts(seasonal_periods=[4, 12], size=108, components=2)
#                                        selected_features=[ "trend"], target=[0.9])
# generate_ts_with_controllable_features(q=1, size=108, frequency=12, seasonal=0, features=["entropy", "stl_features"],
#                                        selected_features=[ "trend"], target=[0.9])
df = pd.read_csv("output\\diverse-ts.csv", sep=";")
df.index = pd.date_range("01/01/2010", freq="MS", periods=len(df.data1))

df.plot()
plt.show()
