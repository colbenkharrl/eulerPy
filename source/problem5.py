# Colben Kharrl | December 2016 | Project Euler Problem 5

##
##  Description:
##  2520 is the smallest number that can be divided by each of the numbers from
##  1 to 10 without any remainder.
##  What is the smallest positive number that is evenly divisible by all of the
##  numbers from 1 to 20?
##

#   loop until a solution matches constraints
def smallest_multiple(limit):
    solution = limit
    while True:
        for i in range(1,limit + 1,1):
            if solution % i != 0:
                break
            if i == limit:
                return solution
        solution += limit

#   beginning of code execution
limit = 20
answer = smallest_multiple(limit)
print("Smallest number that is multiple of number in range 1-20:", answer)
