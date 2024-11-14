import random

def tas():
    count = 0
    max_count = int(input("How many times do you want to roll the dice? "))  # Get the number of rolls from the user
    total_score = 0  # Total score

    while count < max_count:
        generated_number = random.randint(1, 6)  # Generate a random number between 1 and 6
        print(f"The dice rolled and the number: {generated_number} was obtained.")
        total_score += generated_number  # Accumulate scores
        count += 1

    print(f"Total score: {total_score}")  # Display the total score

# Call the function
tas()
