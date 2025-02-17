#Tobby Akinwale
#17/02/2025
#findFirstFourPNs

from perfectNumber import isPerfectNumber

def find_first_four_perfect_number():
    count = 0
    num = 1
    while count < 4:
        if isPerfectNumber (num):
            print(f"{num} is a perfct number")
            count +=1
        num += 1
        
find_first_four_perfect_numbers()



