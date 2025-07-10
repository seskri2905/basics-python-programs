def split_the_even_and_odd(lst):
    odd_list = []
    even_list = []
    
    for item in lst:
        if item % 2 == 0:
            even_list.append(item)
        else:
            odd_list.append(item)
    
    return odd_list,even_list



odd , even = split_the_even_and_odd([1,2,3,4,5])


print("Odd List:",odd)
print("Even List:",even)