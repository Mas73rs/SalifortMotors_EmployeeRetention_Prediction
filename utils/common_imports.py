
# common_imports.py
# This script contains imports and utility functions commonly used across the project notebooks

# Data Manipulation
import pandas as pd
import numpy as np

# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Metrics and other functions
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score,\
f1_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.tree import plot_tree

# For display all columns in dataframes
pd.set_option('display.max_columns', None)

# Saving model
import pickle

# Warnings 
import warnings
warnings.filterwarnings("ignore")



# Utility function example
def calculate_percentage(value, total):
    return (value / total) * 100
