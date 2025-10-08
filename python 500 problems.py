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
# a=int(input("enter number"))
# count=0
# for b in range(1,a+1):
#     if a%b==0:
#         count=count+1
# if count==2:
#     print("prime")
# else:
#     print("not prime")

#usig lambda
# prime= lambda n:n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
# print(prime(6))

#lambda 
# primt= lambda n:n>1 and sum(n%i==0 for i in range(2,n+1))==2 
# print(primt(6))
# n > 1 ensures we’re only checking for numbers greater than 1.

# sum(n % i == 0 for i in range(1, n + 1)):

# For each i from 1 to n, we check if n % i == 0 (i.e., divides exactly).

# This creates a list of boolean values like [True, False, ..., True]

# When used in sum(...), True = 1 and False = 0 → giving us a count of exact divisors.

# If that count is exactly 2, the number is prime.

#11 multplication table
# a= int(input('enter multiplication table'))  
# for j in range(1,10+1): # it print range like 1 to 10
#     print(a,'X',j,'=',a*j) # it print table

#12 create simple calulator using two numbers
# print('select options\n addition 1\n subtraction 2\n mul 3\n div 4\n')
# a=int(input('select option'))
# num=int(input('number'))
# num1=int(input('number'))

# def add(a,b):
#     c=a+b
#     return c
# def sub(a,b):
#     c=a-b
#     return c
# sub(num,num1)
# def mul(a,b):
#     c=a*b
#     return c
# mul(num,num1)
# def div(a,b):
#     c=a/b
#     return c
# div(num,num1)
# if a==1:
#     print(add(num,num1))
# elif a==2:
#     print(sub(num,num1))
# elif a==3:
#     print(mul(num,num1))
# elif a==4:
#     print(div(num,num1))
# else:
#     print('thank you')

# 13 area of circle (22/7)*r*r
# a=float(input('enter radius'))
# print(22/7*a*a)

# 14 leap year 
# a=int(input('enter year'))
# if (a%4==0 and a%100!=0) or (a%400==0):
#     print('it is a leap year')
# else:
#     print(' not leap year')

#15 #Sum of digits of a number
# a=int(input('enter number'))
# sum=0         # intially sum =0
# while a>0:    # this loop helps to  break
#     rem=a%10   # it takes last digit
#     sum=sum+rem #0+lastdigit
#     a=a//10 # removes number last digit
# print(sum)

# 16 Reverse a number using slicing
# a=int(input('enter number'))
# b=str(a) # int convert to string
# c=b[::-1] #call to last to first slicing using
# print(c)

# #reverse of number using maths callculation
# a=int(input('enter number'))
# rev=0 #123
# while a>0: # comapre 123>0 trues goes down
#     rem=a%10  # 123%10 =get last number
#     rev=rev*10+rem #rev 3*10
#     a=a//10
# print(rev)

#17 Check if number is a palindrome
# a=int(input('enter number'))
# b=a
# rev=0
# while a>0:
#     rem=a%10
#     rev=rev*10+rem
#     a=a//10
# print(rev)
# if rev==b:
#     print('it is a plandrome')
# else:
#     print('not plandrome')

# 18 armstrong number
# a=int(input('enter number')) # taken varible
# b=str(a) # convert int to str
# lenn=len(b) # find the length
# arm=0 # intially 0
# c=a # heps to comapre arm andc
# while a>0: # check the number >0 or not
#     rem=a%10  #321 1 # get last digit
#     arm=arm+rem**lenn #1*len # main logic arm+rem**len
#     a=a//10          # to remove last digit
# if arm==c: # checking condition
#     print('armstrong')
# else:
#     print('not armstrong' )


#19 Count vowels in a string 
# a=input('enter string') # takes string
# count=0 # it add tem varible
# for b in a: # string sepeartion helps
#     if b in 'A,E,I,O,U,a,e,i,o,u': # they present or not logic
#         count=count+1 # counting
# print(count) # display

# 20 Check if string  is a palindrome using slice
# a=input('enter string')
# b=a[::-1]
# if a==b:
#     print('the string is plandrome')
# else:
#     print('not a plandrome')
  
#without using slice
# a=input('enter string')
# b=''
# for c in a:
#  b=c+b  #c+b must write 
# if b==a:
#     print("the string is plandrome")
# else:
#     print('the string is not  a palandrome')

# #21 Convert binary to decimal
# binary=input('enter binary number')
# decimal=int(binary,2) # 2is a base positon so 2cube +2square+2power1+2power 0
# print(decimal)
 
 #another method
# binary=input("enter decimal number") #taken binary number
# power=len(binary)-1 #lenght of power 
# decimal=0 # decimal intial taken 0
# for digit in binary: #each number seperate
#     decimal=decimal+int(digit)*(2**power) #string convert into int and mutlipy with power
#     power=power-1 #decrease power beach ecah digit descrese
# print(decimal) # output

# #22 decimal to binary
# decimal=int(input("enter decimal number"))
# c=bin(decimal)
# print(c[2:]) # remove 0b

# without using function using number/2 = 0/1
# decimal=int(input('enter decimal number'))
# binary=''
# if decimal==0:
#     binary='0'
# else:
#     while decimal>0: # main decimal
#         rem=decimal%2 # check reminder 0 or 1
#         binary=str(rem)+binary # addition
#         decimal=decimal//10 # remove decimal each digit
# print(binary)
   
# #23 Find ASCII value of a character
# a=input('enter single charcter')
# print(ord(a)) # character to word ord it has single parmter

# #24find hcf of a number
# a=int(input('enter number')) # read number
# b=int(input('enter number')) #reaad 2nd nuber
# while a%b!=0: # check a%b!=0 it check simply remainder corct or wrong
#     rem=a%b  # check rem
#     a=b # swap
#     b=rem
# print(b)

# #25 lcm of number
# a=int(input("enter number")) # 
# b=int(input("enter number"))
# for i in range(1,a*b+1): #range of numbers
#  if i%a==0 and i%b==0: #condion  i check divisible by both or not
#         break
# print(i)
 
# #26 Print ASCII characters from 65 to 90
# for i in range(65,90+1):
#     print(chr(i),end='')

# #27calculate simple intrest
# p=int(input('enter principal'))
# t=int(input('time in months'))
# r=int(input('rate of intrest'))
# simple=p*t*r/100
# print(simple)


#28 compound intrest
#formula we need
#A=P(1+r/n)**n*t
# p=int(input('enter prinicpal'))
# r=int(input('rate of intrest'))
# n=int(input('number of times compund in a year'))
# t=int(input('enter time'))
# a=p*(1+r/n)**(n*t)
# ci=a-p
# print(a)
# print(ci)

# #29Print first N natural numbers
# a=int(input('enter range'))
# for j in range(1,a+1):
#     print(j)

#or
# a=int(input('enter number'))
# num=0
# while num<a:
#     num=num+1
#     print(num)

# #29Print all prime numbers between two numbers
# a=int(input('enter start number'))
# b=int(input('enter end number'))
# for num in range(a,b+1):
#     if num>1:
#         for j in range(2,num):
#            if num%j==0:
#                  break
#         else:
#             print(num)
               
# a=int(input('enter number'))  # just remebering prime number
# count=0
# for num in range(1,a+1):
#     if a%num==0:
#         count=count+1
# if count==2:
#     print('the num is prime')
# else:
#     print('not prime')  

# #30 Generate a random number  # in random module they has no range so we use randint and give 2 parameter
# import random as r
# print(r.randint(0,1000))

#31 import random
# for j in range(10):             # multiple numbers print
#     print(random.randint(0,100))

# #32find square root formula sqrt=0.5**num
# a=int(input('enter number'))
# squrt=a**0.5 #** not a multpliaction it a exponition
# print(squrt)
# or 
# a = float(input("Enter number: "))

# # Handle 0 and 1 quickly
# if a == 0 or a == 1:
#     sqrt = a
# else:
#     # Binary search approach
#     start = 0
#     end = a
#     precision = 0.00001  # desired precision
#     while (end - start) > precision:
#         mid = (start + end) / 2
#         if mid * mid < a:
#             start = mid
#         else:
#             end = mid
#     sqrt = (start + end) / 2

# print("Square root of", a, "is approximately:", sqrt)

# #33Calculate power of a number
# base=int(input('enter base number'))
# exponent=int(input('enter number'))
# power=base**exponent
# print(power)

#34Sum of first N odd numbers
# sum=0
# a=int(input('enter number to range of number  '))
# for num in range(1,a+1):
#     if num%2!=0:
#         sum=sum+num
# print(sum)

# #35 sum of first n even numbers
# sum=0
# a=int(input('enter range'))
# for num in range(1,a+1):
#     if num%2==0:
#         sum=sum+num
# print(sum)

# #35  right angle traingle
# for i in range(5):    # rows 5 outer loop
#      for j in range(i):    # inner columns loop
#         print("*",end="")  # end= it give elemnts in same line
#      print()

# #36 right angle traingle inverted
# for i in range(5): # 5 rows
#     for j in range(5-i):
#         print('*',end=" ")
#     print()

# #37  number pattern
# a=int(input())
# b=0
# for i in range(a):
#   b=b+1
#   for j in range(3):
#      print(b,end="")
#   print()

# for i in range(5):
#     for j in range(i):
#         print("*",end='')
#     print()


# #40 Count characters in a string
# a=input('enter word')
# count=0
# special="!@#%^&*()_+:<>,{}[]|\':"
# for b in a: 
#         if b in special:
#                 count=count+1
# print(count)

#41Reverse a string
# a=input('enter word') # input word
# b=''   # empty space
# for c in a: # loop
#     b=c+b # c+ 
# print(b)

#42 cout words in a string without function
# a='harsha vardhan name is yours'
# count=1
# for b in a:
#     if b in ' ':
#         count=count+1
# print(count)

# #using function
# a="harsha vardhan namasta vanakam vunava poyava"
# words=a.split()
# print(words)
# print(len(words))

# # 43 Replace vowels with a symbol
# a="harshavardhan"
# sym='&'
# for b in a:
#     if b in 'aeiouAEIOU':
#         print(sym,end="")
#     else:
#         print(b,end='')

# #44Remove punctuation from string
# a=input('enter string')
# b=',./?!@'
# for ch in b:
#     a=a.replace(ch,'')
# print(a)

# a=input('enter string')
# str=" "
# b='/,.;/,/.'
# for c in a:
#     if c not in b:
#      str=str+c
# print(str)

# #45sort list of numbers
# a=[3,1,8,9,3,2]
# #only written for itteresation
# for i in range(len(a)): # total interation
#  for j in range(len(a)-1): # loop for indexing comparisson
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
   
#47 Find max and min in a list
# a=[1,80,90,200,2,5,3,1000,0,555,5555] # user input
# for i in range(len(a)):  # outloop runs n time
#     for j in range(len(a)-1): # compares adjacent sides
#         if a[j]>a[j+1]: # logic
#             a[j],a[j+1]=a[j+1],a[j] # swap
# print(a[0],a[-1]) # index

# #48 Remove duplicates from list
# a=[1,1,2,2,2,3,4,5,6,6,7,8,9,11,12,15,15] # list
# b=[] #dummy list
# for i in a: # one by one
#     if  i not in b: # not present 
#         b.append(i) # the will append
# print(b)

# #49 Count occurrences of element in list
# a=[1,1,2,2,3,3,4,4,5,5,5,6,6,7,8,9] # list given
# counts={} #  empty dictonary
# for i in a:   # loop through each element in list
#     counts[i]=counts.get(i,0)+1 # update disctonary count
# print(counts) # final

# #Merge two lists
# a=[1,2,4,9,10,20]
# b=[20,30,50,80,90]
# print(a+b)
# output [1, 2, 4, 9, 10, 20, 20, 30, 50, 80, 90]

# a=[3,4,5]
# b=[1,2,3]
# a.extend(b) # extend function
# print(a)

# a=[1,2,3]
# b=[4,5,6]
# d=[]
# for i in a:
#     d.append(i)    # using loop style

# for j in b:
#     d.append(j)
# print(d)
    

# # 51 sum of elements in a list
# a=[1,20,30,50,80,100,200,800]
# sum=0
# for k in a:
#     sum=sum+k
# print(sum)

# #52Find second largest number in list
# a=[1,18,50,45,43,12,3]
# for i in range(len(a)): # use range not in in check they are present or not external loop no of passes
#     for j in range(len(a)-1): # this loop use for sawap
#         if a[j]>a[j+1]: # swap condition
#             a[j],a[j+1]=a[j+1],a[j] # swap process
# print(a)
# print(a[-2])


#53reverse a list
# a=[1,2,3,4,5,6,7,8,9]
# # print(a[::-1])

# a=[1,2,3,4,5,6,7,8,9,10]  
# b=[]
# c=len(a)-1
# for i in range(len(a)):
#     b.append(a[c])
#     c=c-1
# print(b)

# 54 Sort a dictionary by values
# a={1:'apple',2:'ball',5:'cat',4:'dog'}
# print(sorted(a.items()))

# perfect number
# a=int(input('enter number'))
# sum=0
# for x in range(1,a):
#     if a%x==0:
#         sum=sum+x
# if sum==a:
#     print('perferct number')
# else:
#     print('not perfect number')

#harshad number 18
# a=18
# sum=0
# b=a
# while a>0:
#     rem=a%10
#     sum=sum+rem
#     a=a//10
# if b%sum==0:
#     print('harshd number')
# else:
#     print('not')


#dic creation
# name_numbers={2:787288102,5:18390193,1:72891902,3:902093000}
# print(name_numbers) # dictionary
# print(type(name_numbers)) # type tell
# print(name_numbers[5]) # retervive the key valudes not index
# name_numbers[5]=11111 # modifictaions of dectionary
# print(name_numbers)
# print(sorted(name_numbers)) # only key will be sorted and display key only
# print(sorted(name_numbers.items())) # soretd all items
# print(sorted(name_numbers.keys())) # sorted only keys
# print(sorted(name_numbers.values())) # sorted only values
# print(sort(name_numbers)) # sort works only list

# for x,y in name_numbers.items():
#     print(x,y)

# 2 787288102
# 5 18390193
# 1 72891902
# 3 902093000
 

# only values
# for x in name_numbers.values():
#     print(x)
# 787288102
# 18390193
# 72891902
# 902093000


# for x in name_numbers:
#     print(x)
# 2
# 5
# 1
# 3


#55 merger two dicts
#a={'h':'harsha','s':'sasi','d':'don'}
# b={'b':'banana','c':'cat','e':'elephant'}
# c=a|b #pipe operator symbol for OR/union/merge
# print(c)

#another method
# a={1:'abc',2:'bca',3:'def'}
# b={4:'hahha',5:'rathahru'}
# c=a.copy() # copy
# c.update(b) # update
# print(c)
    
# #another method
# a={1:'abc',2:'52662'}
# b={3:'gyhjl',5:'uyih'}
# b.update(a)
# print(b)

# #56 Access elements of a tuple
# a=(1,2,3,10,20,30)
# print(a[0])
# print(a[2])
# print(a[0:4])
# for b,d in enumerate(a): # using enumarte we get both index and slicing opertators
#     print(b,d)

#57Convert tuple to list and vice versa
# a=(2,3,4,10,20,304,50)
# b=list(a)
# print(b)

#
# #57Convert tuple to list and vice versa
# a=(2,3,4,10,20,304,50)
# b=list(a)
# print(b)

# # #57Convert tuple to list and vice versa without buildin
# a=(2,3,4,5,10,20,30,40)
# b=[]
# for c in a:
#     b.append(c)
# print(b)

#58 Use set operations (union, intersection)
# a={1,20,30,50,79,90}
# b={1,3,20,30,99,100}
# print(a.union(b)) #all elements
# print(a.intersection(b)) #common elements in bot sets

#59 sCount frequency of characters    -------  using counter module
# from collections import Counter using method
# a="banana"
# b=Counter(a)
# print(b)
    
#count frequency in general method 

# a="banana" # input
# char={} # empty dictionary
# for freq in a: # line by line  
#     char[freq]=char.get(freq,0)+1 # we use  frequ is works like key and 0+1 is works values
# print(char)

# #60 Check if key exists in dictionary
# a={"a1":"apple","b":"ball","c":"cat","d":"dog"}
# b= input("enter key")
# if (b in a):      # in operator  it checks b elements is present in a or not
#    print("the  key is exist")
  
# else:        
#     print("the key is not exist")
    

# #61 Print keys and values in dictionary
# items={"a":"apple","b":"ball","c":"cat","d":"dog"}
# for key,values in items.items():
#         print(key,values)

# a apple
# b ball
# c cat
# d dog

# #62 Take user input and print
# a=input("enter what do you want")
# print(a)

#62 Use default function arguments


