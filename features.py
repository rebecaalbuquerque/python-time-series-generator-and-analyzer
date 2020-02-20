from enum import Enum


class _ACFFeatures(Enum):
    x_acf1 = "x_acf1"
    diff1_acf1 = "diff1_acf1"
    diff2_acf1 = "diff2_acf1"
    x_acf10 = "x_acf10"
    diff1_acf10 = "diff1_acf10"
    diff2_acf10 = "diff2_acf10"
    seas_acf1 = "seas_acf1"

    @staticmethod
    def get_name():
        return "acf_features"


class _PACFFeatures(Enum):
    x_pacf5 = "x_pacf5"
    diff1x_pacf5 = "diff1x_pacf5"
    diff2x_pacf5 = "diff2x_pacf5"
    seas_pacf = "seas_pacf"

    @staticmethod
    def get_name():
        return "pacf_features"


class _STLFeatures(Enum):
    trend = "trend"
    spike = "spike"
    linearity = "linearity"
    curvature = "curvature"
    e_acf1 = "e_acf1"
    e_acf10 = "e_acf10"

    @staticmethod
    def get_name():
        return "stl_features"


class _MaxLevelShiftFeatures(Enum):
    time_level_shift = "time_level_shift"
    max_level_shift = "max_level_shift"

    @staticmethod
    def get_name():
        return "max_level_shift"


class _HeterogeneityFeatures(Enum):
    arch_acf = "arch_acf"
    garch_acf = "garch_acf"
    arch_r2 = "arch_r2"
    garch_r2 = "garch_r2"

    @staticmethod
    def get_name():
        return "heterogeneity"


class Function(Enum):
    acf_features = _ACFFeatures
    pacf_features = _PACFFeatures
    stl_features = _STLFeatures
    heterogeneity = _HeterogeneityFeatures
    max_level_shift = _MaxLevelShiftFeatures
    entropy = "entropy"
    nonlinearity = "nonlinearity"
    hurst = "hurst"
    stability = "stability"
    lumpiness = "lumpiness"
    unitroot_kpss = "unitroot_kpss"
    unitroot_pp = "unitroot_pp"
    time_kl_shift = "time_kl_shift"
    time_var_shift = "time_var_shift"
    max_kl_shift = "max_kl_shift"
    max_var_shift = "max_var_shift"
