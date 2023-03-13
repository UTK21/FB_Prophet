# import libraries 
import pandas as pd # Import Pandas for data manipulation using dataframes
import numpy as np # Import Numpy for data statistical analysis 
import matplotlib.pyplot as plt # Import matplotlib for data visualisation
import random
import seaborn as sns
#from fbprophet import Prophet

# dataframes creation for both training and testing datasets 
df=pd.read_csv('avocado.csv')

# Let's view the head of the training dataset
print(df.head())
