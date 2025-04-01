import copy


# # dataType-Lists

# x = ["Aria", 'bri', 29, "Married", 'student', "Engineer"]
# print(x)

# y = list("Aria")
# print(y)

# str = "i'm Aria. i have bro. i am an Software Engineer."
# z = str.split()
# print(z)
# print(str.split(" "))

# z += x
# print(z)

# print(x * 2)

# print(x == z)

# x[0] = "ARIABRI"
# del x[1]
# print(x)

# -----------------------------


# x = [1,2,3,4,5,6]
# x1 = x
# print(id(x1))
# print(id(x))
# coping values of X in X2 BY x[:]: from first index to end index.
# x2 = x[:]
# print(f" ID: {id(x2[:])}")
# coping values of X in X3 BY .copy() function: x3 = x.copy().
# x3 = x.copy()
# print(f" x3 ID: {id(x3)} ")

# ----------------------------


x = [1,2,["ARIABRI", 2025], ['Aria', 29, "bacheler's student", "Engineer"]]
print(x)

x[2][0] = " ari"
x1 = x.copy()
print(x1)
print(x)

x1[2][0] = " ari"
x1 = copy.deepcopy(x)
print(x1)
print(x)





