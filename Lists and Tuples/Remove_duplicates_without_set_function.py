def remove_duplicates(lst):
    seen = {}
    unique = []

    for values in lst:
        if values not in seen:
            seen[values] = True
            unique.append(values)
        
    return unique

print(remove_duplicates([1,1,1,1,1,2,22,2,4,5,6,4,3,3]))