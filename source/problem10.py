# Colben Kharrl | December 2016 | Project Euler Problem 10

from math import sqrt

##
##  Description:
##  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##  Find the sum of all the primes below two million.
##

#   calculate sum of primes under limit
def sum_of_primes_under(limit):
    prime_sum = 0
    for i in range(2,limit):
        if prime(i):
            prime_sum += i
    return prime_sum

#   test if a number is prime
def prime(number):
    if number == 2 or number == 3: return True
    if number == 4: return False
    for i in range (2, int(sqrt(number) + 1), 1):
        if number % i == 0:
            return False
    return True

#   beginning of code execution
limit = 2000000
answer = sum_of_primes_under(limit)
print("Sum of primes under 2,000,000:", answer)
