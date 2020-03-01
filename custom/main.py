from matplotlib import pyplot as plt
import statsmodels.api as sm

from custom.generator import *
from custom.utils import plot_vertically


series_sine, series_noise, series_sine_noise = generate_seasonal_ts(seasonality=Seasonality.year, size=108)
# series_sine, series_noise, series_sine_noise = generate_seasonal_ts(seasonality=Seasonality.weekly, size=365)

res = sm.tsa.seasonal_decompose(series_sine_noise.interpolate(), period=12, model='additive')
res.plot()
plt.show()

plot_vertically(plt, [series_sine, series_noise, series_sine_noise], ["Sine", "Noise", "Sine + Noise"])
plt.show()

series_sine_noise.plot()
plt.show()
