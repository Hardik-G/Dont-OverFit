# Import required modules
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Import training and testing data
training = pd.read_csv('Datasets/train.csv')
testing = pd.read_csv('Datasets/test.csv')

# Obtaining feature and target values of training data
train_features = []
for i in range(300):
	train_features.append(str(i))
xtrain = training[train_features]
ytrain = training['target']

# Obtaining feature values of testing data
test_features = []
for i in range(300):
	test_features.append(str(i))
xtest = testing[test_features]

# Perform logistic regression to fit a model
classifier = LogisticRegression(random_state = 0, solver = "liblinear", penalty = 'l1')
classifier.fit(xtrain, ytrain)

# Predict target values for test data
ytest = classifier.predict(xtest)

# Export result values to a csv file to test on kaggle
id = []
for i in range(250, 20000):
	id.append(i)
result = {'id': id, 'target': ytest}
result = pd.DataFrame(result)
result.to_csv("result.csv", index = False)


important_features = []
for i in range(len(classifier.coef_[0])):
	if classifier.coef_[0][i] != 0:
		important_features.append(i)

important_features = {'features': important_features}
important_features = pd.DataFrame(important_features)
important_features.to_csv("imp_fea.csv", index = False)