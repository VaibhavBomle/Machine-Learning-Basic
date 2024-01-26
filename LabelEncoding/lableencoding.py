# -*- coding: utf-8 -*-
"""LableEncoding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kBH1GvZLA4KUwXlATltV5ViFAXuZZsva
"""



"""Label encoding:


*   Converting the labels into numeric form


"""

# importing the Dependencies
import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""Lable Encoding of Breast Cancer Dataset"""

# lading the data rom csv file to pandas dataFrame
cancer_data = pd.read_csv('/content/breast_cancer_data.csv')

# first 5 rows of dataset
cancer_data.head()

# finding the count of different lables
cancer_data['diagnosis'].value_counts()

# load label encoder function
label_encode = LabelEncoder()

labels = label_encode.fit_transform(cancer_data.diagnosis)
print(labels)

# appending the labels to the DataFrame
cancer_data['target'] = labels

cancer_data.head()

"""0 --> Benign


1 --> Malignant
"""

cancer_data['target'].value_counts()

"""Label encoding od iris data"""

# lading the data from csv file to pandas dataFrame
iris_data = pd.read_csv('/content/iris_data.csv')

iris_data.head()

iris_data['Species'].value_counts()

# loading the label encoder
label_encoder_1 = LabelEncoder()

iris_labels = label_encoder_1.fit_transform(iris_data.Species)
print(iris_labels)

iris_data['target'] = iris_labels

iris_data.head()

iris_data['target'].value_counts()

"""Iris-setosa  --> 0

Iris-versicolor --> 1


Iris-virninica  --> 2
"""