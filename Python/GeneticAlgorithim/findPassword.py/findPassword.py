import random
import datetime


def get_fitness(guess):
    tempfit = 0
    for expected, actual in zip(target, guess):
        if (expected == actual):
            tempfit = tempfit + 1
    return tempfit



    # return sum(1 for expected, actual in zip(target, guess)
    #            if expected == actual)


def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))


def generate_parent(length):
    return ''.join(random.sample(geneSet, length))
    # print(random.sample(geneSet, length))
    # genes = []
    # while len(genes) < length:
    #     sampleSize = min(length - len(genes), len(geneSet))
    #     genes.extend(random.sample(geneSet, sampleSize))
    # return ''.join(genes)


def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    if childGenes[index] != alternate:
        childGenes[index] = alternate
    elif newGene != childGenes[index]:
        childGenes[index] = newGene
    return ''.join(childGenes)


   
    # childGenes[index] = alternate \
    #     if newGene == childGenes[index] \
    #     else newGene
    


random.seed()
geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello World!"
startTime = datetime.datetime.now()
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)
while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)

    if bestFitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child
