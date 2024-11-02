import pandas as pd
import numpy as np
from scipy import stats

# Read the CSV files
users = pd.read_csv('users.csv')
repos = pd.read_csv('repositories.csv')
users['leader_strength'] = users['followers'] / (1 + users['following'])
top_5_leaders = users.nlargest(5, 'leader_strength')['login'].tolist()
print("\nTop 5 users by Leader Strength:")
print(", ".join(top_5_leaders))
