import random


def pop(popSize):
	population = []
	for i in range(0,popSize):
		individual = []
		for j in range(0,75):
			individual.append(random.randint(0,1))
		population.append(individual)
	return population
