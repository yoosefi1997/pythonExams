# word = 0
# while word <= 10:
#     print("Aria")
#     word += 1
# print("-"*20)
from operator import truediv
from os.path import split

# ------------------

# x = 0
# while x < 100:
#     print(x % 2 ==0, x)
#     x +=2
# print("End!")
# ----------------

# x = 0
# while x < 100:
#     if x % 2 == 0:
#         print(x, x % 2 == 0)
#     x +=1
# print("End!")
# --------------------

# x = int(input("enter a number: ".capitalize()))
# while x < 100:
#     if x % 2 == 0:
#         print(x, x % 2 == 0)
#     x +=1
# print("End!")

# -------------------

# x = 1
# y = int(input("Enter a number: "))
# while x <= y:
#     print("*" * y)
#     x += 1
# ------------------

# x = int(input("Enter a number: "))
# y = 1
# while x >= y:
#     print("*" * x)
#     x += -1
# ---------------

# x = int(input("Enter a number: "))
# y = 1
# while x >= y:
#     print("*" * x)
#     x -= 1
# ------------------

# x =1
# xi = int(input("Enter a number: "))
# while x <= xi:
#     print("*" * xi)
#     x += 1
#
#
# y = int(input("Enter a number: "))
# while y >= 1:
#     print("*" * y)
#     y -= 1
# ------------------

# n = int(input("enter a number: ".capitalize()))
# while n <= 100:
#     if n % 3 == 0 and n % 7 == 0:
#         print(n)
#     n += 1
# print("-" * 20, "End1")
# -----------------
# n = int(input("enter a number: ".capitalize()))
# while n <= 1000:
#     if n % 3 == 0 and n % 7 == 0:
#         print(n)
#     n += 1
# print("-" * 20, "End1")

# ---------------

# i = 1
# j = int(input("Enter a number: "))
# while i <= j:
#     if j % i == 0:
#         print(i,end=" ")
#     i += 1
# print("\n","-" * 20)
# -------------------

# i = 1
# j = int(input("Enter a number: "))
# l = []
# while i <= j:
#     if j % i == 0:
#         l.append(i)
#     i += 1
# print(l)
# print("\n","-" * 20)
# -------------------------

# n = int(input("enter a number:".capitalize()))
# i = 1
# l = []
# while i <= n:
#     if n % i == 0:
#         print(i, end=" ")
#         l.append(i)
#     i += 1
# print("\n",l)
# print("-"*20)
# ---------------------

# n = int(input("enter a number:".capitalize()))
# i = 1
# l = []
# while i <= n:
#     if n % i == 0:
#         print(i, end=" ")
#         l.append(i)
#     i += 1
# print("\n","Divisor: ",l,"\n","Sum of Number's Digits: ", sum(l)-n,"Is it complete? ", sum(l)-n == n)
# print("-"*20)
# --------------------

# n = int(input("enter a number:".capitalize()))
# i = 1
# l = []
# while i <= n:
#     if n % i == 0:
#         l.append(i)
#     i += 1
# print("Divisors: ",l,"\n","Sum of Number's Digits: ", sum(l)-n,"\nIs it complete? ", sum(l)-n == n)
# print("-"*20)
# -----------------------

# n = int(input("enter a number:".capitalize()))
# i = 1
# l = []
# while i <= n:
#     if n % i == 0:
#         l.append(i)
#     i += 1
# print("Divisors: ",l,"\n","Sum of Number's Digits: ", sum(l)-n)
# if sum(l)-n == n:
#     print("it's Complete.")
# else:
#     print(" No complete! ")
# print("-"*20)
# --------------------------

# n = int(input("enter a number:".capitalize()))
# i = 1
# c = 0
# while i < n:
#     if n % i == 0:
#         c += i
#         print(i, end=" ")
#     i += 1
# if c == n:
#     print(f" it's Complete: {c} ")
# else:
#     print(" No complete! ")
# print("-"*20)
# ---------------------

# i = 1
# a, b = 0, 1
# while i <= 5:
#     print(b)
#     a,b = b, a+ b
#     i += 1
# print("End!")
# -------------------

# n = int(input("enter a number:".capitalize()))
# i = 1
# a, b = 0, 1
# while i <= n:
#     print(b)
#     a,b = b, a + b
#     i += 1
# print(F" Length of last Number: {len(str(b))} ")
# print(" FIBONACCI End!")
# ----------------

# i = 1
# n = int(input("Enter a number:"))
# a, b = 1, 2
# l = []
# while i <= n:
#     a,b = b, a * b
#     l.append(b)
#
#     i += 1
# print(l)
# print(sum(l))
# print(len(str(sum(l))))
# ------------

# f = int(input("Enter a number:"))
# print(f * (f - 1))
# ----------------

# i = 1
# n = int(input("Enter a number:"))
# a,b = 0,1
# while i <= n:
#     print(b)
#     a,b = b, a+b
#     i += 1
# print("-"*20,"End")

# --------------------

# i = 1
# while i <= 100:
#     print(i)
#     if i == 5:
#         break
#     i += 1
# print("+"*15)
# ----------------

# n = float(input("enter a number".capitalize()))
# n1 = 0
# while True:
#     n1 += n
#     s = input("?")
#     if s.lower() == "yes":
#         print(n1)
#         n = float(input("enter a number".capitalize()))
#     else:
#         break
# print(n1)
# ---------------

# n = float(input("Enter a number: "))
# m = n
# while True:
#     print(m)
#     s = input("?")
#     if s.lower() == "yes":
#         print(m)
#         n = float(input("Enter a number: "))
#         if n < m:
#             m = n
#             print(m)
#     else:
#         break
# print(m)
# --------------------
#
# m = float("inf")
# n = float(input("Enter a number: "))
# while True:
#     if n < m:
#         m = n
#         print(m)
#     s = input("?")
#     if s.lower() == "yes":
#         n = float(input("Enter a number: "))
#     else:
#         break
# print(m)
# -----------------

# m = float("inf")
# n = float(input("Enter a number: "))
# while True:
#     if n < m:
#         m = n
#         print(m)
#     s = input("?")
#     if s.lower() == "no":
#         break
# print(m)
# ---------------

# m = float("inf")
# while True:
#     n = float(input("Enter a number: "))
#     if n < m:
#         m = n
#     s = input("?")
#     if s.lower() == "no":
#         break
# print(m)
# ----------------

# i = 0
# while i < 10:
#     i += 1
#     if i % 3 == 0:
#         continue
#     print(i)
# ----------------------

# i = 0
# while i < 10:
#     i += 1
#     if i % 3 == 0:
#         continue
#     print(i)
# else:
#     print("  Ok!")
# -----------------

# i = 0
# while i < 10:
#     i += 1
#     if i % 3 == 0:
#         break
#     print(i)
# else:
#     print("  Ok!")
# ----------------------

# i = 2
# n = int(input("enter a number: ".capitalize()))
# if i > 1:
#     while i < n:
#         if n % i == 0:
#             print(n, " is'nt a prime number! ")
#             break
#         i += 1
#     else:
#         print(n, " is a prime number ")
# else:
#     print(n, " is'nt a prime number! ")
# --------------------

# i = 2
# n = int(input("enter a number: ".capitalize()))
# if i > 1:
#     while i < (n // 2)+1:
#         if n % i == 0:
#             print(n, " is'nt a prime number! ")
#             break
#         i += 1
#     else:
#         print(n, " is a prime number ")
# else:
#     print(n, " is'nt a prime number! ")
# ------------------

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(f"  {j} ")
#         j += 1
#     print(i)
#     i += 1
# ---------------

# i = 1
# while i <= 10:
#     print(i)
#     j = 1
#     while j <= 10:
#         print(f"  {j} ")
#         j += 1
#     i += 1
# ---------------

# i = 1
# while i <= 10:
#     print(i)
#     j = 1
#     while j <= 10:
#         print(f"  {j} ")
#         j += 1
#     i += 1
# print("****","I: ", i)
# print("_"*20,"End")
# -------------

# l = ["aria","arsin","aron","arta","arad","artin"]
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1
# ------------------

# l = ["aria","arsin","aron","arta","arad","artin"]
# i = 0
# while i < len(l):
#     print(l[i])
#     s = l[i]
#     j = 0
#     while j < len(s):
#         if j % 2 == 0:
#             print(s[j].upper(),end="")
#         else:
#             print(s[j], end="")
#         j += 1
#     print()
#     i += 1
# --------------------------

# l = ["aria","arsin","aron","arta","arad","artin"]
# i = 0
# while i < len(l):
#     print(l[i])
#     j = 0
#     while j < len(l[i]):
#         if j % 2 == 0:
#             print(l[i][j].upper(), end="")
#         else:
#             print(l[i][j], end="")
#         j += 1
#     print()
#     i += 1
# ------------------

# l = ["aria","arsin","aron","arta","arad","artin"]
# i = 0
# while i < len(l):
#     j = 0
#     while j < len(l[i]):
#         if j % 2 == 0:
#             print(l[i][j].upper(), end="")
#         else:
#             print(l[i][j], end="")
#         j += 1
#     print()
#     i += 1
# -----------------------

# l = input("enter a list of names:".capitalize()).split("-")
# i = 0
# while i < len(l):
#     j = 0
#     while j < len(l[i]):
#         if j % 2 == 0:
#             print(l[i][j].upper(), end="")
#         else:
#             print(l[i][j], end="")
#         j += 1
#     print()
#     i += 1
# ------------------------

# i = 0
# while i <= 10:
#     j = 0
#     while j <= 10:
#         print(i*j)
#         j += 1
#     i += 1
# --------

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i*j, end="\t")
#         j += 1
#     i += 1
# -----------------------

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i*j)
#         j += 1
#     i += 1



# table = [[1]*10 for _ in range(10)]
#
# for num1 in range(1, 11):
#     for num2 in range(1, 11):
#        table[num1-1][num2-1] = num1*num2
#
# for row in table:
#     print(row)
# an example from internet for multiply table in Python.
# -----------

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i * j, end="\t")
#         j += 1
#     print()
#     i += 1

# -------------------

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i * j, end="\t")
#         j += 1
#     print()
#     i += 1

# -----------------------

# i = 1
# while i <= 50:
#     print("*" * i)
#     i += 1
# ------------------------------------

# i = 1
# while i <= 20:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j +=1
#     print()
#     i += 1
# --------------------------
# for Loop

# names = ["Aria","Aria","Ariaz","Aria","Aria","Aria","Aria","Aria"]
# for i in names:
#     print("-" * 10)
#     print(i)
# ----------------
# # aski code
# aski_code = [121, 112, 65, 76, 87, 92]
# for i in aski_code:
#     print(chr(i))
# ------------------------

# -------------

# Nested FOR loo[
# l1 = [1,2,4, 5,12,3, 7 , 9]
# l2 = [1,2,3,5,7, 11, 13]
# for i in l1:
#     for j in l2:
#         if  i == j:
#             print(i)
# ---------------------------

# s1 = {1,2,4,5,9, 11, 13, 9}
# s2 = {2,4,6,8, 13,11, 9, 2}
# for  i in s1:
#     for j in  s2:
#         if i == j:
#             print(i)
# ------------------

# s1 = {1,2,3,5,7, 11,99,2}
# s2 = {2,4,6,5,8, 11, 9, 9}
# for i in s1:
#     if i in s2:
#         print(i)

# --------------------------

# a, b, c = [1, 2, 3]
# print(a,b,c, end="\t")
# ----------------------

# a, *b, c = [1, 2, 3,"Aria", 29, "AI", 25]
# print(a,"\n",b,"\n",c)
# ----------------------------

# for a,b,c in [[1,2,3],[4,5,6,],[7,8,9]]:
#     print(a,"\t", b, "\t", c)
# -------------------------

# list = {97, 87, 77, 65, 112}
# for c in list:
#     print("Aria" * 100)
#     print(chr(c))
# ----------------------

# a = [1,2,5,12,4,7, 200]
# b = [1,2,5,121, 200, 14]
# for i in a:
#     for j  in b:
#         if(i == j):
#             print(i)
#  ---------------------------
# a = [1,2,3,25,100]
# b = [1,2,3,14, 200]
# for i in a:
#     if i in b:
#         print(i)

# a, b, c = 2, 4,6
# print(a)
# print(b)
# print(c)
# --------------------
# a, *b, c = 1, 2, 3, 45, 5, 6
# print(a)
# print(b)
# print(c)
# ------------------
# for a in [[1,2,3], [4,5,6], [7,8, 9]]:
# #     print(a)
# for a, *b, c in [[11, 12,55,  13], [14, 15, 16], [21, 22, 23]]:
#         print(a, b, c)
#         print("*" *5)
# # ------------------------
# for a, *b, c in [[1,2,3, 5], [11, 22, 33], [111, 222, 333, 6], [23, 34, 45]]:
#     print(a)
#     print(b)
#     print(c)
#     print("-" *20)
# --------------

# d = {"a": 1, "b": 2, "c": 3}
# for key, value in d.items():
#     print(key, ":", value)
#     ----------
# d = {"a": "Aria", "b": "Arezo", "c": "Aramesh"}
# for key in d.keys():
#     print("Keys: ", key, "\n")
# ------------------
# d = {"a": "Aria","a": "Aria","b": "Afarinesh","c": "Azita","d": "Aramesh","e": "Atusa",}
# for value in d.values():
#     print("value: ", value)
#     ----------------


# range in FOR Loop

# print(range(10))
# print(type(range(10)))
# print("List of range(10) numbers", list(range(10)))
#
# x = list(range(10))
# print("list X: ",x)

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end="\t")
#     print()

# for i in range(2, 11):
#     if i % 2 == 0:
#         print(i, end="\n")

# for i in range(1, 15):
#     if i % 3 == 0 and i < 10:
#         print(i)

# i = int(input(" enter a number ".capitalize()))
# for x in range(0, i):
#     if x % 2 == 0 and x <= 20:
#         print(x)













































































