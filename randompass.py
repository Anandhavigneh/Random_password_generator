print(" Welcome to Random Password generator ")
import random

random_char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
random_pass=int(input("place enter the number of password generate:"))
paslen=int(input("place enter the length of password:"))

for x in range(random_pass):
    password=""
    for y in range(paslen):
        password+=random.choice(random_char)
    print(password)
