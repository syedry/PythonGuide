#Check output to know more about formatting strings based on required parameters

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

#Aligning the text fields
celsius=32.22
farhenhiet=90
print("{:>3}F | {:>6.2f}C".format(farhenhiet,celsius))