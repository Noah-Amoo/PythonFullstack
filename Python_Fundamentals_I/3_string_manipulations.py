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


# 3) Build a simple text formatter that takes a paragraph and: capitalizes the first letter of each sentence, removes extra whitespace, and wraps lines at 80 characters.

import re
import textwrap

def text_formatter(paragraph):
    # Remove extra whitespace
    paragraph = " ".join(paragraph.split())

    # Splits into sentences while maintaining the punctuation using regular expression
    parts = re.split(r"([.!?])", paragraph)

    formatted_sentences = []
    for i in range(0, len(parts), 2):
        sentence = parts[i].strip()
        punctuation = parts[i + 1] if i + 1 < len(parts) else ""
        if sentence:
            formatted_sentences.append(sentence.capitalize() + punctuation)

    formatted_text = " ".join(formatted_sentences)

    #Wrap at 80 characters
    return textwrap.fill(formatted_text, width=80)


paragraph = "   hello world.   this is python! i just   love having fun    with it."
print(text_formatter(paragraph))

# Outputs: Hello world. This is python! I just love having fun with it.


# 4) Write a function that takes a string and returns it in snake_case, camelCase, and PascalCase formats.

def case_convert(text):
    words = text.split(' ')

    snake_case = "_".join(word.lower() for word in words)
    camel_case = words[0].lower() + "".join(word.capitalize() for word in words[1:]) if words else ""
    pascal_case = "".join(word.capitalize() for word in words)

    return snake_case, camel_case, pascal_case


result = case_convert("hello noah amoo")
print(result)

# Output: 'hello_noah_amoo', 'helloNoahAmoo', 'HelloNoahAmoo'