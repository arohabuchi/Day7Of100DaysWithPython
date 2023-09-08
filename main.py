##################################### DAY 7 #############################################
####################################### Simple mathematical operaion ################################################

################## Division #################
a,b,c,d=2,3,4,7
x=b/a
print(x)
#floor division
y=b//a
print(y)

#modulus division
z=b%a
print(z)

############### Addition #################
a,b,c=2,3,4
x=a+b+c
print(x)
a+=c
print(a)

#Note: + is also use for concatenation of string, list and turple
x2 ="first name "+" Last name"
print(x2)
x22= [1,2,3]+[7,8,9]
print(x22)

##################### Exponentiation #######################
a,b=2,3
x= a**b
print(x)
# using built in pow method
xx = pow(2, 3)
print(xx)

############## Intro to math module ##################
import math
c=30
x=math.sqrt(c)
print(x)
################ Trig function : this is in math module ############
xx=math.sin(c)
# math.cos(c)
# math.acosh(c)
print(xx)

#we also have log in the maths module
math.log(30)
#log in other bases
t=math.log2(30)
print(t)

# we also have operator like multiplication and subtraction, bitwise  and boolean operators
#operator precedence
# PEMDAS=>Perenthesis, Exponential,Multiplication Division, Addition Subtraction

