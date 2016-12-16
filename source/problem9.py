# Colben Kharrl | December 2016 | Project Euler Problem 9

##
##  Description:
##  A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
##  a^2 + b^2 = c^2
##  For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
##  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##  Find the product abc.
##

#   test if three values are valid under pythagorean theorem
def is_pythagorean(a, b, c):
    if (pow(a,2) + pow(b,2)) != pow(c,2):
        return False
    return True

#   search for valid triplet that sums to constant
def product_of_special_sum(constant):
    for a in range(1, constant):
        for b in range(1, constant):
            if b < a:
                continue
            for c in range(1, constant):
                if c < b or a + b + c != constant or not is_pythagorean(a,b,c):
                    continue
                else:
                    return a*b*c

#   beginning of code execution
constant = 1000
answer = product_of_special_sum(constant)
print("Product of pythagorean triplet that has a sum of 1000:", answer)
                
