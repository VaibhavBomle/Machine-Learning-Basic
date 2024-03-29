# -*- coding: utf-8 -*-
"""NumericalDataSetPrePreprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YTESft8jeR3U9L_-NBFf3dMMphU1xcpu
"""

#Imporitng the Dependencies
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

"""Data Collection and Pre-Processing"""

# loading the data as csv file to a pandas dataframe
diabetes_data = pd.read_csv('/content/diabetes.csv')

# first 5 rows of the data frame
diabetes_data.head()

# number of trows and column
diabetes_data.shape

diabetes_data.describe()

# split data set into feature and target

"""Seperating Features and Target"""

X = diabetes_data.drop(columns = 'Outcome', axis = 1)
Y = diabetes_data['Outcome']

print(X)

print(Y)

"""0 --> Non Diabeted


1 --> Diabtetic

Data Standardizaion
"""

scaler = StandardScaler()

standardized_data = scaler.fit_transform(X)

print(standardezed_data)

X = standardezed_data
print(X)

print(Y)

"""Splitting the dataset into Training data and testing Data"""

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)