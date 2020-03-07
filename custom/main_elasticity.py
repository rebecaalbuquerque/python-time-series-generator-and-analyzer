from custom.generator import generate_elasticity_ts
from matplotlib import pyplot as plt

generate_elasticity_ts(size=100, dependency_min=5, dependency_max=10).plot()
plt.show()
plt.close()
