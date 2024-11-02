import csv
from collections import Counter
from datetime import datetime

def get_second_most_common_language_after_2020():
    # Step 1: Filter users who joined after 2020
    users_after_2020 = set()
    with open("users.csv", "r", encoding="utf-8") as users_file:
        reader = csv.DictReader(users_file)
        for row in reader:
            joined_date = datetime.strptime(row["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            if joined_date.year > 2020:
                users_after_2020.add(row["login"])
    
    # Step 2: Count languages used by filtered users
    language_counter = Counter()
    with open("repositories.csv", "r", encoding="utf-8") as repos_file:
        reader = csv.DictReader(repos_file)
        for row in reader:
            if row["login"] in users_after_2020:
                language = row["language"]
                if language:  # Ignore missing or empty language fields
                    language_counter[language] += 1

    # Step 3: Find the second most common language
    most_common_languages = language_counter.most_common(2)
    if len(most_common_languages) >= 2:
        second_most_common_language = most_common_languages[1][0]
        print(f"The second most popular programming language among users who joined after 2020 is: {second_most_common_language}")
    else:
        print("Not enough data to determine the second most popular language.")

# Run the function
get_second_most_common_language_after_2020()
