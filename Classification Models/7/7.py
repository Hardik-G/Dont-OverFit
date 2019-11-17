# Import required modules
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier

# Import training and testing data
training = pd.read_csv('../../Datasets/train.csv')
testing = pd.read_csv('../../Datasets/test.csv')

# Obtaining feature and target values of training data
train_features = []
for i in range(2, 302):
	train_features.append(i)
xtrain = training.iloc[:, train_features].values
ytrain = training.iloc[:, 1].values

# Obtaining feature values of testing data
test_features = []
for i in range(1, 301):
	test_features.append(i)
xtest = testing.iloc[:, test_features].values

# Perform logistic regression to fit a model
classifier = AdaBoostClassifier(n_estimators=50, learning_rate=1)
classifier.fit(xtrain, ytrain)

# Predict target values for test data
ytest = classifier.predict(xtest)

# Export result values to a csv file to test on kaggle
id = []
for i in range(250, 20000):
	id.append(i)
result = {'id': id, 'target': ytest}
result = pd.DataFrame(result)
result.to_csv("Result.csv", index = False)
