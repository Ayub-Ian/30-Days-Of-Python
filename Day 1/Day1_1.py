"""
program which will find all such numbers which are divisible by 2
but are not a multiple of 3,
between x and y (both included)

"""


def numCheck(x,y):
    random = range(x,y+1)
    #range of numbers from x as startpoint and y as endpoint
    for i in random:
        #check if number in range is divisible by 2 and not multiple of 3
        if i % 2 == 0 and i % 3 != 0:
            #print numbers separated with a comma
            print(i, end=',')
        

x = int(input("Enter range startpoint:"))
y = int(input("Enter range endpoint:"))
numCheck(x,y)


