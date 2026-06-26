def sentence_analysis(sentence):
    words = sentence.split()
    word_count = len(words)
    character_count = len(sentence.replace(' ', ''))
    # The key of len ensures that the longest word is returned
    longest_word = max(words, key=len) if words else ""

    return word_count, character_count, longest_word


info = "I am the best programmer in the world"

print(sentence_analysis(info))