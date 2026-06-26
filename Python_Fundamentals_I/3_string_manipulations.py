# 1) Write a function that takes a sentence and returns: word count, character count (excluding spaces), and the longest word.

def sentence_analysis(sentence):
    words = sentence.split()
    word_count = len(words)
    character_count = len(sentence.replace(' ', ''))
    # The key of len ensures that the longest word is returned
    longest_word = max(words, key=len) if words else ""

    return word_count, character_count, longest_word


info = "I am the best programmer in the world"

print(sentence_analysis(info))


#2) Create a password validator that checks: minimum 8 characters, at least one uppercase, one lowercase, one digit, and one special character. Use string methods only (no regex).

def password_validator(password):
    has_min_char = len(password) >= 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    return has_min_char and has_uppercase and has_lowercase and has_digit and has_special

print(password_validator("Noa3h@Amoo")) # Returns True