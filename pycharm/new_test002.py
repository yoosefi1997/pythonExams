from email.policy import default
from turtledemo.penrose import start

# x = int(input("enter a score: ".capitalize()))
# if x < 10:
#     print("Rejected!!")
#     print("*"*5)
# else:
#     print("Accepted!")
# print(x < 10)
# ________

# score = float(input("enter your score: ".capitalize()))
# if score <= 20 and score >= 18:
#     print(" your Grade is: A ")
# elif score < 18 and score >= 16:
#     print(" your Grade is: B ")
# elif score < 16 and score >= 14:
#     print(" your Grade is: C ")
# elif score < 14 and score >= 12:
#     print(" your Grade is: D ")
# elif score < 12 and score >= 10:
#     print(" your Grade is: D ")
# elif score < 10 and score >= 9:
#     print(" your Grade is: E ")
# elif score < 9 and score >= 8:
#     print(" your Grade is: E ")
# elif score < 8 and score >= 7:
#     print(" your Grade is: F ")
# elif score < 7 and score >= 5:
#     print(" your Grade is: G ")
# elif score < 5 and score >= 0:
#     print(" your Grade is: H ")
# else:
#     print(" Wrong!! ")
# --------


# score = float(input("enter your score: ".capitalize()))
# if 20 >= score >= 18:
#     print(" your Grade is: A ")
# elif 18 > score >= 16:
#     print(" your Grade is: B ")
# elif 16 > score >= 14:
#     print(" your Grade is: C ")
# elif 14 > score >= 12:
#     print(" your Grade is: D ")
# elif 12 > score >= 10:
#     print(" your Grade is: D ")
# elif 10 > score >= 9:
#     print(" your Grade is: E ")
# elif 9 > score >= 8:
#     print(" your Grade is: E ")
# elif 8 > score >= 7:
#     print(" your Grade is: F ")
# elif 7 > score >= 5:
#     print(" your Grade is: G ")
# elif 5 > score >= 0:
#     print(" your Grade is: H ")
# else:
#     print(" Wrong!! ")

# ------------

# x = float(input("Enter a score: "))
# if x > 10:
#     print("Accepted")
#     if 18 <= x <= 20:
#         print("A")
#     elif 16 <= x <= 18:
#         print("B")
#     elif 14 <= x <= 16:
#         print("C")
#     elif 12 <= x <= 14:
#         print("D")
#     print("Rejected!!")
# else:
#     print("Rejected!!")

# --------------

# x = int(input("enter a number: ".capitalize()))
# if x % 2 == 0:
#     print("عدد زوج")
# else:
#     print("fard!")
# -------------

# x = int(input("Enter a number: "))
# if x % 2 == 0 and x % 5 == 0:
#     print(" Divisible ")
# --------------------------

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# if a == b == c:
#     print(" متساوی الاضلاح ")
# elif a != b != c:
#     print(" مختلف الاضلاع ")
# elif a ** 2 + b ** 2 == c ** 2:
#     print(" قائم الضاویه ")
# elif a == b != c:
#     print(" متساوی الساقین ")
# else:
#     print(" oops! ")
# -----------------------------

# x = 21
# y = 11 + 3 if x < 20 else 5
# print(y)
# -----------------
# x = int(input(" enter number:  "))
# y = int(input(" enter number:  "))
# z = int(input(" enter number:  "))
# if x < y + z and y < x + z and z < x + y:
#     print(" Yes!. ")
#     if x == y == z:
#         print(" متساوی الاضلاع ")
#     if x == y or y == z or z == x:
#         print(" متساوی الساقین ")
#     if x != y != z:
#         print(" مختلف الاضلاع ")
#
#     if x ** 2 == y ** 2 + z ** 2 or y ** 2 == x ** 2 + z ** 2 or z ** 2 == x **2 + y ** 2:
#         print(" قائم الزاویه ")
#
# else:
#     print(" No!! ")

# -------------------------------

# x = input("enter a char: ".capitalize())
# print(x)
# print(ord(x))
# if ord(x) <= 32:
#     print(" Empty!! ")
# if ord(x) == 33 and ord(x) <= 47:
#     print(" Sign ")
# if ord(x) >= 48 and ord(x) <= 57:
#     print(" Numbers ")
# if ord(x) >= 58 and ord(x) <= 64:
#     print(" Sign ")
# if ord(x) >= 65 and ord(x) <= 90:
#     print(" Big english alphabet. ")
# if ord(x) >= 90 and ord(x) <= 96:
#     print(" Sign! ")
# if ord(x) >= 97 and ord(x) <= 122:
#     print(" Small english alphabet. ")
# if ord(x) >= 123 and ord(x) <= 1272:
#     print(" Special english alphabet! ")
# -------------------------

print(min(1,2,12, 13))
print(max(1,2,12, 13))
l = [1,2,12, -1000, 13]
print(min(l, default=1000))
print( min([1,2,12, -1000, 13], default=-1001))
print(min([], default=-1001))

print(min(["aria", "arsin", "arta", "selina"], default="abcd"))
print(min(["zeus", "arsin", "arta", "selina"], default="abcd"))
print(max(["zeus", "arsin", "arta", "selina"], default="abcd"))

print(sum([1,2,12, 1000, 13]))
print(sum([1,2,12, -1000, 13]))
print(sum([1,2,12, 1000, 13], start=10))

# ----------------------------------------------- chapter4 end





