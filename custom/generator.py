import math
import random
from enum import Enum
import numpy as np
import pandas as pd
import datetime


# De quanto em quanto tempo o padrão da série temporal se repete
class Seasonality(Enum):
    year = "year"
    quarter_of_year = "quarter_of_year"
    monthly = "monthly"
    weekly = "weekly"


def generate_seasonal_ts(seasonality, size):

    def difference(dataset, interval=1):
        diff = list()
        for i in range(interval, len(dataset)):
            value = dataset[i] - dataset[i - interval]
            diff.append(value)
        return diff

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

    # ======================================== NOISE ======================================== #
    # 0: mean of the normal distribution, 1: standard deviation of the normal distribution, 2: number of elements
    noise = np.random.normal(0, maximum_peak / 10, size)
    noise = difference(noise)
    noise.append(noise[len(noise)-1])

    # ===================================== SIN + NOISE ===================================== #
    sine_noise = []

    # Percorre o array de ruído
    for i in range(0, len(noise)):

        if sine[i] == max(sine):

            if noise[i] > 0:
                # Se o ruído atual é maior do que zero, soma o ruído e o valor do pico
                sine_noise.append(noise[i] + sine[i])
            else:
                # Caso contrário, faz ele ficar positivo e então soma o ruído e o valor do pico
                sine_noise.append((-1 * noise[i]) + sine[i])

        else:
            sine_noise.append(noise[i])

    return pd.Series(sine, dates), pd.Series(noise, dates), pd.Series(sine_noise, dates)
