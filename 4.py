import csv
from collections import Counter

def get_most_common_company():
    # Counter to track company occurrences
    company_counter = Counter()

    # Read the users.csv file and count each company
    with open("users.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            company = row["company"]
            if company:  # Ignore empty company fields
                company_counter[company] += 1

    # Get the most common company
    most_common_company, _ = company_counter.most_common(1)[0]
    
    print(f"The company where the majority of these developers work is: {most_common_company}")

# Run the function
get_most_common_company()
