import rpy2.robjects.packages as r
from matplotlib import pyplot as plt

from features import Function
from generator import *
from importer_R_package import import_r_package

utils = r.importr("utils")
devtools = import_r_package(utils, "devtools")
import_r_package(utils, "doParallel")
import_r_package(utils, "tsfeatures")
import_r_package(utils, "ykang/gratis", devtools)

# ====================================================================== #
#    Frequency = número de repetições antes do padrão sazonal se repetir #
#        1 (annual), 4 (quarterly), 12 (monthly), 52 (weekly)            #
# ====================================================================== #

# df = generate_diverse_ts(q=1, frequency=12, components=2, size=108)
# df = generate_multi_seasonal_ts(seasonal_periods=[7, 365], size=800, components=2)
df = generate_ts_with_controllable_features(
    q=1,
    size=60,
    frequency=1,
    seasonal=0,
    features=[Function.time_level_shift, Function.max_var_shift, Function.heterogeneity.value.arch_acf,
              Function.heterogeneity.value.garch_r2, Function.heterogeneity.value.arch_r2],
    target=[20, 3, 0.3, 0.5, 0.5]
)

df.data.plot()
plt.show()
