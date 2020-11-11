import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ways to look at the data, in tabular form

data_train = pd.read_csv("C:/Users/User/Desktop/DataScience/sales_train.csv")
data_train.describe()
data_train.shape

data_train['date'] = pd.to_datetime(data_train['date'], format='%Y-%m-%d')
data_train['year'] = data_train['date'].dt.year

data_train.head()
data_train['date'].max()

## add more analysis

### EDIT FOR NEW BRANCH ###
