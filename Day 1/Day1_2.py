"""
Find the number of elements in a list.
Eg., l = [1, 2, 3, 4] 
Number of elements in [1,2,3,4]: 4

"""

def length(L):
    counter = 0
    for i in L:
        counter += 1

    return counter

userList = []

x = input("Enter numbers separated by commas:")
userInput = x.split(",")

for i in userInput:
    integer = int(i)
    userList.append(integer)

print(userList)
print("Number of elements on list:", length(userList))