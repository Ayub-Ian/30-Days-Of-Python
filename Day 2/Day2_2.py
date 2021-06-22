import math

#get input
userInput=input("Input number: ")
userInput=int(userInput)

#create a function that returns the factorial of a number

def factorial(n):
    while n%2==0:
        print (2,end=",")
        n=n/2

    for i in range(3,int(math.sqrt(n)+1),2):
        while n% i==0:
            print (i,end=",")
            n=n/i

    if n>2:
        print(n)


print(factorial(userInput))