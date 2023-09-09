import os
import numpy as np

pathNeg = r'\Users\f1506\Documents\data labs\data\movie\neg'
pathPos = r'\Users\f1506\Documents\data labs\data\movie\pos'

pos = os.listdir(pathNeg)
neg = os.listdir(pathPos)
posList = []
negList = []

os.chdir(pathNeg)
for _ in pos:
    with open(_,'r') as f:
        words = f.readline()
        for i in words.split():
            posList.append(i)

os.chdir(pathPos)
for _ in neg:
    with open(_,'r') as f:
        words = f.readline()
        for i in words.split():
            negList.append(i)
                       
allList = []
allList.extend(posList)
allList.extend(negList)

words = list(set(allList))
print(words)

results = np.zeros((len(allList), len(words)))


for i, sequence in enumerate(allList):
    for j in sequence.split():
        results[i, words.index(j)] = 1

print(results) 