'''
#defining a function
def add():
    a=10
    b=10
    print(a+b)
add()

#parameter
def addition(m,n,a): #parameter
    print(m+n+a)
a=10
addition(1,2,a) #argument

a=10 #global variable
def addition(m,n):
    x=10 #local variable
    print(x)
    print(m+n+a)
    
addition(1,2)
print(x)

#positional argument
def course(c_n,c_d):
    print("Course Name :",c_n,"\nCourse Duration :",c_d)
course("Python","60 hrs")

#default arguments

def user_details(un="Guest"):
    print("Username :",un)
user_details("Mounika")

#keyword argument
def add(a,b,c):
    print("A:",a)
    print("B:",b)
    print("C:",c)
add(b=20,c=25,a=10)

def user_details(un="Guest",mail="mail@gmail.com",phone="+91xxxxxxxxxx"):
    print("Username :",un,"\nMail Id  :",mail,"\nPhone no :",phone)

user_details(mail="livewiremounika@gmail.com",phone="+919384542020")

#variable length argument
def sum1(*x):
    s=0
    for i in x:
        s=s+i
    print(s)
sum1(1,2,3,4,5,6,7)

def details(**d):
    for i in d:
        print(i," : ",d[i])
details(id1="name1",id2="name2",id3="name3",id4="name4")

#return type
def add(a,b):
    return a+b
x=add(1,20)
print(x)
print(add(15,23))

#without return , without parameter
def demo1():
    a=10
    b=20
    print(a+b)
demo1()

#without return , with parameter
def demo1(a,b):
    print(a+b)
a=10
b=20
demo1(a,b)

#with return , without parameter
def demo1():
    a=10
    b=20
    return a+b
print(demo1())

#with return , with parameter
def demo1(a,b):
    return a+b
print(demo1(15,23))

#lambda functions

a = lambda x : x*x
print(a(5))

#map function
def isOdd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
a = [1,2,1,4,6]
s = list(map(isOdd,a))
print(s)

#filter function
def isOdd(n):
    if n%2!=0:
        return n
a = [1,2,5,3,6]
s = list(filter(isOdd,a))
print(s)
'''
#recursion
def hi():
    print("hi")
    hi()
hi()
