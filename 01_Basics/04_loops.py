# loops ->repeatedly

# for loop
# while loop

# for x in range(6):
#   print(x)           
#   0,1,2,3,4,5,

# for x in range(0,11):
#     print(x)
# 0123456789
    
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

# Example
# Increment the sequence with 3 (default is 1):

# for x in range(0, 30, 3):  #(start,end,steps(default(1)))
#   print(x)
# # 0
# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
  
# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# Example
# Print all numbers from 0 to 5, and print a message when the loop has ended:

# for x in range(6):
#   print(x)
# else:
#   print("Khatam tata bye bye")
# 0
# 1
# 2
# 3
# 4
# 5
# Khatam tata bye bye
  

# for x in range(11):
#     for y in range(11):
#         if x==2:
#             print(x,y)
#             break
      

# Nested Loops
# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":

# Example
# Print each adjective for every fruit:

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)


# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content,
#  put in the pass statement to avoid getting an error.

# Example
# for x in [0, 1, 2]:
#   pass


# While loop

# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

# ExampleGet your own Python Server
# Print i as long as i is less than 6:

# i = 1
# while i < 6:
#   print(i)
#   i += 1


# The continue Statement

# With the continue statement we can stop the current iteration, and continue with the next:

# Example
# Continue to the next iteration if i is 3:

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)



# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

# Example
# Print a message once the condition is false:

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")


