import random


def one_point(coloring1, coloring2):
    """One-point Crossover"""
    crossover_point = random.randrange(len(coloring1))
    coloring1[crossover_point:], coloring2[crossover_point:] =\
        coloring2[crossover_point:], coloring1[crossover_point:]
    return coloring1, coloring2


def uniform(coloring1, coloring2, r=0.5):
    """Uniform Crossover"""
    for i in range(len(coloring1)):
        if random.random() < r:
            coloring1[i], coloring2[i] = coloring2[i], coloring1[i]
    return coloring1, coloring2
