def invert_a_dictionary(dct):
    result = {}
    for key,value in dct.items():
        result[value] = key
    
    return result

d1 = {'a': 10, 'b': 20, 'c': 30}

print(invert_a_dictionary(d1))