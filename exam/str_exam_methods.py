# x = "ARIABRI"
# print(isinstance(x, float))
# print(type(x))


# y = " i'm ARIA \t bri \t  "
# print(y)

# z = """\
# ARIA BRI
# ARIA BLUE BRI
# ARIA BRI9094\
# """
# print(z)
# print(" -------------------- ")
# print(z[0:5])
# print(z[:5:2])
# print(len(z))
# print(z[len(z) -1])

# -----------------------


# txt1 = " ARIAblueBRI "
# txt2 = " Aria "
# txt3 = ' i\'m 29 years old '
# print(txt1 + "\n" + txt2 * 3 + "\t" + txt3 )

# -------------------------------------


# txt spliting

# sentence = """\
# i'm ARIABRI. 
# i am 29 years old
# i'm married
# """
# print(sentence)
# words = sentence.split()
# print(words)
# print(" ".join(words))
# print(words, sep="")

# -----------------------------


# str replacing

# msg = " hi, Aria "
# print(msg)
# print(msg.replace("Aria", "ALEXANDRA"))

# ---------------------------


# in

# x = " machine learning is Amazing "
# print("machine" in x)
# print("aria" not in x)

# ------------------------------


# F-string

# my_name = "Aria"
# my_age = 29
# my_feild = "AI"
# print(F" My name is {my_name} and i'm {my_age} years old. ")

# ---------------------------


# txt repeet

# x = "ARIA"
# y = "blue"
# z = "BRI"
# print("Aria " *2 + z)

# ---------------------------


# slicing

# x = "ARIAblueBRI"
# print(x[0:-7:2])
# print(x[0:4] + x[8:])
# print(x[::-1])



# exams

# x = "ARIA blue BRI"
# print(x.split())
# x = x.split()
# print(x)
# print("\n".join(x))
# x = "\n".join(x)
# print("\n", x)
# print("\n", x.replace("A", "x"))

# ----------------------------


# exam-1

# str sorting

# x = """\
# ARIA_blue_BRI,
# this is a chajnnel for you.
# orginal owner: ARIA
# """
# x = x.split()
# # print(x)
# y = x[0]
# # print(y)
# # print(x)
# y = y.split("_")
# # print(y)
# y = "".join(y)
# print(y)
# x[0] = y
# print(x)
# y2 = x[1:7]
# print(y2)
# y2 = " ".join(y2)
# print(y2)
# x[1] = y2
# print(x)
# del x[2:7]
# print(x)
# # print(len(x))
# y3 = x[2:5]
# # print(y3)
# y3 = " ".join(y3)
# print(y3)
# x[2] = y3
# print(x)
# del x[3:5]
# print(x)
# x = " ".join(x)
# print(x)

# -------------------------

# # optimization by chatgpt:

# x = """\
# ARIA_blue_BRI,
# this is a chajnnel for you.
# orginal owner: ARIA
# """
# x = x.split()
# x[0] = "".join(x[0].split("_"))
# x[1] = " ".join(x[1:x.index("orginal")])
# x = [x[0], x[1], " ".join(x[x.index("orginal"):])]
# x = " ".join(x)
# print(x)

# -------------------------------



# CHATGPT

# x = """\
#     ARIA blue BRI
#     this is my channel. 
#     i wnat intro real AI to you.
#     follow me please!
#     """
# x = x.split()
# x[0] = "".join(x[0:x.index("this")])
# x[1] = " ".join(x[x.index("this"):x.index("i")])
# x[2] = " ".join(x[x.index("i"):x.index("follow")])
# x[3] = " ".join(x[x.index("follow"):])
# x = "".join(x[0]) , "".join(x[1]) , "".join(x[2]) , "".join (x[3])
# x = " ".join(x)
# print(x)

# --------------------


# y = """\
#     ARIA blue BRI
#     this is my channel. 
#     i wnat intro real AI to you.
#     follow me please!
#     """
# words = y.split()
# idy_this = words.index("this")
# idy_i = words.index("i")
# idy_follow = words.index("follow")
# part1 = "".join(words[:idy_this])
# part2 = " ".join(words[idy_this:idy_i])
# part3 = " ".join(words[idy_i:idy_follow])
# part4 = " ".join(words[idy_follow:])
# final_txt = f"{part1} {part2} {part3} {part4} "
# print(final_txt)

# --------------------


# x = """\
# ARIA blue BRI
# this is my channel. 
# i wnat intro real AI to you.
# follow me please!
# """
# # جدا کردن متن به خطوط مجزا بدون حذف فاصله‌ها
# lines = x.splitlines()

# # حذف فاصله‌های اضافی در هر خط (strip) و ترکیب خطوط در یک متن
# final_text = " ".join(map(str.strip, lines))

# print(final_text)



# x = """\
#     ARIA blue BRI
#     this is my channel. 
#     i wnat intro real AI to you.
#     follow me please!
#     """
# x = x.split()
# x[0] = "".join(x[:x.index("this")])
# sections = [
#     " ".join(x[x.index("this"):x.index("i")]),
#     " ".join(x[x.index("i"):x.index("follow")]),
#     " ".join(x[x.index("follow"):])
# ]
# final_text = " ".join([x[0]] + sections)
# print(final_text)

# ---------------------

# my try


# str1 = """\
#      ARIA blue BRI,
#      this is my channel. 
#      i want intro real AI to you.
#      follow me please!
#     """
# str1 = str1.split()
# str1[0] = "".join(str1[:str1.index("this")])
# sections = [
#     " ".join(str1[str1.index("this"):str1.index("i")]),
#     " ".join(str1[str1.index("i"):str1.index("follow")]),
#     " ".join(str1[str1.index("follow"):])
# ]
# final_text = " ".join([str1[0]] + sections)
# print(final_text)





