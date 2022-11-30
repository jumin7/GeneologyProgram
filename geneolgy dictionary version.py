
"""make a list of first name, last name, dob for each section of family 
edit or qury function
add or remove inside edit
inside add, which section of the family and remove
takeout serie number from the list, 
query means look up or display

"""
firstname_user= []
lastname_user = []
dob_user =[]

firstname_parent=[]
lastname_parent= []
dob_parent =[]

firstname_grandparent =[]
lastname_grandparent =[]
dob_grandparent = []

firstname_sibling =[]
lastname_sibling =[]
dob_sibling =[]


def main():
    firstname = input((" Enter your first name"))
    firstname_user.append(firstname)
    lastname= input(("Enter your last name"))
    lastname_user.append(lastname)
    dob = str(input("Enter your date of birth in mm/dd/yyyy"))
    dob_user.append(dob)
    geneolgy_options()

#GENEOLOGY OPTIONS
def geneolgy_options():
    option = input("Enter if you want to 'E' if you want to edit or enter 'Q' for query")
    if option== "E":
        edit_tree()
    elif option == "Q":
        query_tree()
    else:
        print ("ERROR \n. Make sure you capitalize!")
        geneolgy_options()

# End or Conitnue the program
def end_or_continue():
    result= input("Press 'C' if you want to continue and 'X' if you want to exit")
    if result == "C":
        geneolgy_options()
    elif result == "X":
        print ("You are leaving")
    else:
        print ("Something went wrong")
        end_or_continue()

# Adding the parent
def add_parent():
    first_name_parent = input("Enter the first name of the parent you want to add")
    firstname_parent.append(first_name_parent)
    last_name_parent = input ("Enter the last name of your parent")
    lastname_parent.append (last_name_parent)
    dob_parent_to_add = input("Enter the date of birth of your grand parent in dd/mm/yyyy format")
    dob_parent.append (dob_parent_to_add)
    print ("Succesfully added")
    end_or_continue()

def remove_parent():
    first_name_remove = input ("Enter the first name of the person you want to remove")
    for x in firstname_parent:
        if x == first_name_remove:
            serienum = firstname_parent.index(x)
            firstname_parent.remove(x)
            lastname= lastname_parent[serienum]
            lastname_parent.remove (lastname)
            dob= dob_parent[serienum]
            dob_parent.remove (dob)
            print ("Succesfully Removed")

def add_grandparent():
    first_name_gparent_toadd = input("Enter the first name of the grandparent you want to add")
    firstname_grandparent.append(first_name_gparent_toadd)
    last_name_gparent_toadd = input ("Enter the last name of your grandparent")
    lastname_grandparent.append (last_name_gparent_toadd)
    dob_grandparent_to_add = input("Enter the date of birth of your grand parent in dd/mm/yyyy format")
    dob_grandparent.append (dob_grandparent_to_add)
    print ("Succesfully added!")
    end_or_continue()

def remove_grandparent():
    first_name_remove = input (" Enter the first name of the person you want to remove")
    for x in firstname_grandparent:
        if x == first_name_remove:
            serienum = firstname_grandparent.index(x)
            firstname_grandparent.remove(x)
            lastname= lastname_grandparent[serienum]
            lastname_grandparent.remove (lastname)
            dob= dob_grandparent[serienum]
            dob_grandparent.remove (dob)
            print (" Succesfully Removed")

def add_siblings():
    first_name_sibling_toadd = input("Enter the first name of the sibling you want to add")
    firstname_sibling.append(first_name_sibling_toadd)
    last_name_sibling_toadd = input ("Enter the last name of your sibling")
    lastname_sibling.append (last_name_sibling_toadd)
    dob_sibling_toadd = input ("Enter the date of birth of your sibling")
    dob_sibling.append(dob_sibling_toadd)
    print ("Succesfully added!")
    end_or_continue()

    end_or_continue()

def remove_sibling():
    first_name_remove = input (" Enter the first name of the person you want to remove")
    for x in firstname_sibling:
        if x == first_name_remove:
            serienum = firstname_sibling.index(x)
            firstname_sibling.remove(x)
            lastname= lastname_sibling[serienum]
            lastname_sibling.remove (lastname)
            dob= dob_sibling[serienum]
            dob_sibling.remove (dob)
            print (" Succesfully Removed!")
    
# Edit tree to add or remove
def edit_tree():
    edit = input("Enter 'R' if you want to remove somebody or enter 'A' if you want to add someboy")
    which_section = input (" Enter 'S' for sibling, 'P' for parent and 'G' for grandparents")
    if edit == "R":
        if which_section == "S":
            remove_sibling()
        elif which_section == "P":
             remove_parent()
        elif which_section == "G":
            remove_grandparent()
        else:
            print ("Invalid option")
            edit_tree()
    elif edit== "A":
        if which_section == "S":
            add_siblings()
        elif which_section == "P":
             add_parent()
        elif which_section == "G":
            add_grandparent()
        else:
            print ("Invalid option")
            edit_tree()
    else:
        print ("ERROR")
        edit_tree()

def lookup_tree():
    look_name = input("Enter the first name of the person you wan to look up")
    found = False
    for i in firstname_parent:
        if look_name== i:
            found = True
            serienum = firstname_parent.index(i)
            lastname= lastname_parent[serienum]   
            dob= dob_parent[serienum] 
            print (i,lastname,"is the parent. They were born on ",dob)

    for i in firstname_sibling:
        if look_name== i:
            found = True
            serienum = firstname_sibling.index(i)
            lastname= lastname_sibling[serienum]   
            dob= dob_sibling[serienum] 
            print (i,lastname,"is the sibling . They were born on",dob)

    for i in firstname_grandparent:
        if look_name== i:
            found = True
            serienum = firstname_grandparent.index(i)
            lastname= lastname_grandparent[serienum]   
            dob= dob_grandparent[serienum] 
            print (i,lastname,"is the grand parent. They were born on ",dob)

    if not found:
        print ("Person Not Found")

def query_tree():
    choice= input("If you want to display the geneology, type 'D', and if you want to look up type 'L'")
    if choice == "D":
        display_tree()
    elif choice == "L":
        lookup_tree()
    else:
        print ("Invalid answer")
        query_tree()

def display_tree():
    print( "Genealogy for:")
    for i in range(len(firstname_parent)):
        print(
            firstname_user[0].ljust(12),
            lastname_user[0].ljust(12), 
            str(dob_user[0].rjust(5))
        )

    print( "\nParents:")
    """for i in range(len(firstname_parent)):
        print(firstname_parent[i],lastname_parent[i], dob_user[i].rjust(10))"""
    for i in range(len(firstname_parent)):
        print(
            firstname_parent[i].ljust(12),
            lastname_parent[i].ljust(12),
            str(dob_parent[i].rjust(5))
        )

    print ("\nGrandparents:")
    for i in range(len(firstname_grandparent)):
        print(
            firstname_grandparent[i].ljust(12),
            lastname_grandparent[i].ljust(12),
            str(dob_grandparent[i].rjust(5))
        )


    print( "\nSiblings:")
    """for i in range(len(firstname_sibling)):
        print(firstname_sibling[i], lastname_sibling[i], dob_sibling[i].rjust(10))"""
    for i in range(len(firstname_sibling)):
        print(
            firstname_sibling[i].ljust(12),
            lastname_sibling[i].ljust(12),
            str(dob_sibling[i].rjust(5))
        )
    
main()    


