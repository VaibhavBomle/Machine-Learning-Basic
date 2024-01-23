# -*- coding: utf-8 -*-
"""Importing Datasets through Kaggle API.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14khVyx2Vm9-RyXY86RC_xZOeGXJmxuzk

Import data set from kaggle API
"""

#install Kaggle API
!pip install kaggle

"""Upload your Kaggle.json file"""

# Configure the path of kaggle.json file
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

"""Importing Earthquake dataset"""

# API to fetch the dataset from Kaggle
!kaggle competitions download -c LANL-Earthquake-Prediction

# extracting the compressed Dataset
from zipfile import ZipFile
dataset = '/content/LANL-Earthquake-Prediction.zip'

with ZipFile(dataset,'r') as zip:
  zip.extractall()
  print("The dataset is extracted")