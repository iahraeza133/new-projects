import random

def guess_word():
    names = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eva",
        "Frank",
        "Grace",
        "Hannah",
        "Isaac",
        "Jack"
    ]
    
    result_string = ""
    selected_word = random.choice(names)
    
    count = 0
    max_count = len(selected_word)
   
    while count < max_count:
        user_input = input("Please enter a character: ")

        if len(user_input) == 1 and user_input.isalpha():
            if user_input in selected_word:
                result_string += user_input
                print(f"Valid character added. Current string: {result_string}")
            else:
                print("Invalid input: character not in the selected word.")
        else:
            print("Invalid input: please enter a single alphabetic character.")

        count += 1

    return f"Game over! You had {max_count} attempts. Final string: {selected_word}"

print(guess_word())
