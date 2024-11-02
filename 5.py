import csv
from collections import Counter

def get_most_common_language():
    # Counter to track programming language occurrences
    language_counter = Counter()

    # Read the repositories.csv file and count each programming language
    with open("repositories.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            language = row["language"]
            if language:  # Ignore missing or empty language fields
                language_counter[language] += 1

    # Get the most common language
    most_common_language, _ = language_counter.most_common(1)[0]
    
    print(f"The most popular programming language among these users is: {most_common_language}")

# Run the function
get_most_common_language()
