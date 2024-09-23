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
r= int(input("What is the radius of your circle?"))
c= 2*r*math.pi
a= math.pi*r**2
print("c=",c," a=",a)


import math
r= float(input("What is the radius of your circle?"))
h= int(input("What is the height of your circle?"))
c= 2*r*math.pi
a= math.pi*r**2*h
print("c=",c," a=",a)

import math
name = input("What is your name?")
a = int(input("What is a?"))
b = int(input("What is b?"))
c = int(input("What is c?"))
quad = (b**2-4*a*c)
posX = (-b+math.sqrt(quad))/(2*a)
negX = (-b-math.sqrt(quad))/(2*a)


print(posX)
print(negX)
