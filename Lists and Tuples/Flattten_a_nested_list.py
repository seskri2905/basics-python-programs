def flatted_a_nested_list(lst):
    flat = []
    for sublist in lst:
        for item in sublist:
            flat.append(item)
    return flat

print(flatted_a_nested_list([[1,2], [3,4]]))