import pandas as pd
import numpy as np

# Read the users CSV
users = pd.read_csv('users.csv')

# Email sharing by hireable status
# Calculate fraction of users with email for hireable and non-hireable groups
hireable_email_fraction = users[users['hireable'] == True]['email'].notna().mean()
non_hireable_email_fraction = users[users['hireable'] == False]['email'].notna().mean()
email_fraction_diff = hireable_email_fraction - non_hireable_email_fraction
print(f"15. Difference in email sharing (hireable - non-hireable): {email_fraction_diff:.3f}")

