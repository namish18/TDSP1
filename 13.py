import pandas as pd
import numpy as np
from scipy import stats

# Read the CSV files
users = pd.read_csv('users.csv')
repos = pd.read_csv('repositories.csv')


# Remove users without bios
users_with_bio = users[users['bio'].notna() & (users['bio'] != '')]

# Calculate bio length in Unicode characters
users_with_bio['bio_length'] = users_with_bio['bio'].str.len()

# Regression of followers on bio length
slope, intercept, r_value, p_value, std_err = stats.linregress(
    users_with_bio['bio_length'], 
    users_with_bio['followers']
)
print(f"13. Regression slope of followers on bio length: {slope:.3f}")
