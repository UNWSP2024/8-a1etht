#Programmer: Alethea Lo
#Date: 3/16/25
#Title: Initials

def get_initials(name):
    name_parts = name.split()
    initials = [part[0].upper() + '.' for part in name_parts]
    return ' '.join(initials)

#User Input
full_name = input("Enter your first, middle, and last name: ")

#Displaying the results
print("Your initials are:", get_initials(full_name))
