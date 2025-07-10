def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():  # check if it's a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Test
v, c = count_vowels_consonants("Hello World!")
print("Vowels:", v)        # Output: 3 (e, o, o)
print("Consonants:", c)    # Output: 7 (H, l, l, W, r, l, d)
