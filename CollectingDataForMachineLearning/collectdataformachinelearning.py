# -*- coding: utf-8 -*-
"""CollectDataForMachineLearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1endE1QHE1dSHCW0R3RuazbeJKZre6qhO

Data Collection Sites:


*   Kaggle
*   UCI Machine Learning Repositoty
*   Google Dataset Search
"""

import pandas as pd

# loading a dataset to a pandas dataframe
dataset = pd.read_csv('/content/housing.csv')
dataset.head()