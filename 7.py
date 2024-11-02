import csv

def calculate_email_fraction_difference():
    # Counters for hireable and non-hireable users
    hireable_with_email = 0
    hireable_total = 0
    non_hireable_with_email = 0
    non_hireable_total = 0

    # Read users.csv and calculate counts
    with open("users.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            has_email = bool(row["email"])
            is_hireable = row["hireable"].lower() == "true"
            
            if is_hireable:
                hireable_total += 1
                if has_email:
                    hireable_with_email += 1
            else:
                non_hireable_total += 1
                if has_email:
                    non_hireable_with_email += 1

    # Calculate fractions
    hireable_fraction = hireable_with_email / hireable_total if hireable_total > 0 else 0
    non_hireable_fraction = non_hireable_with_email / non_hireable_total if non_hireable_total > 0 else 0

    # Calculate difference
    difference = hireable_fraction - non_hireable_fraction

    # Output the result rounded to 3 decimal places
    print(f"{difference:.3f}")

# Run the function
calculate_email_fraction_difference()
