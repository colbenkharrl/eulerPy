# Colben Kharrl | December 2016 | Project Euler Problem 6

##
##  Description:
##  The sum of the squares of the first ten natural numbers is,
##      1^2 + 2^2 + ... + 10^2 = 385
##  The square of the sum of the first ten natural numbers is,
##      (1 + 2 + ... + 10)^2 = 55^2 = 3025
##  Hence the difference between the sum of the squares of the first ten natural
##  numbers and the square of the sum is 3025 − 385 = 2640.
##  Find the difference between the sum of the squares of the first one hundred
##  natural numbers and the square of the sum.
##

#   calculate sum of squares in range number
def sum_of_squares(number):
    solution = 0
    for i in range(1, number + 1, 1):
        solution += pow(i, 2)
    return solution

#   calculate square of the sum of numbers in range number
def square_of_sum(number):
    sum = 0
    for i in range(1, number + 1, 1):
        sum += i
    return pow(sum, 2)

#   beginning code execution
number = 100
sosq = sum_of_squares(number)
sqos = square_of_sum(number)
answer = sqos -sosq
print("The difference between the sum of squares and the square of sums is", answer)
