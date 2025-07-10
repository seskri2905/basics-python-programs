def merge_and_sum(dict1,dict2):
    result = dict1.copy()

    for key,value in dict2.items():
        if key in result:
            result[key] = result[key] + value
        else:
            result[key] = value

    return result    
    
    
    
    
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 25}

print(merge_and_sum(d1,d2))