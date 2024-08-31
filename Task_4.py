def count_vowels(text):
    vowels = "aeiou"
    text = text.lower()
    return sum(1 for char in text if char in vowels)

print(count_vowels("Hello World"))