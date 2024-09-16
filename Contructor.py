#Each time you create an instance of a class, Python calls a special class method the constructor. 
#The constructor’s job is to set up the object, meaning that instance of the class, so it’s ready to be used. 
#Usually this means initializing some variables and doing other simple housekeeping.

class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"

honeycrisp = Apple()
print(honeycrisp.color)