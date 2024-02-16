#Operators

# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

#Arithmatic operators

# a=5
# b=2

# print(a+b)    #7
# print(a-b)    #3
# print(a*b)    #10
# print(a/b)    #2.5
# print(a**b)   #25
# print(a%b)    #1
# print(a//b)   #2   gives integer - floor division

#Assignment Operator

# c=10
# c+=5  #c=c+5
# print(c)   #c=15


# Operator	     Example	           Same As
# =	                   x = 5	               x = 5	
# +=	               x += 3	               x = x + 3	
# -=	               x -= 3	               x = x - 3	
# *=	               x *= 3	               x = x * 3	
# /=	               x /= 3	               x = x / 3	
# %=	               x %= 3	               x = x % 3	
# //=	               x //= 3	               x = x // 3	
# **=	               x **= 3	               x = x ** 3

# # relational / comparision operator

# Operator	  Name	                        Example
# ==	          Equal	                        x == y	
# !=	          Not equal	                    x != y	
# >	          Greater than	                x > y	
# <	          Less than                    	x < y	
# >=	          Greater than or equal to	    x >= y	
# <=	          Less than or equal to      	x <= y


# ab=10
# cd=20
# print(ab>cd)
# print(ab<cd)
# print(ab>=cd)
# print(ab<=cd)
# print(ab==cd)
# print(ab!=cd)



# Logocal operator
#and,or,not

# Logical operators are used to combine conditional statements:

# Operator	            Description	                                Example
# and 	Returns True if both statements are true	                x < 5 and  x < 10	
# or	Returns True if one of the statements is true	            x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# a,b,c=10,20,30  #shoercut

# print((a>b)and(b<c))     #False

# print((a>b)or(b<c))      #True

# print(not(a>b)or(b<c))   # True



#Identity operator

# is 	Returns True if both variables are the same object	x is y

# is not	Returns True if both variables are not the same object	x is not y

# pranav=10
# vibhu=10

# print(pranav is vibhu)
# print(not pranav is vibhu)


#Membership Operator


# Operator	                   Description	                                                              Example 
# in              	Returns True if a sequence with the specified value is present in the object	      x in y	
# not in	        Returns True if a sequence with the specified value is not present in the object	  x not in y

# a=[1,2,3,4,5]
# b=2
# print(b in a)       #True
# print(b not in a)   #False

a= input("Enter the number :")    #take input as string
print(a*2)    #aa

b=int(input("Enter the number :"))
print(float(b*2))   #b*2


