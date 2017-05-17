#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:30:04 2017

@author: josh
"""

from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn import tree


iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = .5)


my_classifier = tree.DecisionTreeClassifier()

my_classifier.fit(X_train,y_train)

predictions = my_classifier.predict(X_test)
print(predictions)
print(accuracy_score(y_test,predictions))
