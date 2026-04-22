#write a program to find smallest number among two given integers
'''
a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
if a<=b:
    print(a,"IS THE SMALLEST VALUE")
else:
    print(b,"IS THE SMALLEST VALUE")


a = int(input("Enter a number :")) #a=-10
if a>0:
    print(a)
else:
    print(-(a))#print(-(-10))->print(10)


a = int(input("Enter a number :"))
if a%10==0:
    print("yes")
else:
    print("no")

a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
c = int(input("Enter a number :"))
if a>=b and a>=c:
    print(a,"IS THE LARGEST VALUE")
elif b>=a and b>=c:
    print(b,"IS THE LARGEST VALUE")
elif c>=a and c>=b:
    print(c,"IS THE LARGEST VALUE")
else:
    print("Invalid")

ch = str(input("Enter a character :"))
if ch>='a' and ch<='z':
    #v = ['a','e','i','o','u']
    #if ch in v:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        print("vowel")
    else:
        print("consonant")
else:
    print("It is not a alphabet")
'''

a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
s = str(input("Enter a operator (+ , - , * , /) :"))
if s == '+':
    print(a+b)
elif s == '-':
    print(a-b)
elif s == '*':
    print(a*b)
elif s == '/':
    print(a/b)
else:
    print("Invalid Operator")

    
