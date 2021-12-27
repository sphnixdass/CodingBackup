import random
import datetime

class Chromosome:
    Genes = None
    Fitness = None
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness


def get_fitness(guess, target):
    tempfit = 0
    for expected, actual in zip(target, guess):
        if (expected == actual):
            tempfit = tempfit + 1
    return tempfit


def display(genes, target, startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(genes, target)
    print("{0}\t{1}\t{2}".format(genes, fitness, str(timeDiff)))


def _generate_parent(length, geneSet):
    return ''.join(random.sample(geneSet, length))



def _mutate(parent, geneSet, get_fitness):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    if childGenes[index] != alternate:
        childGenes[index] = alternate
    elif newGene != childGenes[index]:
        childGenes[index] = newGene
    return ''.join(childGenes)


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    random.seed()
    bestParent = _generate_parent(targetLen, geneSet)
    bestFitness = get_fitness(bestParent)
    display(bestParent)
    if bestFitness >= optimalFitness:
        return bestParent
    while True:
        child = _mutate(bestParent, geneSet, get_fitness)
        childFitness = get_fitness(child)
        if bestFitness >= childFitness:
            continue
        display(child)
        if childFitness >= optimalFitness:
            return child
        bestFitness = childFitness
        bestParent = child


