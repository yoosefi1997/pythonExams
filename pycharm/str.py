import  copy

# x = "aria".capitalize()
# print(isinstance( x, str))
# print(type(x))
# print(type(x))

# -----------------------

# l0 = [1,2,3,4,5,"aria", 6]
# print(l0)
# l1 = l0
# print(l1)
# l1 = [1,2,3,4,5,"aria", 7]
# print(f" l1: {l1}\n l0: {l0} ")
# l2 = l0
# l2[0] = 0
# print(f" l2: {l2}\n l0: {l0} ")
# l3 = copy.deepcopy(l0)
# print(f" l3: {l3}\t l0: {l0} ")
# l3[-1] = 5
# print(f" l3: {l3}\n l0: {l0} ")

# t0 = (1,2,3,4,"aria", ['a','b','c','d','d',])
# print(t0)
# print(type(t0))
# t1 = t0
# print(f" t0: {t0} -- t1: {t1} ")
# -------------------------

# t = (1, 2, 4, "aria", ['a','b','c'], 5)
# print(t)
# print(type(t))
# t[4][1] = "R"
# print(t)
# --------------------------

# a, *b, c = 1, 2, 3, 4, 5, 6
# print(b)
# print(type(b))
# --------------------

# d = {"name": "aria", "lastname": "yousefi", "age": 29}
# print(d)
# print(type(d))
# d["phone"] = +989928117494
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# print(list(d.values()))
# print(list(d.items()))

# -----------------------------

# l = [1,2,4,5,12,0, 23]
# print(l)
# print(sorted(l))
# l = sorted(l)
# print(l)
# l = sorted(l , reverse=True)
# print(l)
# d = {"b": 29, "z": 1, "x": "aria", "n": 30}
# print(d.keys())
# print(sorted(d.keys()))
# # print(sorted(d.values()))
# d["x"] = 50
# print(d)
# print(sorted(d.values()))
# d["n"] = "aria"
# print(sorted(d.items()))
# y = d["n"]
# print(y)
# del d["n"]
# d["y"] = y
# print(d)
# ------------------------

# d = dict([("y", 415),("h", 315),("g", 215),("b", 115),("c", 95),("x", 55),("v", 15)])
# print(d)
# --------------------------

# d_info = {
#     "548": {"name": "aria", "family": "yousefi", "age" : 29, "gender": "male", "ave": 19},
#     "549": {"name": "ali", "family": "yousefifar", "age" : 25, "gender": "male", "ave": 18},
#     "547": {"name": "atrisa", "family": "yousefi", "age" : 29, "gender": "female", "ave": 19}
# }
# print(d_info)
# print(d_info["548"])
# print(d_info["549"]["name"])
# print(d_info["547"]["family"][1])
# ---------------------------
#
# k = "a","b","c","d","z","x","n"
# print(k)
# print(type(k))
# v = "aria", 25, 45, 15, 33,0.1
# d = dict(zip(k, v))
# print(d)
# z = zip(k, v)
# print(z)
# # print(list(zip(k, v)))
# print(dict(zip(k, v)))

# ------------------------------
#
# s = {1,3,4}
# print(s)
# s.add(5)
# print(s)
# s.remove(4)
# print(s)
# # s.update(1,5,4,6, 12)
# print(type(s))
# s.add("a")
# print(s)
# i_n = input("enter name: ")
# i_n1 = input("enter name: ")
# i_n2 = input("enter name: ")
# s.add(i_n)
# s.add(i_n1)
# s.add(i_n2)
# print(s)
#
# # if(i_n in s):
# #     print("there is in list. please try again!")
# # else:
# #     print("okay!")
#
# s.update([2,3,12,13])
# print(s)
# s.remove(i_n1)
# print(s)
# print(len(s))
# print("aria" in s)
# print("aria" is s)
# print(s == "aria")
# ---------------

# s = {1,2,3}
# print(s)
# s.add("aria")
# print(s)
# s.remove("aria")
# print(s)
# s.remove("aria")
# print(s)

# s = {1,2,3}
# print(s)
# s.add("aria")
# print(s)
# s.discard("aria")
# print(s)
# s.discard("aria")
# print(s)
# ---------------------------
#
# p = {3, 9, 15, 12, 6, 18}
# q = {4, 10, 16, 2, 8, 14, 12, 6, 18}
# print(p - q)
# print(q - p)
# print(p.difference(q))
# print(q.difference(p), "\n")
#
# print(" p | q = ", p | q)
# print(q | p)
# print(p.union(q))
# print(q.union(p))
#
# print("\n"," p & q = ", p & q)
# print(q & p)
# print(p.intersection(q))
# print(q.intersection(p))
#
# print("\n"," p ^ q = ", p ^ q)
# print(q ^ p)
# print((p | q) - (p & q))
# print((p - q) | (q - p))
# print(p.symmetric_difference(q))
# print(q.symmetric_difference(p))
# ------------------------

# a = {20, 40, 50}
# b = {10, 30, 60}
# print("A:",a,"B:", b)
# a.update(b)
# print("A:",a,"B:", b)
# print(f" A < B = {a < b} ")
# print(f" B < a = {b < a} ")
# print(f" A > B = {a > b} ")
# print(f" B < A = {b > a} ")
# print(" \ncalculation with python methods: ")
# print(f" A < B = {a.issubset(b)} ")
# print(f" B < a = {b.issubset(a)} ")
# print(f" A > B = {a.issuperset(b)  } ")
# print(f" B > A = {b.issuperset(a)} ")

# -------------------------

# none type data type

n = None
print(type(n))
b = True
print(b)
print(type(b))
print(int(b))
print(float(b))
print(complex(b))
print(int(b)+1)
print(int(b)-1)
print(int(b)*1)
print(b == 2)
b += 1
print(b)
print(b == 2)

if(b > 0) :
    print('aria')
b = False


