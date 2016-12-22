# Colben Kharrl | December 2016 | Project Euler Problem 14

##
##    Description:
##    The following iterative sequence is defined for the set of positive integers:
##        n → n/2 (n is even)
##        n → 3n + 1 (n is odd)
##    Using the rule above and starting with 13, we generate the following sequence:
##        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
##    It can be seen that this sequence (starting at 13 and finishing at 1) contains
##    10 terms. Although it has not been proved yet (Collatz Problem), it is thought
##    that all starting numbers finish at 1.
##    Which starting number, under one million, produces the longest chain?
##

#   beginning of code execution
a = 1
b = 1000000
max_count = 0
value = 0
solutions = []
for i in range(0, b-a):
    base = i
    count = 0
    while base > 1:
        if base < i:
            count = count + solutions[int(base)]
            break
        if base % 2 == 0:
            base = base / 2
        else:
            base = base * 3 + 1
        count = count + 1
    solutions.append(count)
    if solutions[i] > max_count:
        max_count = solutions[i]
        value = i
print("The value with the longest collatz sequence is:", value)
print("The length of the sequence is:", max_count)
