from graph_coloring.problem import GraphColoring
from graph_coloring.selections import tournament
from graph_coloring.crossovers import one_point
from graph_coloring.mutations import n_bit_flip
import random


class Individual:
    """default individual class"""

    def __init__(self, genome):
        self.genome = genome
        self.fitness = None


random.seed(318)

gcp = GraphColoring(n_node=9, n_edge=23)
evaluate = lambda coloring: 1-gcp.violent(coloring)/gcp.n_edge

COLORS = gcp.colors
NDIM = gcp.n_node
NPOP = 100
NGEN = 1000

NELITE = 2
TOURNA_SIZE = 3
CXPB = 0.5
MUTPB = 0.5
NBIT = 3

best_individual_in_history = None

# initialize a population
population = []
for _ in range(NPOP):
    genome = random.choices(COLORS, k=NDIM)
    population.append(Individual(genome))

for current_generation in range(NGEN-1):

    # evaluate the fitnesses of individuals
    for individual in population:
        individual.fitness = evaluate(individual.genome)

    # get best individual in the population
    best_individual = max(population, key=lambda individual: individual.fitness)

    if best_individual_in_history:
        if best_individual.fitness > best_individual_in_history.fitness:
            best_individual_in_history = best_individual
    else:
        best_individual_in_history = best_individual
    print(best_individual_in_history.fitness)

    if best_individual_in_history.fitness == 1:
        break

    # selection
    parents = [best_individual] * NELITE
    parents.extend(
        [tournament(population, t=TOURNA_SIZE) for _ in range(NPOP-NELITE)]
    )
    random.shuffle(parents)
    genomes = [parent.genome for parent in parents]

    # crossover
    for genome1, genome2 in zip(genomes[::2], genomes[1::2]):
        if random.random() < CXPB:
            one_point(genome1, genome2)

    # mutation
    for genome in genomes:
        if random.random() < MUTPB:
            n_bit_flip(genome, n_bit=NBIT, colors=COLORS)

    population = [Individual(genome) for genome in genomes]

# print results
print("=============================RESULTS=============================")
print("EGDES OF GRAPH")
[print(f"{i}-{j}") for i,j in gcp.edges]
print("coloring:", best_individual_in_history.genome)
print("fitness:", best_individual_in_history.fitness)
