# -*- coding: utf-8 -*-
"""Sequential problems python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17SkFWQqWzS8NJJrU6P9XCbg7qIBR_S7R

***1 . Average of 3 numbers***
"""

num1=int(input("Enter a number : "))
num2=int(input("Enter a number : "))
num3=int(input("Enter a  number : "))
sum=num1+num2+num3
average=sum/3
print("Average = ",+average)

"""***2 . Sum and average of 3 numbers***"""

num1=int(input("Enter a number : "))
num2=int(input("Enter a number : "))
num3=int(input("Enter a  number : "))
sum=num1+num2+num3
average=sum/3
print("Sum = ",+sum)
print("Average = ",+average)

"""***3 . Time***"""

sec=int(input("Enter seconds : "))
min=sec/60
hours=min/60
print("Seconds in minutes : ",+min)
print("Seconds in hours : ",+hours)

"""***4 . Area and Perimeter of a triangle***"""

A=float(input("Enter length of first side : "))
B=float(input("Enter length of second side : "))
C=float(input("Enter length of third side : "))
perimeter=A+B+C
s=perimeter/2
Area=(s*(s-A)*(s-B)*(s-C))**0.5
print("Perimeter = ",+perimeter)
print("Area = ",+Area)

"""***5 . Area of Circle***"""

import math
radius=float(input("Enter radius : "))
area=math.pi*(radius**2)
print("Area of the circle = ",+area)

"""***Swapping without temporary variable***"""

a=int(input("Enter number A : "))
b=int(input("Enter number B : "))
a=a+b
b=a-b
a=a-b
print("Number A = ",+a)
print("Number B = ",+b)

"""***Sum,Difference,Product,Quotient***"""

a=int(input("Enter first number = "))
b=int(input("Enter second number = "))
sum= a+b
print("Sum = ",+sum)
diff = a-b
print("Difference = ",+diff)
pro= a*b
print("Product = ",+pro)
quo=a//b
print("Quotient = ",+quo)
rem=a%b
print("Reminder = ",+rem)

"""***Days calculator***"""

days=int(input("Enter number of days = "))
months=days/30
years=days/365
print("Number of months = ",+months)
print("Number of years = ",+years)