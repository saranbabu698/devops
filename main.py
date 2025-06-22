# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#print("Good Morning !!")
#for i in range(10):
#    print ("Number is",i, "and the number's double is",i+i)

#name = input(str("What is your name? "))
#age = input("What is your age? ")
#Profession = input ("What is your profession? ")
#print("Hello " + name + "! You are a " + age + " years old! and you are a",Profession)
#print("You will be",(int(age)+5),"years old after 5 years!! and you will be a Senior",Profession)


#list = [(1,2,3),("Python","Java","React","C++","C")]
#print (list)
#print (list[1][1])

#s = "Saran"
#print (s.index('n'))

#dict = {"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]}
#print(dict)
#print (dict["B"])

#def add(a, b):
#    sum = a + b
#    return (sum)
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#print(add(a, b))

#import math
#print (math.copysign(10,-3))

#import numpy as np
#a = np.arange(0,1000)
#print(a)

#num = int(input("Enter a number: "))

#print(f"Factors of {num} are:")
#for i in range(1, num + 1):
#    if num % i == 0:
#        if i % 2 == 0:
#            print(f"{i} is Even")
#        else:
#            print(f"{i} is Odd")
#words = input("Enter words separated by space: ")
#word_list = words.split()
#word_list.sort()
#print("Sorted words:", " ".join(word_list))
result = []

#for num in range(1000, 3001):
#   num_str = str(num)
#    if all(int(digit) % 2 == 0 for digit in num_str):
#        result.append(num_str)
#
#print(",".join(result))

#sentence = input("Enter a sentence: ")

#letters = sum(c.isalpha() for c in sentence)
#digits = sum(c.isdigit() for c in sentence)

#print("LETTERS:", letters)
#print("DIGITS:", digits)

#s = input("Enter a string: ")
#print(s[::2])

#import random
#print (random.sample(range(1,10),5))

#n = int(input("Enter value of n: "))
#result = sum(i/(i+1) for i in range(1, n+1))
#print(round(result, 2))

from math import fsum
nums = [0.1] * 10
print("sum:", sum(nums))
print("    fsum:", fsum(nums))






