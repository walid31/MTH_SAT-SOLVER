from population import pop
import pickle
import random

# load the binary file of satisfied files in a list 
with open('datastructure/satisfied.pickle', 'rb') as f:
    satisfied = pickle.load(f)


# This function return the fitness of an instance
def fitness(instance):
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
	return round(temp_fit/325 * 100,2)		

# You can change your parameters here
popSize = 100
maxIter = 100
crossOver = 0.5
mutationRate = 0.1

# Generate a population
population =  pop(popSize)



for individ in population:
	listFit=[]
	for instance in satisfied:
		temp_fit=0
