#Tobby Akinwale
#17/02/24
#PerfectNumber.py

from divisors import divisors

def isPerfectNumber(n):
    if sum(divisors(n)) == n:
        return True
        return False
    
print (isPerfectNumber(8128))

if (isPerfectNumber(8128)): print("8128 is a perfect number")
