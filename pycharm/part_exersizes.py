

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# min = min(x, y)
# max = max(x, y)
# while min <= max:
#     print(min)
#     min += 1
# --------------    
# for i in range(min, max + 1):
#     print(i)
    
# ------- End ---------

# the Common divisor of two numbers

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# for i in range(1, x + 1):
#     if x % i == 0 and  y % i == 0:
#         print(i, end="  ")
# -----------------

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# m = min(x, y)
# for i in range(1, m + 1):
#     if x % i == 0 and  y % i == 0:
#         print(i, end="  ")
# -----------------

# the bigest common divisor of two numbers

# x = int(input("Enter a number:"))
# y = int(input("Enter a number:"))
# m = min(x, y)
# tmp = 1
# for i in range(1, m + 1):
#     if x % i == 0 and y % i == 0:
#         if i > tmp:
#             tmp = i
# print(tmp)
# -----------------
# the best practice to find bigest common divisor of two numbers 

# x = int(input("Enter a number:  "))
# y = int(input("Enter a number:  "))
# m = min(x,y)
# for i in range(m, 0, -1):
#     if x % i == 0 and y % i == 0:
#         print(i)
#         break
# -----------------

# the last common multiple of two numbers

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# min_ = min(x, y)
# max_ = max(x, y)
# for i in range(1, min_ + 1 ):
#     if (max_ * i) % min_ == 0:
#         print(max_ * i, i, (max_ * i) / min_)
#         break
# -----------------

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# min_ = min(x, y)
# max_ = max(x, y)
# i = max_
# while i % min_ != 0:
#     i += max_
# print(i)
# -----------------

# # the lenght of a number
# x = int(input("Enter a number:"))
# print(len(str(x)))
# -----------------

# x = input("Enter a number:")
# print(len(x))
# -----------------

# x = int(input("Enter a number: "))
# for  i in range(1, len(str(x))+1):
#     print(i)
# -----------------

# x = input("Enter anumber: ")
# for i in range(len(x)+1):
#     print(i)
# -----------------

# x = input("Enter anumber: ")
# for i in range(len(x), 1, -1):
#     print(i)
#     break
# -----------------

# x = int(input("Enter a number: "))
# i = 0
# while x > 0:
#     x //= 10
#     i += 1
#     print(i)
# -----------------

# x  = int(input("Enter a number: "))
# i = 0
# while x > 0:
#     x //= 10
#     i += 1
# print(i)
# -----------------

# star print
# x = int(input("Enter a count of stars:"))
# for i in range(1, x + 1):
#     print(" " * (x - i), end="")
#     print("*" * i)
# -----------------
# x = int(input("Enter a count of stars:  "))
# for i in range(1, x + 1):
#     print("*" * i, end="\n")
# -----------------
# x = int(input("Enter a count of stars: "))
# for i in range(1, x + 1):
#     print(" " * (x - i), end="")
#     for j in range(1 , i + 1):
#         print("*", end="")
#     print()
# -----------------
    
# Guessing a name from a list of tennames
from random import random,  choice
# names = ["Aria", "Arash", "Arta", "Arian",
#          "Armin", "Arman", "Arvin", "Arshia", 
#          "Armita", "Asia"]    
# names_cp = names.copy()
# while True:
#     if len(names_cp) == 0:
#         print("You have guessed all the names.")
#         break
#     choiced_name = choice(names_cp)
#     print(choiced_name)
#     ans = input(" is your guess?(Y/N)")
#     if ans.upper() == "Y":
#         print("You win")
#         break
#     else:
#         names_cp.remove(choiced_name)
# -----------------
# names = ["Aria", "Arash", "Arta", "Arian",
#          "Armin", "Arman", "Arvin", "Arshia",
#          "Armita", "Asia"]
# names_cp = names.copy()
# while len(names_cp) > 0:
#     choiced_name = choice(names_cp)
#     ans = input("Guess the name: ")
#     if ans == choiced_name:
#         print("You win")
#         break
#     else:
#         print(f" The name was {choiced_name} pleaseTry again!")
#         names_cp.remove(choiced_name)
#         if ans == "0" or ans in range(1, 11) and ans != choiced_name:
#             print("you have exited the game!")
#             break
# -----------------


