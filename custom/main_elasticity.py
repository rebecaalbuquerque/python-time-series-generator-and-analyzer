from custom.generator import generate_elasticity_ts
from matplotlib import pyplot as plt

from custom.utils import plot_vertically

resulting, dependency, output = generate_elasticity_ts(
    size=100,
    dependency_min=10,
    dependency_max=20,
    resulting_min=20,
    resulting_max=200
)

plot_vertically(
    plt,
    [resulting, dependency, output],
    ["Resultante (Venda)", "Mandante (Preço)", "Resultante e Mandante"]
)

plt.show()

plt.close()
