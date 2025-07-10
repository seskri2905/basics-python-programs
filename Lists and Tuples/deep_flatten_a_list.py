def deep_flatten_a_list(lst):
    result =  []
    for item in lst:
        if isinstance(item,list):
            result.extend(deep_flatten_a_list(item))
        else:
            result.append(item)
    return result



print(deep_flatten_a_list([1, [2, [3, 4]], 5]))