import pandas as pd
from sklearn.linear_model import LogisticRegression

training = pd.read_csv('train.csv')

lst = []

for i in range(2, 302):
	lst.append(i)

xtrain = training.iloc[:, lst].values
ytrain = training.iloc[:, 1].values

classifier = LogisticRegression(random_state = 0)
classifier.fit(xtrain, ytrain)

testing = pd.read_csv('test.csv')

lst = []

for i in range(1, 301):
	lst.append(i)

xtest = testing.iloc[:, lst].values

ytest = classifier.predict(xtest)

id = []

for i in range(250, 20000):
	id.append(i)

result = {'id': id, 'target': ytest}

result = pd.DataFrame(result)

result.to_csv("Result.csv")