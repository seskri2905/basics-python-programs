# Compound Interest
""" A = P(1 + R/100) t 

Compound Interest = A - P 
 """


def compound_interest(principal,rate,time):
    amount = principal * (pow((1 + rate / 100),time))
    ci = amount - principal
    print("Compound Interest:",ci)


compound_interest(10000, 10.25, 5)