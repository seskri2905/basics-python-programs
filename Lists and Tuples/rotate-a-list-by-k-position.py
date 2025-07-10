def rotate_list_in_place(lst, k):
    n = len(lst)
    k = k % n  # Handles if k > n

    for _ in range(k):
        last = lst.pop()         # Step 1
        lst.insert(0, last)      # Step 2

    return lst

print(rotate_list_in_place([1, 2, 3, 4], 1))      # [4, 1, 2, 3]
print(rotate_list_in_place([1, 2, 3, 4, 5], 2))   # [4, 5, 1, 2, 3]