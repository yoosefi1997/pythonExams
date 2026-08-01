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

# The maximum of three number by max() method:

# def max44(a, b, c):

#     return max(a, b, c)


# x = int(input("Enter the number-1:"))
# y = int(input("Enter the number-1:"))
# z = int(input("Enter the number-1:"))
# print(" the Maximum of this three number is: ", max44(x, y, z))
# ----------

# def max55(x, y, z):
#     return max(x, y, z)

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# n = max55(a, b, c)
# print("\n The maximum number is: ", n)
# -------------

# argumant syntax:
# Normal:

# def max66(a, b, c):
#     print(max(a, b, c))

# max66(2, 3, 5)
# max66(a=5, b=3, c=2)
# --------------
# Name = value:

# def func77(a, b, c):
#     print("A : ", a)
#     print("B : ", b)
#     print("c : ", c)

# func77(c = 5, a = 1, b = 2)
# ------------
# Normal + Name = value(Combinen):

# def func78(a, b, c):
#     print("A : ", a)
#     print("B : ", b)
#     print("c : ", c)

# func78(1, 2, c = 5)
# print()
# func78(2, b = 5, c = 1)
# print()
# func78(3, c = 5, b = 2)
# ----------------
# *Iterable(str, tuple, list, set ,....) 

# def func79(x, y, z):
#     print("X : ", x)
#     print("y : ", y)
#     print("z : ", z)

# f = func79
# f(*[1, 2, 3])
# print()
# l = [2, 4, 6]
# f(*l)
# -------------
# **Dict:

# def func80(a, b, c):
#     print("A : ", a)
#     print("B : ", b)
#     print("C : ", c)

# d = {"a": 2, "b": 5, "c": 9}
# func80(**d)
# print()
# d = {"b": 2, "a": 5, "c": 9}
# f = func80
# f(**d)
# ----------------

# parametter syntax:
# Normal syntax:
# def funcc(a, b, c):
#     print("A -", a)
#     print("B -", b)
#     print("C -", c)
#     print(a + b + c)

# f = funcc
# f(1, 3, 5)
# ----------

# Default syntax
# def funcc(a = 2, b = 6, c = 8):
#     print("A -", a)
#     print("B -", b)
#     print("C -", c)
#     print(f"A : {a} + B : {b} + C : {c}  = {a + b + c}")

# funcc() 
# print()

# funcc(1,2,3)
# print()

# funcc(-2,3)
# print()

# funcc(4)
# print()

# funcc(c = 7)
# print()

# funcc(a = 6, b = 5)
# --------------

# Normal syntx + Default syntax(Combine syntax):

# def funcc(a, b, c = 5):
#     print(f" A : {a} \n B : {b} \n C :  {c} ")
#     print(f" A : {a} * B : {b} * C :  {c}  = {a * b * c}")

# funcc(1, 2, 3)
# print()

# funcc(1, 3)
# print()

# funcc(a = 5, b = 6)
# print()

# funcc(5, b = 2)
# print()

# funcc(a = 6, b = 7, c = 9)
# print()
# ---------------

# * starName syntax:

# def funcc(a, b, *c):
#     print(f" A: {a} + B: {b} + C: {c}  ")
    
# funcc(2, 3, 4, 5)
# ------------

# starName: Normal + Stared + Name_value
# def  funcc(a, b, *c, d):
#     print(f" A: {a} B: {b} C: {c} D: {d} ")

# funcc(2, 4, 5, 7, 8, 3, d = 10)
# -------------

# Normal + Default + nameValue + * starName 

# Normal + Default value + * Star name + Dictionary value + Name value

# def funcc(a, b = 5, *c, **d):
#     print(f" A: {a}\n B: {b}\n C: {c}\n D: {d} ")

# f = funcc
# f(2, 3, 4, 5, 6, 7, c = 8, d = 9)

# -------------

# Parameter pointers:
# parameter - * star:

# def xfunc(a, *,  b, c):
#     print(f" A: {a}\n B: {b}\n C: {c} ")

# xfunc(1,b =2, c =3)
# ------------

# Parameter - / slash:
""" in this condition we most use Normal value argumant from first to
    before '/' simbol.
"""

# def xfunc(a, b, c, /, d):
#     print(f" A: {a}\n B: {b}\n C: {c}\n D: {d} ")

# x = xfunc
# x(1, 2, 3, d = 4)
# --------

# / Slash + * Star parameters

# def xfunc(a, b, /, c, d, *, e, f):
#     print(f" A: {a}\n B: {b}\n C: {c}\n D: {d}\n E: {e}\n F: {f} ")

# n = xfunc
# n(1, 2, 3, 4, e = 5, f = 6)
# ------------

# Docstring(Documentation string ):

# def max3(a, b, c):
#     """
#       Return the Maximum number of three entered numbers.

#       Parameters: (a, b, c)
#       Rturns: max(a, b, c)
#       inputs: 
#         name of input variabless: x, y, z
#         types: (int)
       
#         """

#     return max(a, b, c)

# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# z = int(input("Enter the third number: "))

# m = max3
# print("The maximum number is: ", m(x, y, z))
# print("The Docstring of max3 is: \n", m.__doc__ )
# print("The help contex of MAX3 function is: \n ", help(m))
# ----------------

# # Function annotations:

# def funcc(a:int, b:int, c:int) -> list :
#     """
#         Show the three numbers.
#     """

#     print("\nA: \t", a)
#     print("B: \t", b)
#     print("C: \t", c)

#     return a + b + c, a, b, c

# print(funcc(1, 2, 3))
# print(funcc.__annotations__)
# --------------

# def sumFuncc(x: int, y: int, z: int = 10) -> list:
#     """
#     Sum of three numbers:
#     """

#     print(f"X: {x}\t Y: {y}\t Z: {z}\n")


#     return x + y + z, x, y, z

# print(sumFuncc(1,2))
# print(sumFuncc.__annotations__)

# ---------------

# firstClass functions:
"""
    The first class functions include types bellow:
        1 - can be created at runtime.
        2 - can be assigned to a variable
        3 - can be passed as an argumant to a function.
        4 - can be return as a result from a function.
        5 - can have properties and methods.
    however all functions in python are firstClass. because you can use
    they for every ting and every condition.    
"""
# 1 - can be created at runtime:

# x = True
# if x:
#     def funcc(a):
#         print(a+2)

# funcc(5)

# x = False
# if x:
#     def funccc(a):
#         print(a + 2)

# funccc(5)
# ------------

# def func_a(x):
#     print(x)
#     def func_b(y):
#         print(y * 2)
#     func_b(x)

# func_a(5)
# ------

# 2 - can be assigned to a varable:

# def pow_func(a):
#     print(a ** 2)

# p_f = pow_func
# p_f(5)
# ---------------

# 3 - can be passed as an argumant to a function:

# def descending(mylist):
#     print(sorted(mylist))
# def ascending(mylist):
#     print(sorted(mylist, reverse= True))

# def sorting_func(f, sortedList):
#     f(sortedList)
# sorting_func(descending, [2, 4, 6, 2, 1, 6, 7, 5, 12, 43])
# sorting_func(ascending, [1, 5, 6, 7, 9, 24, 12, 8])

# 4 - can be return as a result from a function:

# def mysort(s):


#     def descending(mylist):
#         print(sorted(mylist))

#     def ascending(mylist):
#         print(sorted(mylist, reverse= True))

#     def errorx(eror):
#         print("Eror!")

#     if s == "a":
#         return ascending
#     elif s == "d":
#         return descending
#     else:
#         return errorx

# actionx = input("Action: ")
# funcx = mysort(actionx)
# funcx([1, 4, 6, 7, 12, 54, 76, 21, 3])
# 5 - can be have properties nad methods:
# print(funcx.__name__)

# -----------

# Examples for firstClass functions:
# 1 - can be created at runtime

# x = True
# if x:
#     def funcc(a):
#         print(a+2)

# funcc(5)
# ----------

# user_types = ["1 -vip", "2 -gold", "3 - silver", "4 - bronze"]
# print("The users include, ", ", ".join(user_types) )
# search_user = input("Enter a type of users(with his numbers): ")

# if search_user == "1":
#     def user_price(price):
#         """
#         This is a function for calculate price.
#         """

#         return price * 0.0
#     print("$",user_price(5000))
# elif search_user == "2":
#         def user_price(price):
#                 """
#                 This a function for calculate price.
#                 """
        
#                 return price * 0.5
#         print("$",user_price(5000))

# elif search_user == "3":
#       def user_price(price):
#               """
#               This a function for calculate price.
#               """
      
#               return price * 1.25
#       print("$",user_price(5000))
      
# elif search_user == "4":
#       def user_price(price):
#               """
#               This a function for calculate price.
#               """
      
#               return price * 1.75
#       print("$",user_price(5000))

# else:
#        def user_price(price):
#                """
#                This a function for calculate price. """
               
#                return "User type not found!"

# """ we can show the result of function that do calculatate 
# out of "if|elif". for example, in bellow:"""
# result = user_price(5000)
# print("$", result)
# --------------

# user_types = ["1 -vip", "2 -gold", "3 - silver", "4 - bronze"]
# print("The users include, ", ", ".join(user_types) )
# search_user = input("Enter a type of users(with his numbers): ")

# if search_user == "1":
#     def user_price(price):
#         """
#         This is a function for calculate price.
#         """

#         return price * 0.0

# elif search_user == "2":
#     def user_price(price):
#         """
#             This a function for calculate price """
        
#         return price * 0.5

# elif search_user == "3":
#     def user_price(price):
#         """
#             This a function for calculate price."""
      
#         return price * 1.25
      
# elif search_user == "4":
#     def user_price(price):
#         """
#             This a function for calculate price."""
      
#         return price * 1.75
      
# else:
#     def user_price(price):
#         """ This a function for calculate price. """
               
#         return "User type not found!"

# result = user_price(5000)
# print("$", result)

# -------

# 2 - can be assigned to a variable:

# def multiply_x(number):

#     return number * 2

# doublex = multiply_x
# print(doublex(5))
# ------------

# 3 - can be passed as an argumant to a function

# def upper_tex(text):

#     return text.upper()

# def lower_text(text):

#     return text.lower()

# def processed_mesage(processFunc, message):

#     return processFunc(message)

# result1 = processed_mesage(upper_tex, "Hi, i'm aria")
# print(result1)

# result2 = processed_mesage(lower_text, "Hi, i'm ARIA")
# print(result2)
# ----------------

# def is_even(number):

#     return number % 2 == 0

# def is_greater_than10(number):

#     return number > 10

# def custom_filter(condition_func, numbersList):
#     filtered_list = []
#     for num in numbersList:
#         if condition_func(num):
#             filtered_list.append(num)

#     return filtered_list

# myNumbers= [2, 4, 6, 7, 12, 32, 23, 14, 50]

# evens = custom_filter(is_even, myNumbers)
# print(evens)

# greaters = custom_filter(is_greater_than10, myNumbers)
# print(greaters)

# ---------

# def is_even(number):

#     return number % 2 == 0

# def is_greater_than10(number):

#     return number > 10

# def custom_filter(condition_func, numbersList):
#     filtered_list = []
#     for num in numbersList:
#         if condition_func(num):
#             filtered_list.append(num)

#     return filtered_list

# myNumbers= [2, 4, 6, 7, 12, 32, 23, 14, 50]

# evens = custom_filter(is_even, myNumbers)
# print(sorted(evens))

# greaters = custom_filter(is_greater_than10, myNumbers)
# print(sorted(greaters))
# -------

# def ten_percent_off(price):

#     return price * 0.90

# def bulk_discount(price):
#     if price > 100:
#         return price - 20
#     return price

# def calculate_total(discount_func, price):
#     finnal_price = discount_func(price)

#     return finnal_price

# cart_price = 190

# print("%10 off: ", calculate_total(ten_percent_off, cart_price))
# print("-%20 off: ", calculate_total(bulk_discount, cart_price))
# ----------------

#  4 - can be return as a result from a function.

# def greeting_factory(language):
#     def greet_fa(name):

#         return f"درود {name}"

#     def greet_en(name):

#         return f"Hello {name}"

#     if language == "fa":
#         return greet_fa
#     else:
#         return greet_en

# say_hello_persian = greeting_factory("fa")
# print(say_hello_persian("آریا"))

# say_hello_english = greeting_factory("en")
# print(say_hello_english("Aria")) 
# -----------

# def power_factory(exponent):

#     def calculate(base):
#         return base ** exponent
#     return calculate

# squar = power_factory(2)
# print(squar(3))
# # above output == bellow output
# print(power_factory(3)(2))
# --------------

# def make_multiplier(factor):

#     def multiplier(number):
#         return number * factor
#     return multiplier

# double = make_multiplier(2)
# quintupe = make_multiplier(5)

# print(double(10)) # = 20
# print(quintupe(10)) # = 50
# -------------

# 5 - can have properties and methods.

# Save the additional information into the function

# def send_email(reccipient, message):
#     print(f"Sending e-mail to {reccipient}: {message}")
#     send_email.calls_count += 1
# """Create a cutom_attribute: 
#         function_name.custom_attribute_name = value
#         for example, inabove and bellow'calls_count':
#             send_email.calls_count += 1
#                 function_name: send_email
#                 custom_attribute: calls_count
#                 value: calls_count +=1
#                     calls_count = calls_count +1
#         we can create a memmory by custom_attributes and
#         give it a value."""

# send_email.calls_count = 0

# send_email("aria@ari.com", "Hi Aria")
# send_email("ariayoosefi@aria2ber.com", "How are you, ARIA?")

# print("Total email sent: ", send_email.calls_count)
# ---------------

# Tax_rate()

# def calculate_total(price):
#     tax = price * calculate_total.tax_rate
#     return price + tax

# calculate_total.tax_rate = 0.10
# print("Total with 10% tax: ", calculate_total(100))

# calculate_total.tax_rate = 0.20
# print("Total with 20% tax: ", calculate_total(100))
#--------------------

# Name space vs Scope:
"""
    Name space: 
            it is a space that assign to a function or an object.
    Scope: 
            The collection of some spaceNames that his names
    is Similar together.
    Types: 
            1 - Built-in 2 - Global 3 - Enclosed 4 - Local
There is some example about them, in bellow.

"""
# 1 - Name spaces:
# 1 - Built-in: 

# print(dir(__builtins__))


# 2 - Global:

# print(globals())

# x = "Aria"
# def xy(a):
#     return a ** 2
# y = xy
# print(y(5))
# print(globals())


# 3 - Local:

# def xa():
#     x = 5    
#     print(f"X: {x}")
#     print("Locals(): ", locals(), "Type: ", type(locals()))

# def xb():
#     x = 6
#     print(f"X: {x}")
#     print("Locals(): ", locals(), "Type: ", type(locals()))

# xa()
# xb()

# print(locals())
# print(globals())
# In above the locals() == globals().


# 4 - Enclosed:

# def xa():
#     print("XA ->")
#     x = 5
#     print(f"\t X = {x}\t Enclosed: {locals()} Type: {type(locals())}")
#     def xb():
#         print("\n \t XB ->")
#         x = 6
#         print(f"\t \t X = {x}\t Locals: {locals()} Type: {type(locals())}")
#     xb()
# xa()


# Then finnaly all of 4 above types of nameSpaces in python are a Dictionary.
# They are a dictionary than include, Key: nameSpace, Value: value
# They're can be a Variable, function, Parameter, Argumant or any object.


# we can use a Built in nameSpace by import command, in python:

# import math
# pi = 20
# print(f"Out pi: {pi},\t math.pi: {math.pi}")

# we can see names from the Built-in nameSpaces by dir(bultinNamespace):

# print(dir(math))


# 2 - Scopes:
""" Scopes are groups of name spaces.
    The Scopes have 4 types similar name spaces. types:
        1 - Built-in 2 - Global 3 - Enclosing 4 - local"""
# x = 50
# if x == 50:
#     y = 10
# print(y,"\n")

# def xa():
#     # x = 20


#     def xb():
#         x = 25
#         print(f"X: {x}")

#     xb()

# xa()
# ------------------

# x = 50
# if x == 50:
#     y = 10
# print(y,"\n")

# def xx():
#     x = 15
#     def xa():
#         nonlocal x
#         # x -= 20
    
#         def xa2():
#             nonlocal x
#             x += 25
#             print(f"X: {x}")

#         xa2()

#     xa()

# xx()
# print()
# print(x)
# ----------

# x = 50
# if x == 50:
#     y = 10
# print(y,"\n")

# def xx():
#     x = 15
#     def xa():
        
#         x = 20
    
#         def xa2():
#             global x
#             x += 25
#             print(f"X: {x}")

#         xa2()
#     xa()

    
# xx()
# print()
# print(x)
# -----------

# Pass by value VS Pass by refrence: pass argumant by value or by refrence.

# Pass by value:

# def funcx(a):
#     a += 1
#     print(a)

# funcx(2)
# print()

# a = 1
# print(a, id(a))
# a +=1
# print(a, id(a), "\n")
# inMutable object 

# a_list = [1, 2, 3, 4]
# print(a_list, id(a_list))
# a_list.append(5)
# print(a_list, id(a_list))
# Mutable object

# in finnaly, inMutable objects are Pass by value.


# def funcx(a, b):
#     a += [2, 4, 6]
#     a[0] = 0
#     print(a)

# a = [1, 2, 3]
# print(a)
# print()

# funcx(a)
# print()

# print(a)
# print()

# def funcy(a):
#     b = {"a": 5, "b": 10, "c": 15}
#     a.update(b)
#     print(a)
    

# a = {"d": 4, "e": 8, "f": 12}
# print(a)
# print()

# funcy(a)
# print()

# print(a)

# def funcy2(a):
#     a["d"] = 8
#     print(a)

# a = {"a": 2, "b": 4, "c": 6}
# print(a)
# print()

# funcy2(a)
# print()

# print(a)


# def funcz(x):
#     x |= {1, 1, 4, 4, 6}
#     print(x)

# x = {2, 2, 3, 3, 5}
# print(x)
# print()

# funcz(x)
# print()

# print(x)


# def funcj(w):
#     w += [5, 6, 7, 8]
#     print(w)


# w = [1, 2, 3, 4]
# print(w)
# print()

# funcj(w)
# print()

# print(w)


# def funci(y):
#     y |= {"c": 3, "d": 4}
#     print(y)

# y = {"a": 1, "b": 2}
# print(y)
# print()

# funci(y)
# print()

# print(y)

# in finnaly Mutable objects == pass by refrences
# Mutable objects: lists, dicts, sets
# inMutable objects: int, str, tuple


# Control this reality: 1 - for Mutables 2 - for inMUutables 
# 1 - Mutables: copy() VS copy().deepcopy()

# def funcw(a):
#     a += [5, 6, 7, 8]
#     print(a)
    
# a = [1, 2, 3, 4]
# print(a)
# print()

# funcw(a.copy())
# print()

# print(a)

# import copy
# def funcu(a):
#     a += [{"c": [10, 11, 12]}, "d"] 
#     print(a)

# a = [[1, 2, 3], [4, 5, 6], "a", "b"]
# print(a)
# print()

# funcu(a.copy())
# funcu(copy.deepcopy(a))
# print()

# print(a)

# 2 - inMutables: return

# def funcv(a):
#     a += 1
#     print(a)
#     return a


# a = 4
# print(a)
# print()

# funcv(a)
# print()

# print(a)
# print()

# a = funcv(a)
# print(a)
# ---------------------------




