# def x(a):
#     a += 2
#     return a
# x(5)
# print(x(5))
# n = x(10)
# print(n)
# m = x
# print(m(5))
# --------------
# def y():
#     print("Hello")
#     return "World"
# y()
# print(y())
# --------------
# def z():
#     return 5
# z()
# print(z())
# -------------
# def a():
#     print("Hello ARIA")
#     x = 5; y = 10;  x + y
    
# a()
# print(a())
# ------------
# def b():
#     print("Hello ARIA")
#     x = 5; y = 10; return x + y
# b()
# print(b())
# ------------

# def f(x):
#     return x ** 3
# y = int(input("Enter a number: "))
# n = f(y)
# print(" The cube of ", y, " is ", n)
# ------------


# Examples for function
# The repeated digit:
 
# def repeated_digit(number, digit):
#     count = 0
#     while number > 0:
#         if number % 10 == digit:
#             count += 1
#         number //= 10
#     return count

# x = int(input("Enter a number:"))
# y = int(input("Enter your digit: "))
# print(" The digit", y, " is repeated", repeated_digit(x, y),\
#     "times in the number", x)
# ------------
# def repeated_digit(number, digit):
#     return str(number).count(str(digit))
# x = int(input("Enter a number: "))
# y = int(input("Your digit: "))
# print("The digit", y, " is repeated", repeated_digit(x,\
#     y), "times in the number", x)
# ------------

# The sum of numbers factorial:
"""
 we most divide this operation into two parts:
 1 - find the factorial of a number
 2 - find the sum of the digits of the factorial
For example, if the number is 5, the factorial is 120 and the
sum of the digits is faact1 + fact2 + fact3 + fact4 + fact5 
fact1 = 1 + fact2 = 2 + fact3 = 6 + fact4 = 24 + fact5 = 120 ->
1 + 2 + 6 + 24 + 120 = 153.
every part is a function and we will call them. 
they're names are fact and sum_fact. part 1 is fact function and
part 2 is sum_fact. because we most do everything in just one function.

  
"""
# def fact(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f
# # print(fact(5))
# def sum_fact(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += fact(i)
#     return total
# x = int(input("Enter a number: "))
# y = sum_fact(x)
# print("The sum of the factorials of the numbers from 1 to", x, " is:", y)
# ------------

# def fact(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f
# def sum_fact(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += fact(i)
#     return total
# x = int(input("Enter a number: "))
# print("The factorial of ", x, " is: ", fact(x))
# print("The sum of the factorial from 1 to", x, " is: ", sum_fact(x))
# ------------

# def fact(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     print("The factorial of ", i, " is:", f)
#     return f

# def sum_fact(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += fact(i)
#     return total    

# x = int(input("Enter a number: "))
# y = fact(x)
# z = sum_fact(x)
# print("\n The factorial of ", x, " is: ", y)
# print("The sum of the factorials is :", z)
# ------------

# The maximum of three numbers:

# def max3(a, b, c):
#     if  a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# z = int(input("Enter the third number: "))
# print("The maximum of the three numbers is: ", max3(x, y, z))
# ------------

# def max3():
#     x = int(input("Enter the number1: "))
#     y = int(input("Enter the number2: "))
#     z = int(input("Enter the number3: "))
#     if x >= y and x >= z:
#         return x
#     elif y >= x and y >= z:
#         return y
#     else:
#         return z
# print("The maximum of the three numbers is: ", max3())
# ------------

# def max3():
#     x = int(input("Enter the number-1: "))
#     y = int(input("Enter the number-2: "))
#     z = int(input("Enter the number-3: "))
#     if x >= y and x >= z:
#         print("the maximum is", x)
#     elif y >= x and y >= z:
#         print("The maximum is", y)
#     else:
#         print("The maximum is", z)

# max3()
# max3()
# -------------









        
        
        
        
        




