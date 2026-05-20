#write mode
file = open(r"C:\Users\Livewire\Desktop\bill.docx","w")
file.write("hi")
a=input("Enter a data :")
file.write(a)
file.close()

#append mode
file = open(r"C:\Users\Livewire\Desktop\bill.docx","a")
file.write("hi")
a=input("Enter a data :")
file.write(a)
file.close()

#read mode
file = open(r"C:\Users\Livewire\Desktop\bill.docx","r")
print(file.read())
print(file.read(44))
print(file.readline())
print(file.readline(1))
print(file.readlines())
print(file.readlines(3))
print(file.name)
print(file.mode)
file.close()

import os
print(os.getcwd())
print(os.listdir())
#os.rename("1130.docx","dharanishwaran.txt")
os.remove(r"C:\Users\Livewire\Desktop\1130.docx")
