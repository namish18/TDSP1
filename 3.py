import csv
from collections import Counter

def get_top_licenses():
    # Counter to track license occurrences
    license_counter = Counter()

    # Read the repositories.csv file and count each license
    with open("repositories.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            license_name = row["license_name"]
            if license_name:  # Ignore missing licenses
                license_counter[license_name] += 1

    # Get the three most common licenses
    top_licenses = [license for license, _ in license_counter.most_common(3)]
    
    # Print the result in comma-separated format
    print(", ".join(top_licenses))

# Run the function
get_top_licenses()
