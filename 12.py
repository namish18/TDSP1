import pandas as pd
import numpy as np
from scipy import stats

# Read the CSV files
users = pd.read_csv('users.csv')
repos = pd.read_csv('repositories.csv')



#  Average following for hireable vs non-hireable users
avg_following_hireable = users[users['hireable'] == True]['following'].mean()
avg_following_not_hireable = users[users['hireable'] == False]['following'].mean()
following_diff = avg_following_hireable - avg_following_not_hireable
print(f"12. Difference in average following (hireable - not hireable): {following_diff:.3f}")
