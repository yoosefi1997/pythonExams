# Encrypting and Decrypting a message using a simple cipher
# while True:
#     print(" 1-Encrypt \n 2-Decrypt \n 3-Exit")
#     choice = input("Enter your choice:")
#     if choice == '1':
#         message = input("Enter the text: ")
#         encrypted_message = ""
#         for c in message:
#             x = ord(c) * 3 + 5
#             encrypted_message += chr(x)
#         print("Encrypted message: ", encrypted_message)
#         print("*"*20 + "\n")
#     elif choice == '2':
#         encrypted_message = input("Enter the encrypted text:")  
#         decrypted_message = ""
#         for c  in encrypted_message:
#             x = (ord(c) - 5) // 3
#             decrypted_message += chr(x)
#         print("Decrypted message: ", decrypted_message)
#         print("*"*20 + "\n")
#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice. Please try again.")
# ----------

# the password generator
# from random import random, choice, randint, shuffle, sample
# import string

# lover = string.ascii_lowercase
# upper = string.ascii_uppercase
# # print(string.ascii_letters)
# symbols = "!@#$%^&*()_+"
# numbers = "0123456789"
# all = lover + upper + symbols + numbers

# while True:
#     print(" Options: \n 1-Generate a password \n 2-Exit")
#     choice = input("Enter an option: ")
#     if choice == "1":
#         lenght = int(input("Enter the lenght of the password: "))
#         password = "".join(sample(all, lenght))
#         print("Your password is: ", password, "\t Lenght: " , len(password))
         
#     elif choice == "2": 
#         break
#     else:
#         print("Invalid choice! Please try again.")
#         break
# ----------

# from time import time, sleep
# from os import name, system
# while True:
#     print(" Do you want to start it?  (Y/N)")
#     choice = input("Enter your choice: ")
#     if 'y' in choice.lower():
#         hour = int(input("Enter the hour: "))
#         minute = int(input("Enter the minute:"))
#         second = int(input("Enter the second: "))
#         total = hour * 60 * 60 + minute * 60 + second
#         print("The timer is starting know...")
#         sleep(1)
#         while total >= 1:
#             print("Time left: ", total, "Seconds")
#             total -= 1
#             sleep(1)
#             if name == "nt":
#                 system("cls")
#             else:
#                 system("clear")
          
#         print("Timer ended!")
#         if name == "nt":
#             system("cls")
#         else:
#             system("clear")
            
            
        
    
#     elif 'n' in choice.lower():
#         break
#     else:
#         print("Invalid choice! Please try again.")
# --------


    
 