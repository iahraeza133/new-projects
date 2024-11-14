import random

def guess():
    count = 0
    max_attempts = 5
    
    # Generate a random number once for the user to guess
    random_number = random.randint(1, 100)
    
    low_bound = 1
    upper_bound = 100

    # Loop until the user has guessed 5 times
    while count < max_attempts:
        # Get user input
        user_input = int(input(f"Enter a number between {low_bound} and {upper_bound}: "))

        # Compare the user input with the random number
        if user_input == random_number:
            print(f"Congratulations! You guessed the correct number: {random_number}")
            break  # End the loop if the user guesses correctly
        else:
            print(f"Sorry, the correct number was {random_number}. Your guess was {user_input}.")
        
        count += 1  # Increment the count after each guess

    if count == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {random_number}.")

# Call the function
guess()
