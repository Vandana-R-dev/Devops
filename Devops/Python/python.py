# print("hello")

# print("1+2")
# print(1+2)

# print("I am learning python")
# a=3
# print(a)

# name="vandana"
# age=32
# print(name,age)

# name=input("enter your name")
# age=input("enter your age")
# print("hi",name)
# print("my age is",age)





# print("i will become a python developer")



# name=input("please tell your name")
# food=input("enter your favorite food")
# print("my name is", name, "and I love",food)



# age=int(input("enter your age"))
# print("next year you wil be",age)

# age=23
# if age>=20:
#     print("you are major")
# else:
#     print("you are minor")

# a=int(input("enter the number"))
# if a>=0:
#     print("positive number")
# else:
#     print("negative number")

# marks = input("enter the password to open the machine")
# if marks == "python123":
#     print("access provided")
# else:
#     print("access not provided")

# marks=40
# if marks>=30:
#     print("poor student")
# elif marks<=29:
#     print("fail student")
# else:
#     print("good student")

# marks = 100

# if marks >= 90:
#     print("Excellent")
# elif marks >= 70:
#     print("Good")
# else:
#     print("Need practice")

# 🎯 Mission 1 — Even or Odd
# num=int(input("enter your number"))
# if num%2==0:
#     print("its even number")
# else:
#     print("its odd number")

# Mission 2 — Largest Number
# a=int(input("enter the first number"))
# c=int(input("enter your other number"))
# if a>=c:
#     print(a, "is the largest number")
# else:
#     print(c,"is the largest number")

# Mission 3 — Login System 🔥
# username=input("enter your username")
# password=input("enter your password")
# if username=="admin" and password=="python123":
#     print("login successful")
# else:
#     print("Invalid credentials")

# MINI PROJECT — Age Category System
# age=int(input("enter your age"))
# if age<=13:
#     print("its a child")
# elif age>13 and age<=19:
#     print("its a teenager")
# elif age>=20 and age<=59:
#     print("it's an adult")
# else:
#     print("senior citizen")

# if age < 13:
#     print("Child")

# elif age <= 19:
#     print("Teenager")

# elif age <= 59:
#     print("Adult")

# else:
#     print("Senior Citizen")

# for i in range (3):
#   print("hello")

# for i in range(1,6):
#   print("vandana")
#   print(i)

# 🎯 Mission 1
# Print:
# 1 to 10
# using loop.
# count=1
# while count<=4:
#     print("hi")
#     count+=1

# 🎯 Mission 2
# Print all EVEN numbers from 1 to 20.

# for i in range(1,21):
#     if i%2==0:
#         print(i)

# 🎯 Mission 3
# Ask number from user.
# Print multiplication table.
# Example:
    
# a=int(input("enter the number"))
# for i in range(1,11):
#     print(a, "*", i,"=",a*i)


# password=''
# while password!="python123":
#     password=input("enter the password")
#     print("wrong password")
# print("access provicded")

# def welcome(name):
#     print("Welcome", name)

# welcome("Rahul")
# welcome("Amit")
# welcome("Priya")

# def create_hi(message):
#     print(message)

# create_hi("hi")

# def multiply(a,b):
#     print(a*b)
# multiply(2,3)

# def multiply(a,b):
#     return a*b

# a=multiply(3,4)
# print(a)

# def cube(a):
#     return a*a*a
# a=cube(3)
# print(a)

# def country(name):
#     return(name)
# b=country("india")
# print(b)

def math(a,b):
    return a+b, a-b,a*b
value=math(2,3)
print(value)
