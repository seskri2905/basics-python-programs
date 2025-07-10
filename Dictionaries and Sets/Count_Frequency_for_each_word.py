def count_word_frequency(str):
    words = str.split()
    frequency = {}

    for item in words:
        if item in frequency:
            frequency[item] = frequency[item] + 1
        else:
            frequency[item] = 1
    
    return frequency
 



print(count_word_frequency("this is a test this is only a test"))