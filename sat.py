import pickle

with open('datastructure/satisfied.pickle', 'rb') as f:
    satisfied = pickle.load(f)

for i in satisfied:
	print (satisfied[i])
	print (i)