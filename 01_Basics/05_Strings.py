# print("Hello")
# print('Hello')

# a="hello"
# print(a)

# a="""hellow 
# how are you ?
# Use triple quetes for multi line string"""
# print(a)

# Strings are Arrays
# Square brackets can be used to access elements of the string.



# a="hello"
# print(a[1])      # e

# Looping Through a String

# for x in "banana":
#   print(x)

# a = "Hello, World!"
# print(len(a))


# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

# text="The best thing in life is freedom"
# print("freedom" in text)

# Use it in an if statement:
# life="The best thing in life is freedom"
# if "freedom" in life:
#     print("Yes 'freedom' is present in \
#           life")

# life="The best thing in life is food"
# if "freedom" in life:
#     print("Yes 'freedom' is present in life")
# else:
#     print("No freedom")


# Python - Slicing Strings

# b = "Hello, World!"
# print(b[0:5])   # will not consider end 


# Slice From the Start
# By leaving out the start index, the range will start at the first character:

# Example
# Get the characters from the start to position 5 (not included):

# b = "Hello, World!"
# print(b[:5])

# Slice To the End
# By leaving out the end index, the range will go to the end:

# Example
# Get the characters from position 2, and all the way to the end:

# b = "Hello, World!"
# print(b[7:])

# b = "Hello, World!"
# print(b[:])        # Hello, World!   will give full string


# Negative Indexing
# Use negative indexes to start the slice from the end of the string:

# b = "Hello, World!"
# print(b[-6:-1])
# World               will not include -1 vala part


# Python - Modify Strings

# Upper Case
# Example
# The upper() method returns the string in upper case:

# a='pranav'
# print(a.upper())

#lower case
#Example
# The lower() method returns the string in lower case:

# a="PRANAV"
# print(a.lower())

# Remove Whitespace

# a="       Hellow , World!"
# print(a.strip())
# Hellow , World!


# Replace String
# Example
# The replace() method replaces a string with another string:

# a="Hahahahahah"
# print(a.replace("a","e"))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

# a="Pranav , and , friends"
# print(a.split(","))      

#------------------------------------------

# String Concatenation

a="hello ! "
b="how are tu ?"

# print(a+b)

# c=a+b
# print(c)

# c=a+" "+b
# print(c)

# print(a+" "+b)

#-------------------------------------------------------

# String Format

# The format() method takes the passed arguments, formats them,
#  and places them in the string where the placeholders {} are:

# obj="object"
# name="Pranav"
# age=19
# me="Hello i am {} and my name is {} and i am {} year old"
# print(me.format(obj,name,age))


# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

# obj="object"
# name="Pranav"
# age=19
# me="Hello i am {1} and my name is {0} and i am {2} year old"
# print(me.format(obj,name,age))


# Escape Character

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Escape Characters
# Other escape characters used in Python:

# Code	Result	
# \'	Single Quote	    txt = 'It\'s alright.'
# \\	Backslash	        txt = "This will insert one \\ (backslash)."
# \n	New Line	        txt = "Hello\nWorld!"
# \r	Carriage Return	    txt = "Hello\rWorld!"
# \t	Tab	                txt = "Hello \t World!"

# \b	Backspace	       
 #This example erases one character (backspace):
# txt = "Hello \bWorld!"