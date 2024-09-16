"""Showing 3 different outputs for experimenting with strings with the print function"""

greeting="Hello! I'm getting good at this."
index=0
while index<len(greeting):
    print(greeting[index])
    index+=1
print()

index=0
while index<len(greeting):
    print(greeting[index:index+2])
    index+=1
print()

index=0
while index<len(greeting):
    print(greeting[index],end="")
    index+=1