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


# x = [1,2,["ARIABRI", 2025], ['Aria', 29, "bacheler's student", "Engineer"]]
# print(x)

# x[2][0] = " ari"
# x1 = x.copy()
# print(x1)
# print(x)

# x1[2][0] = " ari"
# x1 = copy.deepcopy(x)
# print(x1)
# print(x)

# ------------------

# l1 = [1, 2, 3]
# print(l1)
# print(id(l1))
# l2 = l1
# print(l2)
# print(id(l2)) 

# print(f" \n ")

# l2[0] = 0
# print(l2)
# print(id(l2))
# print(l1)
# print(id(l1))

# print(f" \n ")

# # coping values of l1 in l2 by indexing: [:]
# l2 = l1[:]
# print(l2)
# print(id(l2))
# print(l1)
# print(id(l1))
# l2[1], l2[2] = 1, 2
# print("after changes:")
# print(l2)
# print(id(l2))
# print(l1)
# print(id(l1))

# print(f" \n ")

# # coping values of l1 in l2 by Copy function: .copy()
# print(l2)
# print(id(l2))
# print(l1)
# print(id(l1))
# print(" after changes ")
# l2 = l1.copy()
# l2[2] = 4
# print(l2)
# print(id(l2))
# print(l1)
# print(id(l1))

# ----------------------------

# person = ["persons",  [" Aria ", 29, " male ", " married ", "Software student", "Software engineering"]
#           , [" Elias ", 28, " male ", " married ", "Software student", "Software engineering"],
#             [" Eskandar ", 29, " male ", " single ", "Software student", "Software engineering"]  ]
# print(person)
# print(type(person))
# print(person[1])

# ---------------------------

# cars = list("benz BMW AUD Ferari TOYUTA")
# clasic_cars = cars[0:2]
# print(id(cars))
# print(id(clasic_cars))
# print(cars)
# print(clasic_cars)

# --------------------------

# countries = input(" Enter a name of several countries: ")
# print(countries)

# countries = countries.rstrip(".")
# countries = countries.split(",")  
# print( f" list of your Entered countries: \n\t  {" \n".join(countries) } "  )




# ---------------------------------

# countries = input(" Enter a name of several countries: ")
# print(countries)

# countries = countries.rstrip(".")
# countries = countries.upper().strip(",").split()
# print( f" list of your Entered countries: \n\t  {(f" \n ".join(countries) ) } " )

# -----------------------------

# x = [1, 2, ['a','b', 'c'], 5]
# print(x)
# print(f" the thirth index of above list is: {x[2]} ")
# print(f" the2th argumant of 3th index is: {x[2][1]}  ")

# -----------------------------

# x = [1, 2, ['aria','blue', '29'], 5]
# print(x)
# print(f" the thirth index of above list is: {x[2]} ")
# print(f" the2th argumant of 3th index is: {x[2][1]}  ")
# print(f" first argumant from first index that is 3th member of above list is: {x[2][0][0]} ")
# print(f" first argumant from first index that is 3th member of above list is: {x[2][2][0]} ")

# -------------------------------

# l1 = [1,2, ['aria', 'b']]
# # print(f" list-1 : {l1},  ID: {id(l1)} ")
# l2 = l1.copy()
# # print(f" list-2 without changes : {l2}, ID: {id(l2)} ")
# l2[1] = "Aria"
# # print(f" list-2 with changes : {l2}, ID: {id(l2)} ")
# l2[2][0] = 'A'
# print(f" list-2 with changes : {l1}, ID: {id(l1)} ")
# print(f" list-2 with changes : {l2}, ID: {id(l2)} ")
 
# -----------------------------

# l1 = [1,2, ['aria', 'b']]
# # print(f" list-1 : {l1},  ID: {id(l1)} ")
# l2 = copy.copy(l1)
# # print(f" list-2 without changes : {l2}, ID: {id(l2)} ")
# l2[1] = "Aria"
# # print(f" list-2 with changes : {l2}, ID: {id(l2)} ")
# l2 = copy.deepcopy(l1)
# l2[2][0] = 'A'
# print(f" list-2 with changes : {l1}, ID: {id(l1)} ")
# print(f" list-2 with changes : {l2}, ID: {id(l2)} ")

# -----------------------------

# l = [1, 2, 3, "Aria", '29']
# print(l)
# l.append("bri")
# print(l)
# l.append(['a', 'b', 'c'])
# print(l)

# ----------------------------

# l = [1, 2, 3, 4, 5, 6]
# print(l)
# print(l[2:5])

# l[2:5] = ['a', 'b', 'c']
# print(l[2:5])
# print(l)

# l[2:5] = ['a', 'b', 'c', 'd']
# print(l)

# l[2:5] = []
# print(l)

# l[:] = []
# print(l)

# del l[1]
# print(l)

# del l[2:5]
# print(l)

# x = len(l)
# print(x)

# print(l[0:len(l)])

# print(l[len(l)-1])

# print(l[0:len(l)-1])

# a, b, c = [1, 2, 3]
# print(a)
# print(a, b, c)

a, b, *c = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
print(  F" also you see the values of above variables is: A = {a}, B = {b}, C = {c}   "  )
print(f"  az whel az we see,  values of thirth variable included a list of iintegeres!  ")
print(f" variable: C, value: {c}, variableType is: {type(c)}  ")


# a, *b, c = [1, 2, 3, 4, 5, 6]
# print(a)
# print(b)
# print(a, b, c)

# *a, b, c = [1, 2, 3, 4, 5, 6]
# print(a)
# print(b)
# print(c)
# print(a, b, c)
         
# ------------------------




