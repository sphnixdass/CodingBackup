import datetime
import genetic

def test_Hello_World():
    target = "For I am fearfully and wonderfully made."
    guess_password(target)

def guess_password(target):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()
    def fnGetFitness(genes):
        return genetic.get_fitness(genes, target)
    def fnDisplay(genes):
        genetic.display(genes, target, startTime)
    optimalFitness = len(target)
    genetic.get_best(fnGetFitness, len(target), optimalFitness, geneset, fnDisplay)


if __name__ == '__main__':
    test_Hello_World()