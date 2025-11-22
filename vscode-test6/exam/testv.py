
from decimal import Decimal 
from fractions import Fraction

# x = 5
# # print(x)
# y = " Aria "
# print(y[0:4])

# ------------


# # number presentation 

# f = 1_000_000_000.0
# f1 = 1.55
# f2 = 3e+10
# print(type(f2))
# print(f2)

# # --------------


# # casting

# y = float(Decimal('0.5') + Decimal('0.2')  )
# print(type(y))
# print(y)
# print(y == 0.7)

# # ------------------------


# # fractions

# print(Fraction(0.5))



# s = Fraction(1.5)
# print(s)

# # -----------------------


# # COMPLEX

# comp = 5 + 2J
# print(type(comp))
# print(comp)
# print(comp.real)
# print(comp.imag)
# print(comp.conjugate())
# d_comp = 2 - 5j
# print(type(d_comp))
# print(d_comp)
# print(comp + d_comp)

# ----------------------------


# rond, abs, power

p1 = 1.05556852872
print(pow(p1,2))


# kg = 85
# g = kg * 1000
# print(g, " gram ")


# wkg = int(input(" enter your weight(kg):  "))
# wg = (wkg) * 1000
# print( str(wg), "G", sep="")

# -------------------------------------------------


# calculation

# f = int(input(" enter number-1: "))
# g = int(input(" enter number-2: "))
# print( f, "+", g, "=", f + g )
# print( f, "-", g, "=", f - g )
# print( f, "*", g, "=", f * g )
# print( f, "/", g, "=", f / g )


# ---------------------------------------------


# number seperator

f = int(input(" enter number-1: "))
temp = f % 10
print(temp)
f //= 10
temp = f % 10
print(temp)
f //= 10
temp = f % 10
print(temp)

# ----------------------------

