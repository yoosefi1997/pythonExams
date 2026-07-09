# import random
# random.randint()
# random.choice()
from itertools import count
from operator import index

# from random import random, seed
# # when we need amount of
# seed(5)
# print(random())
# print(random())
# print(random())
# print(random())
# print(random())
# print(random())
# ---------------


# from random import random, seed

from decorator import append

# for i in range(10):
#     print( 5 + (random() * (10 - 5)))
#     ----------
# for _ in range(10):
#     print( 5 + ( random() * (11 - 5)))
#     -------------
# for _ in range(12):
#     print(int(5 + ( random() * (15 - 5))))
# ---------
# rand_list = []
# for _ in range(12):
#     print(int(5 + ( random() * (20 - 5))))
# print("-"* 10)
# randlist = []
# for _ in range(12):
#     randlist.append(int(5 + (random() * (10 - 5))))
# print(randlist, end="\n")
# ----------------
# rand_list = []
# for _ in range(10):
#     rand_list.append(int(5 + (random() * (10 - 5))))
# print(rand_list)
# randset = set(rand_list)
# print(randset)
# -------------
from random import random, uniform

# for _ in range(12):
#     print(uniform(5, 12))
# ---------

# for _ in range(15):
#     print(int(uniform(5, 12)))
# -------------

# for i in range(12000):
#     if int(uniform(5, 12)) == 11:
#         print("Ok!")
#     else:
#         print("Not ok")
# ----------
from random import randint

# for _ in range(10):
#     print(randint(5, 12))
# -------------
from random import randrange

# for _ in range(10):
#     print(randrange(5, 99, 2))
# -----------
from random import randint

# x = ['a','b','c','d']
# for _ in range(11):
#     print(x[randint(0, len(x)-1)])
# ------------
from random import choice

# x = ["a","b","c","d","e"]
# for _ in range(12):
#     print(choice(x))
# -----------
from random import sample

# x = ["a","b","c","d","e","f",]
# print("x: ", x)
# print("select amount of members from above list:", sample(x, 2))
# print()
# for _ in range(19):
#     print(sample(x, 3))
# ----------------
from random import seed

x = ["a","b","c","d","e","f","g"]
seed(15)
print("The const of a Sample:", sample(x, 4))
print()
for _ in range(12):
    print(sample(x, 3))
# -------------

# Random Methods:

# x = ["a","b","c","d","e","f","g"]
# print("The const of a Sample:", sample(x, 3))
# the top example is test example for test the python extension in vscode.
