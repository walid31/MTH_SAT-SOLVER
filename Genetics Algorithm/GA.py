from population import pop
from insertionSort import insertionSort
import pickle
from statistics import stdev
from statistics import mean
from fractions import Fraction as fr
import random

# load the binary file of satisfied files in a list 
with open('../datastructure/satisfied.pickle', 'rb') as f:
    satisfied = pickle.load(f)

# This function give the average of a list
def Average(lst): 
	somme = 0.0
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
	subParent1 = parent1[0:int(len(parent1)/ 2)]
	subParent2 = parent2[int(len(parent2) /2):len(parent2)]
	child = subParent1 + subParent2
	return child

# Crossover generation function
def CrossGen(population, crossoverRate, instance):
	cr_max = popSize * crossoverRate / 100 
	if cr_max % 2 != 0:
		cr_max += 1
	parents = random.sample(population, int(cr_max))
	newBorn = []
	i = 0
	while i < cr_max:
		# creates two new children
		if parents[i] != parents[i+1]:
			child1 = Individual(parents[i],parents[i+1])
			if child1 not in newBorn:
				newBorn.append(child1)
		else: 
			print("true")
			print(parents[i])
			print(parents[i+1])
		i += 2	
	
	# mean = Average(newBorn)
	print(len(newBorn))
	return newBorn

# Mutation generation function
def MutateGen(population):
	mt_max = popSize * mutationRate / 100
	newBorn = []
	for mutationCount in range(0,int(mt_max)):
		individ = random.choice(population)
		randLit = random.randint(0,74)
		
		# let's mutate the literal
		if individ[1][randLit] == 0:
			individ[1][randLit] = 1
			newBorn.append(individ)
		else:
			individ[1][randLit] = 0
			newBorn.append(individ)
	return newBorn

# This function returns a list of population with it's fitness 
def popFitness(instance,popul):
	listFit = []
	for individ in popul:	
		fit = fitness(instance,individ)	
		listFit.append([fit,individ])	
	return listFit

# This function merge new borns generation to the global population
def merge(newBorn,population):
	newBornLen = 0
	for child in newBorn:
		if child not in population:
			population.append(child)
			newBornLen += 1
	# Insertion sort of the new born individuals from the crossover
	insertionSort(population)
	# Eliminate the individuals with lower score
	population = population[newBornLen:len(population)]
	return population

# This function udpates 50% of the population
def socialDisaster(lst,instance,popSize):
	disasterList = pop(int(popSize/2))
	disasterList = popFitness(instance,disasterList)
	print(disasterList)
	lst[0:int(len(lst)/2)] = disasterList
	insertionSort(lst)
	return diversification(lst,instance, popSize)	

# If we observe a stagnation we will update 50% of the population
def diversification(lst,instance,popSize):
	fit = [item[0] for item in lst]

	# calculates the standards deviation
	stagnIndicator = stdev(fit)
	print(stagnIndicator)
	# diversification if stagnation
	if stagnIndicator < 1 :
		lst = socialDisaster(lst,instance,popSize)
	return lst


maxIter = 500
popSize = 500
crossoverRate = 50
mutationRate = 100

# Choose a dataset randomly
instance = list(satisfied.items())[0] 
print(instance[0])
# Generate a population
population =  pop(popSize)
print(len(population))
# Associates for each individual it's fitness in the population list
population = popFitness(instance[0],population)
population = diversification(population,instance[0],popSize)	


# ==============================================================================
meanList =[]
for i in range (0, maxIter):
	# generates a new generation with crossover and calculates it's fitness
	newCross = CrossGen(population, crossoverRate, instance[0])
	population = merge(newCross,population)
	population = diversification(population,instance[0],popSize)
	# Mutate an andividual randomly
	newMut = MutateGen(population)
	population = merge(newMut,population)
	mean2 = Average(population)
	meanList.append(mean2)

print("final mean")
print(meanList)
print(mean(meanList))	