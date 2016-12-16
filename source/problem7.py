# Colben Kharrl | December 2016 | Project Euler Problem 7

##
##  Description:
##  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
##  that the 6th prime is 13.
##  What is the 10 001st prime number?
##

#   find prime at index
def prime_at_index(index):
    index_iter = 1
    prime_iter = 2
    while True:
        if index_iter == index:
            return prime_iter
        prime_iter = next_prime(prime_iter)
        index_iter += 1
        
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
index = 10001
answer = prime_at_index(index)
print("Prime number at index 10,001:", answer)
