# Naive Bayes 
# Importing the libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import pickle 
# Importing the dataset 
dataset = pd.read_csv('data.csv') 
X = dataset.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7]].values 
y = dataset.iloc[:, 12].values 
# Splitting the dataset into the Training set and Test set 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 
0.25, random_state = 0) 
# Feature Scaling 
from sklearn.preprocessing import StandardScaler 
sc = StandardScaler() 
X_train = sc.fit_transform(X_train) 
X_test = sc.transform(X_test) 
# Fitting Naive Bayes to the Training set 
from sklearn.naive_bayes import GaussianNB 
classifier = GaussianNB() 
classifier.fit(X_train, y_train) 
# Predicting the Test set results 
y_pred = classifier.predict(X_test) 
# Making the Confusion Matrix 
from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(y_test, y_pred) 
filename = 'finalized_model.sav' 
pickle.dump(classifier, open(filename, 'wb')) 
print(classifier.predict([[10,50,60,70,15,20,25,30]])) 