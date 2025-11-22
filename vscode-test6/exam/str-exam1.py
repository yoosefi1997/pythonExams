

# str1 = " i'm aria bri. i trying to learn. i am a student. "

# print( str1.count("a") )

# ------------------------------

# str1 = " i'm aria bri. i trying to learn. i am a student. "
# c = input(" enter a char: ")
# print( str1.count(c) )

# -----------------------------------


# msg = " i'm ARIABRI, am a student in jahad university. "
# print(msg)
# c_msg = input(" enter a char from above string:  ")

# print(  f" {c_msg} repeaded {msg.count(c_msg)}th in above string. " )

# ---------------------------------


# str1 = " enter a character:  "
# x = str1.split()
# # print(x)
# print(len(x))
# print(x[-1])

# ---------------

# str_in = input( " enter a string: " )
# spl_str = str_in.split()
# print(f" the string is: {str_in} ")
# print(f" the string have {len(spl_str)} words.")      
# print(f" sea please \t {spl_str} ") 
# print(f" the end word is {spl_str[-1]} ")

# -----------------------

# s = input(" enter a string: ")
# s = s.rstrip()
# f = s.rfind(" ")
# print(s[f: ])

# ---------------------

# x = " i'm Aria. i'm a coolMan. "
# print(x)
# y = input(f" Enter a str that joined in above sentece: ")
# print(f" is the  '{y}' in '{x}'? ".capitalize())
# if y in x :
#     print(f" yes the {y} is in {x} ".capitalize())
# else :
#     print(f" No, the {y} isn't in {x} ".capitalize())

# -------------------------

# s = input("enter a string:".capitalize())
# print(s.replace(" ", ""))
# print(s.replace(" ", "").replace("\t", ""))

# ----------------------------

# x = input("enter a phone number:". capitalize())
# print(f" the number without ziro is: {x.lstrip("0")} ")

# ---------------------------

# exersizes:

# exersize-1:

# x = input("enter a text:")
# print(f" your text is:\n\t {"\n\t".join(x.split("."))} " )

# print(x.split("."))
# print(x.split())
# print(x.count("."))
# print(x.count(","))
# print(x.count(x.split('.')))
# print(x.count(x.split()))

# x1 = x.split(".")
# x2 = x.split()
# print(f" \t the count of sentences is {len(x1)}th, \n \
#              the count of words is: {len(x2)}th, \n \
#              the count of alphabet with space is {len(x)} and \n \
#              the count of alphabet without space is: {len(x.replace(" ", ""))} ")
# print(f"'\t' the count of '.' is: {x.count(".")}, '\n' \
#         the count of ',' is: {x.count(",")}, '\n' \
#         the count of '_' is: {x.count("_")} and '\n' \
#         the count of '-' is: {x.count("-")} ")

# ---------------------------

# exersize-2

# x = input(" Enter a char: ")
# print(f" ASCIcode of {x} is: {ord(x)} ")
# y = int(input(" enter ASCKIcode: "))
# print(F" char of {y} is: {chr(y)} ")

# --------------------
# is numeric!?

# x = input(" Enter your phone number: ")
# print(f" the digits of {x} is number: {x.isalnum()}")

# ------------------------

x = input("enter a string:")
x1 = x.count(".")
x2 = x.count("?")
x3 = x.count("!")
y = x1 + x2 + x3

print(f" the number of sentences is {y}th ")
w = x.split()
print(f" the number of words is {len(w)}th. ")
print(f" the number of alphabete with space is {len(x)}th. ")
print(f" the number of alphabete without space is {len(x.replace(" ", ""))}th. ")

# # ---------------------------
