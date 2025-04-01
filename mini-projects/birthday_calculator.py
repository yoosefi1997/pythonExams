from datetime import date

# i develop this code with help of chatgpt.
# i give a code to chatgpt and it completed his.

# دریافت تاریخ امروز
# today = date.today()

# دریافت تاریخ تولد از ورودی
# birth_year, birth_month, birth_day = map(int, input("Enter your birthday (YYYY/MM/DD): ").split("/"))

# محاسبه سن اولیه
# years = today.year - birth_year
# months = today.month - birth_month
# days = today.day - birth_day

# تنظیم مقدارهای منفی
# if days < 0:
#     last_month = (today.replace(day=1) - date.resolution).day  # تعداد روزهای ماه قبل
#     days += last_month
#     months -= 1

# if months < 0:
#     years -= 1
#     months += 12

# نمایش نتیجه
# print(f"You have been alive for {years} years, {months} months, and {days} days.")


# --------------------------

# the bellow there are my code that gave to chatgpt:

# today = datetime.datetime.today()
# year_y = f"{today:%Y}"
# mouth_m = f"{today:%m}"
# day_d = f"{today:%d}"
# birthday = input( " enter your birthday(..../../..): " )
# birthday = birthday.split("/")
# print( " you have been alive {0}years, {1}months, {2} days. "
#       .format(int(year_y) - int(birthday[0]),
#               int(mouth_m) - int(birthday[1]),
#               int(day_d) - int(birthday[2])) )

# ---------------------------------


# today = date.today()
# birth_year, birth_month, birth_day = map(int, input("Enter your birthday(YY/MM/DD):").split("/"))
# years = today.year - birth_year
# months = today.month - birth_month
# days = today.day - birth_day

# if days < 0 :
#     last_month = (today.replace(day= 1) - date.resolution).day
#     days += last_month
#     months -= 1

# if months < 0:
#     years -= 1 
#     months += 12
        
# print(f"you have been alive for {years} years, {months} months, {days} days. ")

# -------------------------------

# today = date.today()
# birth_year,birth_month, birth_day =map(int, input("Enter your birthday(YY/MM/DD):").split("/"))

# years = today.year - birth_year
# months = today.month - birth_month
# days = today.day - birth_day

# if days < 0 :
#     last_month = (today.replace(day= 1) - date.resolution).day
#     days += last_month
#     months -= 1

# if months < 0 :
#     years -= 1
#     months += 12
# print(f"you have been alive for {years} years, {months} months and {days} days. ")


# ------------------

# today = date.today()
# birth_year, birth_month, birth_day = map(int, input("Enter your birthday(YY/MM/DD)").split("/"))
# years = today.year - birth_year
# months = today.month - birth_month
# days = today.day - birth_day
# if days < 0 :
#     llast_mont = (today.replace(day= 1) - date.resolution).day
#     days += llast_mont
#     months -= 1

# if months < 0 :
#     years -= 1
#     months += 12

# print(f"you have been alive for {years} years, {months} months and {days} days. ")

# ----------------------


# today = date.today()
# birth_year, birth_month, birth_day = map(int, input("enter your birthdate(YY/'MM/DD):".capitalize()).split("/"))
# years = today.year - birth_year
# months = today.month - birth_month
# days = today.day - birth_day

# if days < 0 :
#     last_month = (today.replace(day= 1) - date.resolution).day
#     days += last_month
#     months -= 1

# if months < 0 :
#     years -= 1
#     months += 12

# res =  (f"you have been alive for {years} years, {months} months and {days} days. ")
# print(f"you have been alive for {years} years, {months} months and {days} days. ".capitalize())

# print(res.find("and"))

# ------------------------------


# today = date.today()
# birth_year, birth_month, birth_day = map(int, input("enter your birthdate(YY/MM/DD):".capitalize()).split("/"))

# years = today.year - birth_year
# months = today.month - birth_month
# days = today.day - birth_day

# if days < 0 :
#     last_mont = (today.replace(day= 1) - date.resolution).day
#     days += last_mont
#     months -= 1

# if months < 0 :
#     years -= 1
#     months += 12

# print(f"you have been alive for {years} years, {months}  months and {days} days. ".capitalize())

# --------------------------

    
