import datetime

# the calck of birthyear.

# fname = input(" enter your first-name: ")
# lname = input(" enter your last-name: ")
# age = input(" enter your age: ")
# field = input(" enter your field: ")
# c_age = 2025 - int(age)
# # print(c_age)
# print(  f" {fname} {lname}, you are {age} years old. because you burn in {c_age}. " )
# info = f" {fname} {lname}, you are {age} years old. because you burn in {c_age}. "
# spl_info = info.split()
# # print(spl_info)
# # print(type(info))
# print(len(spl_info))
# # print(spl_info[0:2])
# full_name =  spl_info[0:2]
# full_name = " ".join(full_name)
# full_name = full_name.rstrip(',')
# print(full_name)

# -------------------------------

# x = input( " enter number-one " )
# y = input( " enter number-one " )
# print( f" {x} + {y} =  {int(x)+int(y)} " )
# print( f" {x} - {y} =  {int(x)-int(y)} " )
# print( f" {x} * {y} =  {int(x)*int(y)} " )
# print( f" {x} / {y} =  {int(x)/int(y)} " )
# print( f" {x} // {y} =  {int(x)//int(y)} " )
# print( f" divmod {x} / {y} =  {divmod(int(x), int(y))} " )
# print( f" {x} % {y} =  {int(x)%int(y)} " )
# print( f" {x} ^ {y} =  {int(x)**int(y)} " )

# --------------------------

# x = input( " enter a string: " )
# print(x)
# x = x.split()
# print("\t".join(x))
# print( f" the recent word '{x[-1].rstrip(".")}' " )

# ----------------------------

# x = int(input( " enter a number: " ))
# temp = x % 10
# print(temp)
# n = x // 10 
# print(n % 10)
# print(n // 10 % 10)

# x = int(input( " enter a number: " ))
# # print( f" yekan : {x % 10}\n dahgan : {x // 10 % 10}\n \
# #       sadgan : {x // 10 //10 % 10} " )
# print( f"  {x % 10}-{x // 10 % 10}-{x // 10 //10 % 10} " )

# -------------------------

# x = input( " enter a string " )
# y = input( " enter a char " )
# z = x.count(y)
# print(z)

# ---------------------

# x = input( " enter a string: " )
# x = x.rstrip()
# z = x.rfind(" ")
# print(x[z:])
# ----------------
# x = input( " enter a string: " )
# x = x.split()
# y = x[-1]
# y = y.rstrip()
# y = y.rstrip(".")
# print(y)

# -------------------------

# x = input( " enter a string: " )
# y = input( " enter a string: " )

# print( f" {y in x}, {y} is in {x}. " )
# print( f" {y} is {x.find(y)}th in '{x.rstrip(".")}' sentence. " )

# -------------------------

today = datetime.datetime.today()
year_y = f"{today:%Y}"
mouth_m = f"{today:%m}"
day_d = f"{today:%d}"
birthday = input( " enter your birthday(..../../..): " )
birthday = birthday.split("/")
print( " you have been alive {0}years, {1}months, {2} days. "
      .format(int(year_y) - int(birthday[0]),
              int(mouth_m) - int(birthday[1]),
              int(day_d) - int(birthday[2])) )

# --------------------------------




