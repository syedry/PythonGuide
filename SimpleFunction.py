def print_fullname(first,last):
    if (len(first)<2) or (len(last)<2):
        print ("Name cannot be less than 2 characters")
    else:
        print ("Full Name : "+first+' '+last)

first_name='S'
last_name='Rizwan Yasin'
print_fullname(first_name,last_name)