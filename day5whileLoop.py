'''
n = int(input("Enter the count : "))
for i in range(1,n+1,1):
    name = input("Enter the Student name :")
    age = int(input("Enter the age :"))
    print("Student",i," ",name)
    print("Student",i," ",age)

k = 1
while k<=5:
    print(k)
    k+=1
    
k = 5
while k>=1:
    print(k)
    k-=1 

i=1
while i<=5:
    k = 1
    while k<=5:
        print(k,end=" ")
        k+=1
    print()
    i+=1
    
#sum of digits
n = int(input("Enter a number :"))
s = 0
while n>0:
    r = n%10
    s = s + r
    n = n//10
print(s)
'''
#count the digits
n = int(input("Enter a number :"))
c = 0
while n>0:
    n = n//10
    c = c + 1
print(c)














