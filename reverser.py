def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(words)
print(reverse_words("Hello World Python"))