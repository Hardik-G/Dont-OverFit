<h1> Dont-Overfit </h1>

<h2> Link to Problem Statement: </h2>

[https://www.kaggle.com/c/dont-overfit-ii/overview](https://www.kaggle.com/c/dont-overfit-ii/overview)

<h2> Link to Datasets: </h2>

[https://www.kaggle.com/c/dont-overfit-ii/data](https://www.kaggle.com/c/dont-overfit-ii/data)

The dataset for the project can also be found in the [Datasets](https://github.com/mayankagarwal44442/Dont-OverFit/tree/master/Datasets) directory.

<h2> Literature Survey and Exploratory Data Analysis: </h2>

<h3> Literature Survey </h3>

Literature Survey of this project can be found in the [Literature Survey](https://github.com/mayankagarwal44442/Dont-OverFit/tree/master/Literature%20Survey) directory.

<h3> Exploratory Data Analysis </h3>

Exploratory Data Analysis of this project can be found in the [Exploratory Data Analysis](https://github.com/mayankagarwal44442/Dont-OverFit/tree/master/Exploratory%20Data%20Analysis) directory.

<h2> Experimentation: </h2>

<h3> Making sure the data is not sequential </h3>

We know that each target depends on the 300 features corresponding to it, but since we are completely oblivious to origin of data, there is a possibility that the data may be sequential. That is, a row's output can depend on previous output. The result of this will change the way we look at data henceforth. For this purpose, we plot acf and pacf for target variable.

The code and plot is available in the file Exploratory Data Analysis/Check_sequential. 
The results state unequivocally that rows do not have autocorrelation, thus we can treat each row as independent of the other

<h3> Selecting a Classification Model: </h3>

Let us try out a few Classification Models without any Dimensionality Reduction and select the best one for future experimentation.

<ol>
<li> Logistic Regression Classifier (Accuracy = 0.662) </li>
<li> Support Vector Classifier (Accuracy = 0.663) </li>
<li> Decision Tree Classifier (Accuracy = 0.562) </li>
<li> Gaussian Naive Bayes Classifier (Accuracy = 0.611) </li>
<li> Gaussian Process Classifier (Accuracy = 0.526) </li>
<li> Random Forest Classifier (Accuracy = 0.553) </li>
<li> AdaBoost Classifier (Accuracy = 0.636) </li>
<li> K Nearest Neighbours Classifier (Accuracy = 0.560) </li>
<li> Artificial Neural Network Classifier (Accuracy = 0.667) </li>
</ol>

<strong> NOTE: </strong> Python Implementation for the above Classification Models can be found in the [Classification Models](https://github.com/mayankagarwal44442/Dont-OverFit/tree/master/Classification%20Models) directory.

<h3> Dimensionality Reduction </h3>

Yet to be done.......


<h3> References </h3>

* ACF and PACF: https://machinelearningmastery.com/gentle-introduction-autocorrelation-partial-autocorrelation/



<h3> To Do </h3>

*Correct all paths to datasets