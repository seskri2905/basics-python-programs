# Standard way
""" n = int(input("Enter the factorial no.:"))

fact = 1

for i in range(1 , n + 1):
    fact = fact * i

print(fact) """

# Using a recursive function
""" def fact(n):

    return 1 if (n == 1 or n == 0) else n * fact(n - 1)

num = 5
print(fact(num))
 """

# Using math.factorial()
""" import math

def factorial(n):
    return(math.factorial(n))

num = 5
print(factorial(num)) """