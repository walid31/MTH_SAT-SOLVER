import os 
import pickle

for(root,dirs,files) in os.walk('./../dataset'):
	satisfiable = dirs[1]
	unsatisfiable = dirs[0]
	break

for(root,dirs,files) in os.walk('./../dataset/'+satisfiable):
	satInstances = files
	break

for(root,dirs,files) in os.walk('./../dataset/'+unsatisfiable):
	unsatInstances = files
	break

satFiles = []
for i in satInstances:
	file = open ('./../dataset/'+satisfiable+'/'+i, 'r', encoding='utf-8').readlines()

	instance=[]
	clause=[]
	clause = file[8].split(' ')
	instance.append(clause[1:4])
	for i in range(9,len(file)-3):
		clause=file[i].split(' ')
		instance.append(clause[0:3])
	satFiles.append(instance)


unsatFiles = []
for i in unsatInstances:
	file = open ('./../dataset/'+unsatisfiable+'/'+i, 'r', encoding='utf-8').readlines()

	instance=[]
	clause=[]
	clause = file[8].split(' ')
	instance.append(clause[1:4])
	for i in range(9,len(file)-3):
		clause=file[i].split(' ')
		instance.append(clause[0:3])
	unsatFiles.append(instance)

dicsat=dict()
j = 0
for i in satInstances:
	dicsat[i]= satFiles[j]
	j+=1

dicUnsat=dict()
j = 0
for i in unsatInstances:
	dicUnsat[i]= unsatFiles[j]
	j+=1


with open('satisfied.pickle', 'wb') as f:
    pickle.dump(dicsat, f)

