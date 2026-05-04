'''
for i in range(1,6,1):
    if i==3:
        break
    print(i)
    
for i in range(1,6,1):
    if i==3:
        continue
    print(i)
    
for i in range(1,6,1):
    if i==3:
        pass
    print(i)

for i in range(1,21,1):
    if i%2!=0:
        continue
    print(i)
'''
#string accessing
'''
a = "python class"
print(a)
print(a[5])
print(a[0:6])
print(a[7:12])
print(a[-1])
print(a[0:])
print(a[:12])
print(a[:])
print(a[::-1])

#case conversion
a = "PYTHON class"
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())

#alignment
print("hi".center(10))
print("hi".ljust(5))
print("hi".rjust(5))
print("12".zfill(5))

#trimming
a= "      hi  hi hi       "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

#splitting join

a="This is a python programming class"
print(a.split())
a="This.is.a.python.programming.class"
print(a.split('.'))
c = a.split('.')
print(''.join(c))
print(' '.join(c))

#search and replace
a="python programming"
print(a.find('o'))
print(a.rfind('o'))
print(a.find('z'))
print(a.index('n'))
#print(a.index('z'))
a=a.replace('n','&')
print(a)
print(a.count('m'))
print("m@gmail.com".endswith("@gmail.com"))
print("+919384542020".startswith("+91"))

#testing
print("Mounika".isalpha())
print("9876543210".isdigit())
print("TN30".isalnum())
print(" ".isspace())
print("PYTHON".isupper())
print("python".islower())
print("Python Class".istitle())

a="man"
if a==a[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

digit=0
letter=0
space=0
symbol=0
a=str(input("Enter a String"))
for i in a:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        letter+=1
    elif i.isspace():
        space+=1
    else:
        symbol+=1
print("No.of.Digit   :",digit)
print("No.of.Letters :",letter)
print("No.of.Space   :",space)
print("No.of.Symbols :",symbol)
