"""  
program which can compute the factorial of a given numbers.
 
"""

num = int(input("Enter a positive integer:"))
fact = 1

if num == 0 or num == 1:
    print("Factorial is 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
        print(fact, end=",")


