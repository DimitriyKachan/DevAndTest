def first_non_repeating_letter(word):
    word_lower = word.lower()
    for i in range(len(word_lower)-1):
        if word_lower[i] != word_lower[i+1]:
            return word_lower[i+1]


print(first_non_repeating_letter("aaaa"))
print(first_non_repeating_letter("abaa"))
