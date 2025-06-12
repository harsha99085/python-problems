# 1 Print "Hello, World!
# print("hello world!")

#2)Add two numbers
# a=int(input("enter element "))
# b=int(input("enter b elemnt"))
# print(a+b)

#3swap two variables
# a=10
# b=20
# print("before swap",a,b)
# # a,b=b,a
# # print("after swap ",a,b)

# c=a
# a=b
# b=c
# print(a,b)

#4 Convert Celsius to Fahrenheit
# c=float(input("enter celsious"))  
# f=c*9/5+32    # formula frn heat=(celsious*9/5)+32
# print(f)

#4 Convert  Fahrenheit to Celsius
# f=float(input("enter frn heat")) #farhen heat
# celsious=(f-32)*5/9    # celsious= (frnheat-32)*5/9
# print(celsious)

#5 Find the largest of three numbers
# a=int(input("enter number"))
# b=int(input("enter number"))
# c=int(input("enter number"))
# if a>b and a>c:
#     print(a,"is big")
# elif b>a and b>c:
#     print(b,"b is big")
# else:
#     print(c,"is big")

#using lambda
# big=lambda a,b,c: a if a>b and a>c else(b if b>c and b>a else c)
# print(big(10,100,30))

#6 Check if a number is even or odd
# a=int(input("enter number"))
# if a%2==0:
#     print("even",a)
# else:
#     print("odd",a)

#using lambda
# evenorodd = lambda a:"even" if a % 2==0  else  "odd"
# print(evenorodd(20))

#7Calculate factorial using loop
# a=int(input("enter fact number"))
# fact=1
# for i in range(1,a+1):
#     fact=i*fact
# print(fact)

#fact using lambda
# fact= lambda n: 1 if n==0 else n*fact(n-1)
# print(fact(5))

#8 def fact(n):
#   if n==0 or n==1:
#     return 1
#   else:
#     return  n*fact(n-1)     
# print(fact(5))
  
  
# #9 Generate Fibonacci series
# a=0
# b=1
# num=int(input("enter"))
# if num>0:
#     print(a)
# elif num>1:
#     print(b)
# for x in range(2,num):
#     c=a+b
#     a=b
#     b=c
#     print(c)

#10Check if a number is prime
#a=int(input("enter number"))
#count=0
#for b in range(1,a+1):
 #   if a%b==0:
#        count=count+1
#if count==2:
#    print("prime")
#else:
 #   print("not prime")


