import pandas as pd
import numpy as np
from scipy import stats

# Read the CSV files
users = pd.read_csv('users.csv')
repos = pd.read_csv('repositories.csv')

# Clean up company names
users['company'] = users['company'].fillna('').str.strip().str.lstrip('@').str.upper()

slope, intercept, r_value, p_value, std_err = stats.linregress(users['public_repos'], users['followers'])
print(f"\nRegression Analysis:")
print(f"Slope (Followers per additional repo): {slope:.4f}")
print(f"R-squared: {r_value**2:.4f}")
print(f"P-value: {p_value:.4f}")
