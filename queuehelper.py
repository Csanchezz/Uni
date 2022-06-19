import math 

def helper(s, l, m):
    n= 0
    for x in range(s+1):

        if x == s: 
        
            response = (l/m)**x/math.factorial(x) * s * m / (s*m-l)
            n = n+response
        else: 
            response = (l/m)**x/math.factorial(x)
            n = n+response
    r = 1/n
    print(r)
    return r


helper(4, 3, 1)