import random


def plot_vertically(plt, plots, titles=None, style=None):
    colors = ["b", "g", "r", "c", "m", "y", "k"]

    for i, p in enumerate(plots, 1):
        plt.subplot(len(plots), 1, i)

        if style is None:
            style = ""

        p.plot(style=f"{colors[random.randint(0, len(colors) - 1)]}{style}")

        if titles is not None:
            plt.title(titles[i - 1])

    plt.subplots_adjust(hspace=0.5)
