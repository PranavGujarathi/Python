
# interactive mode
# script mode

# string = 'my name is pranav \
#         i live in bombay  \n \
#         my hobby is to do coding \n \
#         how are you \n \
#         what is your name'

# string = 'my name is pranav \t i live in bombay  \t my hobby is to do coding'/

string = "Helllo how are you"

print(string,"Janak",sep="\n")


a =10  #a is variable containg 10
b=20
# is 10 greater than 20
# 10>20 return False

c= a+b
print(c)


# print(a,b,aug="27")


string = "Pranav"
decimal_marks = 100.233   #float
boolean_var1 = True
boolean_var2 = False
none_var = None
print(boolean_var1)
print(10<20)

#Variable naming
# alphabats, numbers, and _
# $ $#@$ use nhhi kar sakthe
# 12pranav = 10 -- error
# python is case sensitive

A =10
a=20
print(1.0e4)  #1.0 X 10^4

print(2 + 10j)
print("the type of given value is ",type(None))



# DYNAMIC TYPING
a="hello everyone"
print(a)
a=30
print(a)

true = 10



a=10
b=a
print("berfore updating b ",a,b)
a=30
print(a,b)

a = [1,2,3]
b=a
print(a,b)
a[0] = 10  #mutable
print(a,b)

# s = "Pranav"   #non mutable
# s[1] = "t"



""""For
 multi line 
comments """



'''
single 
quets also can be used 
3 times
'''


s = "Pranav\"s car"
print(s)

# Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)



# Global Variables

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

# Example	Data Type	Try it

x = str("Hello World")	      #  str	
x = int(20)	                  #  int	
x = float(20.5)         	 #  float	
x = complex(1j)	              #complex	

x = list(("apple", "banana", "cherry"))	       #   list	
x = tuple(("apple", "banana", "cherry"))	    #  tuple	
x = range(6)	                                 # range

x = dict(name="John", age=36)	                #   dict	
x = set(("apple", "banana", "cherry"))          #  	set	
x = frozenset(("apple", "banana", "cherry"))	# frozenset	

x = bool(5)                  # bool	
x = bytes(5)	             # bytes	
x = bytearray(5)        	 #bytearray	
x = memoryview(bytes(5))	 #memoryview	


# Python Casting
# Specify a Variable Type


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3



x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'




