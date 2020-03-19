import random


def pop(popSize):
	population = []
	i = 0
	while i < popSize:
		individual = []
		for j in range(0,75):
			individual.append(random.randint(0,1))
		if individual not in population:	
			population.append(individual)
			i += 1				
	return population
