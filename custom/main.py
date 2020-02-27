import math
import random
from enum import Enum
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime

from custom.utils import plot_vertically


# De quanto em quanto tempo o padrão da série temporal se repete
class Seasonality(Enum):
    year = "year"
    quarter_of_year = "quarter_of_year"
    monthly = "monthly"
    weekly = "weekly"


def generate_seasonal_ts(seasonality, size):
    if seasonality == Seasonality.year:
        return _ts_with_yearly_seasonality(12, size)
    elif seasonality == Seasonality.monthly:
        return pd.Series(), pd.Series(), pd.Series()
    else:
        return _ts_with_yearly_seasonality(52, size)


def _ts_with_yearly_seasonality(lag, size):
    start_year = f"{datetime.datetime.today().year - math.floor(size / lag)}-01-01"
    maximum_peak = random.randint(200, 500)
    dates = pd.date_range(start_year, periods=size, freq='MS')

    # ========================================= SIN ========================================= #
    sin = []

    for j in np.arange(size):
        sin.append(maximum_peak * math.sin(j * 3 * math.pi / lag))

    # ======================================== NOISE ======================================== #
    # 0: mean of the normal distribution, 1: standard deviation of the normal distribution, 2: number of elements
    noise = np.random.normal(0, maximum_peak / 3, size)

    # ===================================== SIN + NOISE ===================================== #
    sin_noise = []

    # Percorre o array de ruído
    for i in range(0, len(noise)):

        if i in range(0, len(noise), lag):
            # ====================== ADICIONANDO PICOS NO ARRAY DE RUÍDOS ====================== #
            # Se o index do ruído atual corresponde com uma nova sazonalidade

            if noise[i] > 0:
                # Se o ruído atual é maior do que zero, soma o ruído e o valor do pico (acrescido 50%)
                noise[i] = noise[i] + (maximum_peak * 1.5)
            else:
                # Caso contrário, faz ele ficar positivo e então soma o ruído e o valor do pico (acrescido 50%)
                noise[i] = (-1 * noise[i]) + (maximum_peak * 1.5)

            # ==================== GERANDO ARRAY RESULTANTE (RUÍDO + SENO) ==================== #
            sin_noise.append(noise[i] + maximum_peak)

        else:
            # Se não corresponde com uma nova sazonalidade então
            sin_noise.append((sin[i] * 0.3) + noise[i])

    return pd.Series(sin, dates), pd.Series(noise, dates), pd.Series(sin_noise, dates)


def _ts_with_weekly_seasonality(lag, size):
    start_year = f"{datetime.datetime.today().year - math.floor(size / lag)}-01-01"
    maximum_peak = random.randint(200, 500)
    dates = pd.date_range(start_year, periods=size, freq='W')

    # ========================================= SIN ========================================= #
    sin = []

    for j in np.arange(size):
        sin.append(maximum_peak * math.sin(j * 2 * math.pi / 7))

    # ======================================== NOISE ======================================== #
    # 0: mean of the normal distribution, 1: standard deviation of the normal distribution, 2: number of elements
    noise = np.random.normal(0, maximum_peak / 3, size)
    sin_noise = []

    # ===================================== SIN + NOISE ===================================== #
    # Percorre o array de ruído
    for i in range(0, len(noise)):

        if i in range(0, len(noise), lag):
            # ====================== ADICIONANDO PICOS NO ARRAY DE RUÍDOS ====================== #
            # Se o index do ruído atual corresponde com uma nova sazonalidade
            print(i)
            if noise[i] > 0:
                # Se o ruído atual é maior do que zero, soma o ruído e o valor do pico (acrescido 50%)
                noise[i] = noise[i] + (maximum_peak * 1.5)
            else:
                # Caso contrário, faz ele ficar positivo e então soma o ruído e o valor do pico (acrescido 50%)
                noise[i] = (-1 * noise[i]) + (maximum_peak * 1.5)

            # ==================== GERANDO ARRAY RESULTANTE (RUÍDO + SENO) ==================== #
            sin_noise.append(noise[i] + maximum_peak)

        else:
            # Se não corresponde com uma nova sazonalidade então
            sin_noise.append((sin[i] * 0.3) + noise[i])

    return pd.Series(sin, dates), pd.Series(noise, dates), pd.Series(sin_noise, dates)


def _ts_with_daily_seasonality(size):
    pass


series_sin, series_noise, series_sin_noise = generate_seasonal_ts(seasonality=Seasonality.weekly,
                                                                  size=84)

plot_vertically(plt, [series_sin, series_noise, series_sin_noise], ["Sin", "Noise", "Sin + Noise"])
plt.show()

series_sin_noise.plot()
plt.show()
