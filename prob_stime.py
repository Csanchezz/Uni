import math 

def probability(l, x):
    response = (l**x * math.e**(-l)) / math.factorial(x)
    print(response)
    return response

def service_time(u, t):
    r = 1-math.e**(-u*t)
    print(r)
    return r

# a = 1 - probability(4, 1) - probability(4, 0)

# print("last: ",a)
# service_time(0.6, 3)

probability(2, 1 )