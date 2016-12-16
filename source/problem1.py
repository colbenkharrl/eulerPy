# Colben Kharrl | December 2016 | Project Euler Problem 1

##
##  Description:
##  If we list all the natural numbers below 10 that are
##  multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
##  Find the sum of all the multiples of 3 or 5 below 1000.
##

#   calculate sum of constraint multiples under domain 
def sum_of_multiples(domain, constraints):
    solution = 0
    multiples = []
    for multiple in constraints:
        for i in range(0,domain,multiple):
            if i not in multiples:
                multiples.append(i)
                solution += i
    return solution
            
#   beginning of code execution
set_domain = 1000
set_constraints = [3,5]
answer = sum_of_multiples(set_domain, set_constraints)
print("Sum of multiples of 3 and 5 in numbers under 1000:", answer)
