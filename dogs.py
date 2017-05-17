#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:27:34 2017

@author: josh
"""

import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labradors = 500

greyhound_height = 28 + 4 * np.random.randn(greyhounds)
labrador_height = 24 + 4 * np.random.randn(labradors)

plt.hist([greyhound_height,labrador_height], stacked=True, color=['r','b'])
plt.show()
