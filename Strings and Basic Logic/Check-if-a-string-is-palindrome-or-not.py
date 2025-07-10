def check_palindrome(s):
    left = 0
    right = len(s) - 1
    while(left < right):
        for char in s:
            if(s[left] != s[right]):
                return False
            left = left + 1
            right = right - 1
    return True

print(check_palindrome("madam"))
print(check_palindrome("sesha"))