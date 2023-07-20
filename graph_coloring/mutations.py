import random


def one_bit_flip(coloring, colors):
    """One-bit Flip Mutation"""
    index = random.randrange(len(coloring))
    color = random.choice(colors)
    while color == coloring[index]:
        color = random.choice(colors)
    coloring[index] = color
    return coloring


def n_bit_flip(coloring, n_bit, colors):
    """n-bit Flip Mutation"""
    indexes = []
    while len(indexes) < n_bit:
        index = random.randrange(len(coloring))
        if index not in indexes:
            indexes.append(index)
            color = random.choice(colors)
            while color == coloring[index]:
                color = random.choice(colors)
            coloring[index] = color
    return coloring
