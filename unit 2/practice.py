'''
This program calculates the perimeter of a rectangle using input from the user.
'''
#Getting the legth from the user
length = int(input("What is the length of the rectangle?"))
width = int(input("What is the width of the rectangle?"))

perimeter= 2* (length+width)

print ("The perimeter is" + str (perimeter))


x=4
y=2
z=9
sol= z+x*y
print("the answer is" + str(sol))


import math
r= int(input("What is the radius of you circle?"))
c= 2*r*math.pi
a= math.pi*r**2
print("c=",c," a=",a)
