# Colben Kharrl | December 2016 | Project Euler Problem 4

##
##  Description:
##  A palindromic number reads the same both ways. The largest palindrome made
##  from the product of two 2-digit numbers is 9009 = 91 × 99.
##  Find the largest palindrome made from the product of two 3-digit numbers.
##

#   test if string is palindrome
def is_palindrome(string):
    end = len(string) - 1
    beg = 0
    while end >= beg:
        if string[beg] != string[end]:
            return False
        beg += 1
        end -= 1
    return True

#   calculate all products and test for palindrome
def largest_palindrome(digits):
    solution = 0
    operand_limit = pow(10, digits)
    for i in range(operand_limit):
        for j in range(operand_limit):
            if is_palindrome(str(i * j)):
                if (i * j) > solution:
                    solution = i * j
    return solution

#   beginning of code execution
digits = 3
answer = largest_palindrome(digits)
print("Largest palindrome from multiples of 3 digit numbers:", answer)
