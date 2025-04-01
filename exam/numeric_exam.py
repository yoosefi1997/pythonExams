
# numeric's data types

# x = 50
# y = 7
# print( f" {x} ^ {y} = ", pow(x, y))

# --------------------------

# x = float(input(" enter number one: "))
# y = float(input(" enter number one: "))
# print( f" {x} ^ {y} = ", round(pow(x, y), 2))


# ----------------------------------------------------


# ABS

# x = -2.05
# print( f" ABS {x} = " + str(abs(x)) )

# ABS - input

# num_x = float(input(" enter a number: "))
# print(f" ABS {num_x} = ", abs(num_x))

# --------------------------------------------


# Max % Min

# x = [5, 2, -3, 3.14, 29, 33]
# print( f" Min {x} =  ", min(x), F" Max {x} = ", max(x) )

# ----------------------------------------

# x = input(" enter number(x, y, ....): ")
# x_list = x.split()
# joined_x = "".join(x_list)
# final_x = int(joined_x)
# print("Final number:", final_x)
# print(type(final_x))
# digits_list_x = [int(digit) for digit in str(final_x)]
# print("List of digits: ", digits_list_x )
# max_x = max(digits_list_x)
# min_x = min(digits_list_x)
# print( f" Max {digits_list_x} = ", max_x) 
# print( f" Min {digits_list_x} = ", min_x )

# -----------------------------------------

# Chatgpt


# numbers = input("Enter numbers separated by space: ")  # مثلاً: 1 2 3 4

# # تبدیل به لیست با استفاده از split()
# num_list = numbers.split()  # ['1', '2', '3', '4']

# # چسباندن عناصر لیست با join()
# joined_num = "".join(num_list)  # '1234'

# # تبدیل به عدد صحیح
# final_number = int(joined_num)

# print("Final number:", final_number) 
# print(type(final_number))

# --------------------------------


# div_mod(x ,y)

# x = float(input("enter number one: "))
# y = float(input("enter number one: "))
# print(f" divmod {x} / {y} = ", divmod(x, y))
# divmod_xy = list(divmod(x, y))
# # print(type(divmod_xy[0]))
# resxy1 = divmod_xy[0]
# resxy2 = divmod_xy[1]
# print(f" Kharej e ghesmat: {resxy1} Baghimandeh: {resxy2} ")

# SUM: a func for sum of all arumont

# x = input("enter numbers with space: ")
# y = x.split()
# z = "".join(y)
# finnal_num = int(z)
# print( f" joined digits of numbers: {finnal_num} ")
# digits_list = [int(digit) for digit in str(finnal_num)]
# print( "list of digits: ", digits_list)
# # print(type(digits_list))
# sum_digit = sum(digits_list)
# print( f" sum of all indexs = {sum_digit} " )

# 







