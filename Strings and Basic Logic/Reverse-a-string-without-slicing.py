def reverse_string(s):
    reverse = ''
    for char in s:
        reverse = char + reverse
    return reverse

print(reverse_string("sesha"))

""" def using_slicing(s):
    return s[::-1]

print(using_slicing("sesha")) """

""" name = "sesha"

print(name[::-1]) """