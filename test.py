from ast import operator
from cmath import sqrt
from hashlib import new
from math import ceil, floor
from tkinter.font import names


name = "mera"
age = "15"
num = 30

print (name+" "+age)
print (12  %  5)
print(type(-555))
print(pow(2,8))
print(max(5,1,8))
print(round(16.3))
print(ceil(5.1))
print(sqrt(4))


# برنامج صغير علي موضوع الانبوت
# name_2 = input("what's your name: ")
# age_2 = input("what's your age: ")
# print("hello "+name_2+" and your age is "+age_2)


# بناء اله حاسبة صغيرة وبسيطة
# num1 = input("enter your first numper: ")
# num2 = input("enter your second numper: ")
# result = float(num1) + float(num2)
# print(result)

# تطبيق لموضوع الليست
my_list = ["hi" , "al3ab" , "3amlen" , "world" , "smile"]
my_list2 = ["hollo" , "welcome" , "my" , "world"]
my_list3 = ["hala"]
my_list[3] = "s3ada"
print(my_list[2:4])

my_list = my_list2 + my_list3 + my_list
print(my_list)

my_list4 = ["welcome" , "my" , "world"]
my_list4.append("hahaha")
print(my_list4)

hmm = my_list2.index("my")
print(hmm)

new_list = my_list3.copy()
print(new_list)



# الفانكشنز
def say_hi(name , age , country) :
    print("hellow " +name+ " your age is " +age+ " your live in "+ country)

say_hi("Mera", str(15), "Egypt")


def sum(num1 , num2):
    return num1 + num2

print(sum(2,3))


# جمل الشرطية
def max_num(num1 , num2 , num3):
    if num1 >= num2 and num1 >= num3 :
        return num1
    elif num2 >= num1 and num2 >= num3 :
        return num2
    else :
        return num3

print(max_num(70,80,60))


# بناء اله حاسبة متطورة بعض الشئ
num1 = float(input("please enter your first numper: "))
operator = input("please enter the operator: ")
num2 = float(input("please enter your second numper: "))

if operator == "+" :
    print(num1 + num2)
elif operator == "-" :
    print(num1 - num2)
elif operator == "/" :
    print(num1 / num2)
elif operator == "*" :
    print(num1 * num2)
else:
    print("wrong operator please try again")