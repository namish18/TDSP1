import pandas as pd
import numpy as np

# Read the users CSV
users = pd.read_csv('users.csv')



#  Most common surname
# Clean and process names
def get_last_name(name):
    if pd.isna(name):
        return np.nan
    # Trim and split by whitespace, get the last word
    parts = str(name).strip().split()
    return parts[-1] if parts else np.nan

# Extract last names
users['last_name'] = users['name'].apply(get_last_name)

# Count last name frequencies
surname_counts = users['last_name'].value_counts()

# Find the maximum count
max_count = surname_counts.max()

# Get surnames with the maximum count (sorted alphabetically)
most_common_surnames = sorted(surname_counts[surname_counts == max_count].index.tolist())

print("16. Most common surname(s):")
print(", ".join(most_common_surnames))
print(f"Number of users with the most common surname: {max_count}")
