'''
for i in range(1,11,1):
    print("hi")

for i in range(1,6,1):
    print(i)

i   i<6       o/p    i=i+1
1   1<6->T    1      i=1+1=2
2   2<6->T    2      i=2+1=3
3   3<6->T    3      i=3+1=4
4   4<6->T    4      i=4+1=5
5   5<6->T    5      i=5+1=6
6   6<6->F ----> terminate

#1 3 5 7 9
for i in range(1,11,1):
    if i%2!=0:
        print(i)

# 5 4 3 2 1

for i in range(5,0,-1):
    print(i)

for i in range(10,0,-2):
    print(i,end=" ")


n = int(input("Enter a num"))
for i in range(1,n+1,1):
    print(i)

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for j in range(1,6,1):
    for i in range(1,6,1):
        print("*",end=" ")
    print()

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

for j in range(1,6,1):
    for i in range(1,6,1):
        print(i,end=" ")
    print()

# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

for j in range(1,6,1):
    for i in range(1,6,1):
        print(j,end=" ")
    print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

for j in range(1,6,1):
    for i in range(1,6,1):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#          
#  * * *   
#  * * *   
#  * * *   
#          

for j in range(1,6,1):
    for i in range(1,6,1):
        if i==1 or i==5 or j==1 or j==5:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
'''
#*
#* *
#* * *
for j in range(1,6,1):
    for i in range(1,j+1,1):
        print("*",end=" ")
    print()

for j in range(1,6,1):
    for i in range(1,6,1):
        if i+j<=6:
            print("*",end=" ")
    print()

for j in range(1,6,1):
    for i in range(1,6,1):
        if i+j>=6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
