from tsimulus.generator import generate_ts
from matplotlib import pyplot as plt


dfs = generate_ts()

for df in dfs:
    df = df.set_index("date")
    df.plot()

plt.show()
