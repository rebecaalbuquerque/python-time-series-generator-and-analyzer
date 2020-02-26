import random


def plot_vertically(plt, plots, titles):
    colors = ["b", "g", "r", "c", "m", "y", "k"]

    for i, p in enumerate(plots, 1):
        plt.subplot(len(plots), 1, i)
        p.plot(style=f"{colors[random.randint(0, len(colors)-1)]}:")
        plt.title(titles[i-1])

    plt.subplots_adjust(hspace=0.5)
