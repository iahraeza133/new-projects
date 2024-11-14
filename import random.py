import random
import string

def password(length=6, is_upper=True, is_lower=True):
    characters = ""
    
    # Adding character sets based on the boolean flags
    if is_upper:
        characters += string.ascii_uppercase  # Adds uppercase letters
    if is_lower:
        characters += string.ascii_lowercase  # Adds lowercase letters
    characters += string.digits  # Always include digits
    characters += string.punctuation  # Optional: include punctuation
    
    if not characters:
        raise ValueError("At least one character type must be selected.")
    
    # Generate a random password
    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

# Example usage
print(password(length=8, is_upper=True, is_lower=True))  # Adjust length and flags as needed
