import random


def tournament(population, t=3, key=lambda individual: individual.fitness):
    indexes = list(range(len(population)))
    random.shuffle(indexes)
    indexes = indexes[:t]
    tournament_pool = [population[i] for i in indexes]
    return max(tournament_pool, key=key)
