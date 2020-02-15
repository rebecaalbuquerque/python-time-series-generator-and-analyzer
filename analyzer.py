import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("output\\ts.csv")
df.drop(["id"], axis=1, inplace=True)
df.index = pd.date_range("01/01/2010", freq="MS", periods=len(df.y))

df.plot()
plt.show()