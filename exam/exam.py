# print(R" aria\blue\bri ")

# print(" X is {} Y is {} Z is {} ".format(5,6, 1+2) )
# print("  ")

# --------------------

x = float(input("enter a number : "))
y = float(input("enter a number : "))

calck_dict = {
    'sum' : x + y,
    'minus' : x - y,
    'multi' : x * y,
    'div' : divmod(x, y),
    'pow_xy' : pow(x,y),
    'pow_yx' : x ** y
}

print( " SUM is : {sum} \n minus is : {minus} \n multiply is : {multi} \n divmod is : {div} \
 \n X ^ Y is : {pow_xy} Y ^ X is : {pow_yx} ".format(**calck_dict) )





