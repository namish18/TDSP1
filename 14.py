import pandas as pd
import numpy as np
from scipy import stats

# Read the CSV files
users = pd.read_csv('users.csv')
repos = pd.read_csv('repositories.csv')

#  Repositories created on weekends (UTC)
repos['created_at'] = pd.to_datetime(repos['created_at'])
repos['is_weekend'] = repos['created_at'].dt.day_name().isin(['Saturday', 'Sunday'])

weekend_repos_by_user = repos[repos['is_weekend']].groupby('login').size().sort_values(ascending=False)
top_5_weekend_repo_creators = weekend_repos_by_user.head(5).index.tolist()
print("14. Top 5 users creating most repositories on weekends:")
print(", ".join(top_5_weekend_repo_creators))
