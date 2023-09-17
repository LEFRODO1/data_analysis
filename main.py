import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn import metrics

pathNeg = r'C:\Users\f1506\Documents\data labs\data\movie\neg'
pathPos = r'C:\Users\f1506\Documents\data labs\data\movie\pos'

pos = os.listdir(pathNeg)
neg = os.listdir(pathPos)
posList = []
negList = []
posList_2 = []
negList_2 = []
Y = []

os.chdir(pathNeg)
for _ in pos:
    Y.append(1)
    with open(_,'r') as f:
        posList_2.append("")
        words = f.readline()
        posList_2[-1] += words
        for i in words.split():
            posList.append(i)

os.chdir(pathPos)
for _ in neg:
    Y.append(0)
    with open(_,'r') as f:
        negList_2.append("")
        words = f.readline()
        negList_2[-1] += words
        for i in words.split():
            negList.append(i)


                       
allList = []
allList.extend(posList)
allList.extend(negList)
print(len(allList))
words = list(set(allList))
# print(words)
print(len(Y))

allList = []
allList.extend(posList_2)
allList.extend(negList_2)

results = np.zeros((len(allList), len(words)))


for i, sequence in enumerate(allList):
    for j in sequence.split():
        results[i, words.index(j)] = 1

print(results.shape) 

X_train, X_test, Y_train, Y_test = train_test_split(results, Y, test_size=0.2, random_state=0)

clf = BernoulliNB()

clf.fit(X_train, Y_train)

print(metrics.accuracy_score(clf.predict(X_test),Y_test))