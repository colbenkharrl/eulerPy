# Colben Kharrl | December 2016 | Project Euler Problem 3

##
##  Description:
##  The prime factors of 13195 are 5, 7, 13 and 29.
##  What is the largest prime factor of the number 600851475143?
##

#   find largest prime factor
def LPF(number):
    cur_prime = next_prime(1)
    solution = 0
    while not prime(number):
        while number % cur_prime == 0:
            solution = cur_prime
            number = number / cur_prime
        cur_prime = next_prime(cur_prime)
    if number > solution:
        solution = number
    return solution

#   return the next prime number
def next_prime(cur_prime):
    cur_prime += 1
    while not prime(cur_prime):
        cur_prime += 1
    return cur_prime

#   test if a number is prime
def prime(number):
    if number == 2 or number == 3: return True
    if number == 4: return False
    for i in range (2, int(sqrt(number) + 1), 1):
        if number % i == 0:
            return False
    return True

#   beginning of code execution
number = 600851475143
answer = LPF(int(number))
print("Largest prime factor of 600851475143:", answer)
