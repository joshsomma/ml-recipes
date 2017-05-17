#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 10:43:59 2017

@author: josh
"""

from sklearn import tree
# feature values for smooth = 1; bumpy = 0
features = [[140,1],[130,1],[150,0],[170,0]]
# label values apple = 1; orange = 0
labels = ['apple','apple','orange','orange']

# create classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

result = clf.predict([[160,0]])
result2 = clf.predict([[130,1]])

print(result)
print(result2)