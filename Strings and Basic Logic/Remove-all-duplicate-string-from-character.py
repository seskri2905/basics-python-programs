def remove_duplicate(s):
    seen = set()    
    result = ""

    for char in s:
        if char not in seen:
            seen.add(char)
            result = result + char
    return result



print(remove_duplicate("banana"))
print(remove_duplicate("sesha"))