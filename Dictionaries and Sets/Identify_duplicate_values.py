def find_duplicate_values(d):
    seen = set()
    duplicates = set()

    for value in d.values():
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)

    return duplicates

d = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
print(find_duplicate_values(d))
