import math
import random
from enum import Enum
import numpy as np
import pandas as pd
import datetime
from scipy.stats import truncnorm


# De quanto em quanto tempo o padrão da série temporal se repete
class Seasonality(Enum):
    year = "year"
    quarter_of_year = "quarter_of_year"
    monthly = "monthly"
    weekly = "weekly"


def _get_truncated_normal(mean=0, standard_deviation=1, floor=0, ceil=10, n=1):
    return truncnorm((floor - mean) / standard_deviation, (ceil - mean) / standard_deviation, loc=mean,
                     scale=standard_deviation).rvs(n).tolist()


def generate_seasonal_ts(seasonality, size):
    if seasonality == Seasonality.year:
        lag = 12
        start_year = f"{datetime.datetime.today().year - math.floor(size / lag)}-01-01"
        dates = pd.date_range(start_year, periods=size, freq='MS')

    elif seasonality == Seasonality.monthly:
        return pd.Series(), pd.Series(), pd.Series()

    else:
        lag = 7
        start_year = f"{datetime.datetime.today().year - math.floor(size / lag)}-01-01"
        dates = pd.date_range(start_year, periods=size, freq='D')

    maximum_peak = random.randint(200, 500)

    # ========================================= SIN ========================================= #
    sine = []

    for j in np.arange(size):
        sine.append(maximum_peak * np.sin(j * 2 * math.pi / lag))

    sine = [x + (min(sine) * -1) for x in sine]

    # ======================================== NOISE ======================================== #
    # 0: mean of the normal distribution, 1: standard deviation of the normal distribution, 2: number of elements
    max_noise = maximum_peak * 0.7
    noise = _get_truncated_normal(mean=int(max_noise / 2), standard_deviation=int(max_noise / 2), floor=0,
                                  ceil=max_noise, n=size)

    # ===================================== SIN + NOISE ===================================== #
    sine_noise = []

    # Percorre o array de ruído
    for i in range(0, len(noise)):

        if format(sine[i], ".2f") == format(max(sine), ".2f"):
            sine_noise.append(noise[i] + (sine[i] * 0.8))

        else:
            sine_noise.append(noise[i])

    return pd.Series(sine, dates), pd.Series(noise, dates), pd.Series(sine_noise, dates)


def generate_elasticity_ts(size, dependency_min, dependency_max, resulting_min, resulting_max,
                           inversely_proportional_constant):

    def _getVariation():
        # Decidir se vai variar pra mais ou menos
        if bool(random.getrandbits(1)):
            # Varia pra mais. Variação mínima = variacao,  Variação máxima = dependencia_max
            var_percentage = float(f"1.{random.randint(1, 9)}") * 1
            var_value = random.randint(variation, dependency_max)
        else:
            # Varia pra mais. Variação mínima = dependencia_min,  Variação máxima = variacao
            var_percentage = float(f"0.{random.randint(1, 9)}") * (-1)
            var_value = random.randint(dependency_min, variation)

        return var_percentage, var_value

    variation = random.randint(dependency_min, dependency_max)
    list_variant = size * [variation]

    # =============== GERAÇÃO TS RESULTANTE =============== #
    list_resulting = _get_truncated_normal(mean=int(resulting_max / 2), standard_deviation=int(resulting_max / 2),
                                           floor=resulting_min, ceil=resulting_max, n=size)

    # ================ GERAÇÃO TS MANDANTE ================ #
    variation_time = random.randint(0, int(size))
    variation_percentage, variation_value = _getVariation()

    for i in range(size):
        variation_range = range(i, i + variation_time)

        for j in variation_range:

            if i + variation_range.stop < size:

                if j == variation_time:
                    variation_time = random.randint(j, int(size))
                    variation_percentage, variation_value = _getVariation()
                else:
                    list_variant[j] = list_variant[j] + (variation_value * variation_percentage)

    for j in range(size):
        # Aplicando a fórmula de inversão proporcional y = C/x
        y = (inversely_proportional_constant / list_variant[j])
        list_resulting[j] = round(random.uniform(y*0.95, y*1.05), 2)
        # list_resulting[j] = y

    ts_resulting = pd.Series(list_resulting)
    ts_variant = pd.Series(list_variant)

    df = pd.concat([ts_resulting, ts_variant], axis=1).reset_index()
    df.columns = ["index", "resulting", "variant"]
    df = df.drop(["index"], axis=1)
    df.to_csv("result.csv", sep=";", index=False)

    for coluna in df.columns:
        df[coluna] = df[coluna] / (max(df[coluna]))

    return ts_resulting, ts_variant, [df.resulting, df.variant]
