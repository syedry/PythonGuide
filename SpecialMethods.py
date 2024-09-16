#Special methods begin and end with dunder(Double underscore)
#Example - __init__ , __str__ , __len__ , __eq__ , __contains__
#__str__ controls how your object is converted to a string representation for output when you print() something
#__len__ returns the length of the object or collection.
#__contains__ tests whether the object contains an item.
#__eq__ tests whether two objects are equal.


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)
    

honeycrisp = Apple("red", "sweet")
print(honeycrisp)
