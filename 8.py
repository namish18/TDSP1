import pandas as pd
import numpy as np
from scipy import stats

# Read the CSV files
users = pd.read_csv('users.csv')
repos = pd.read_csv('repositories.csv')

# Clean up company names
users['company'] = users['company'].fillna('').str.strip().str.lstrip('@').str.upper()

# 1. Language with highest average stars per repository
language_avg_stars = repos.groupby('language')['stargazers_count'].mean().sort_values(ascending=False)
top_language = language_avg_stars.index[0]
top_language_avg_stars = language_avg_stars.iloc[0]

print("Language with highest average stars per repository:")
print(f"{top_language} with {top_language_avg_stars:.2f} average stars")
