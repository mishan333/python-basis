# a={
#     'name':['mishan' , 'acharya'],
#     'roll.no':(2),
#      'add': ('haraiya')
# }

# a.pop('add')
# print(a)

# print 1000 times
# i=0
# while i<1000:
#     print(i,'i love you')
#     i+=1

# print even number

# i=0
# while i<10:
#     print('even number is:',i)
#     i+=2

# print("hello mishan")
# x=6
# x="mishan"

# print(x)
# # print(y)

# print("h"+ 5)

# age=10

# if(age>= 18):
#   print("vote")

# else:
#     print("can not vote")  

# find largest number
# a=int(input())
# b=int(input())
# c=int(input())


# if (a>b & a>c):
#   print("a is greater")

# elif (b>a & b>c):
#        print("b is greater")

# else:
#     print("c is greater")   


# ADD TWO NUMBER
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# print("the sum of a and b is:",(a+b))

# SHORT HAND IF
# a=45
# if a>40:print('a')

# short hand elif

# a=10
# print('a') if a>30 else print('b')


# a=45
# print('c') if a>30  else print('d') if a>40 else print('e')

# for loop
# for i in range(11):
#    a=2*i
#    print(f'2*{i}={a}')
#    i+=1

# for i in range (1,11):
#  result=3*i
#  print(f"3*{i}={result}")
#  i+=1

# F-STRING
# a=20
# b=30
# c=a+b
# print(f"the sum is a {a} and b {b} is {c}")

# use *args

# def abc(*args):
#     sum=0
#     for num in args:
#         sum = sum + num
#     return sum
# sum = abc (2,3,4,5,6)
# print(sum) 

# use **kwargs

# sub={
#      'math': 21,
#      'science':22,

# def percentage(**kwargs):
#     sum=0
#     for key, value in kwargs.items():
#          sum=sum+value 

#     return sum
# sum = percentage(math=99,english=79)    
# print(sum) 


# lambda function

def add(x,y):
   return x+y
print(add(2,4))

# function use gareko mathi ko code lamda use garera yesari use garni :

add = lambda x,y: x+y
print(add(3,4))
