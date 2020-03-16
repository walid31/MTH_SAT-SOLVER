from population import pop
from insertionSort import insertionSort
import pickle
import random

# load the binary file of satisfied files in a list 
with open('../datastructure/satisfied.pickle', 'rb') as f:
    satisfied = pickle.load(f)

# This function give the average of a list
def Average(lst): 
	somme = 0
	cpt = 0
	for item in lst:
		somme += item[0]
		cpt += 1

	return somme / cpt


# This function returns the fitness of an instance
def fitness(instance,individ):
	temp_fit=0
	for clause in satisfied[instance]:
		for lit in clause :		
			if int(lit)>0:
				if individ[int(lit)-1] == 1 :
					temp_fit+=1
					break
			else:
				if individ[(-1)*int(lit)-1] == 0 :
					temp_fit+=1
					break
	return temp_fit		

# This function creates a new child from two parents
def Individual(parent1,parent2):
	subParent1 = parent1[0:int(len(parent1)/2)]
	subParent2 = parent2[int(len(parent2)/2):len(parent2)]
	child = subParent1 + subParent2
	return child

# Crossover generation function
def CrossGen():
	cr_max = popSize * crossoverRate / 100 
	newBorn = []
	for crossCount in range(0,int(cr_max)):
		# gets two parents from population randomly
		parent1 = random.choice(population)
		parent2 = random.choice(population)

		# creates two new children
		child1 = Individual(parent1,parent2)
		child2 = Individual(parent2,parent1)

		newBorn.append(child1)
		newBorn.append(child2)
	return newBorn

# Mutation generation function
def MutateGen(population):
	mt_max = popSize * mutationRate / 100
	for mutationCount in range(0,int(mt_max)):
		individ = random.choice(population)
		randLit = random.randint(0,74)
		
		# let's mutate the literal
		if individ[1][randLit] == 0:
			individ[1][randLit] = 1
		else:
			individ[1][randLit] = 0
		
	return population

# This function returns a list of population with it's fitness 
def popFitness(instance,popul):
	listFit = []
	for individ in popul:	
		fit = fitness(instance,individ)	
		listFit.append([fit,individ])	
	return listFit

# This function merge new borns generation to the global population
def merge(newBorn,population):

	population = newBorn + population
	# Insertion sort of the new born individuals from the crossover
	insertionSort(population)
	# Eliminate the individuals with lower score
	population = population[len(newBorn):len(population)]

	return population

maxIter = 500
popSize = 100
crossoverRate = 25
mutationRate = 20

# Choose a dataset randomly
instance = key = random.choice(list(satisfied.items())) 

# Generate a population
population =  pop(popSize)

# Associates for each individual it's fitness in the population list
population = popFitness(instance[0],population)
mean1 = Average(population)
print(mean1)
# generates a new generation with crossover and calculates it's fitness
newBorn = CrossGen()
population = merge(newBorn,population)
mean2 = Average(population)

# Mutate an andividual randomly
population = MutateGen(population)

print(len(population))
print(mean2-mean1)