import random

# Data elements for password Generation :
alphabets  =  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789012345678998654321"
special_charcters = "@#$%&*?"
data = alphabets + numbers

print("*************************************************************************************************** \n")

password_len = int(input("Welcome Sir ! Please Enter the password length you want :  "))

try:
    if(password_len==0):
        raise(NameError("Error"))
    choice = int(input("Want special Charactes in password if yes ! press 1: "))
    password = ""
    for i in range(password_len):
        flag = random.randint(1,3)
        if(choice==1):
            password += random.choice(special_charcters)
            choice = 0
        password += random.choice(data)
    print("Congratulation ! Your Password is {}".format(password))
except NameError:
    print("Oooh ! It's invalid Length. Try Again !!")
finally:
    print("\n Designed by Ankit Raja")
    print("***************************************************************************************************")
