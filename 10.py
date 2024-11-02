import pandas as pd
import numpy as np
from scipy import stats

# Read the CSV files
users = pd.read_csv('users.csv')
repos = pd.read_csv('repositories.csv')

correlation, p_value = stats.pearsonr(users['followers'], users['public_repos'])
print(f"\nCorrelation between followers and public repositories: {correlation:.4f}")
print(f"P-value: {p_value:.4f}")
