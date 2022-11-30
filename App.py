#Genealogy Program
#By Jumin Shrestha
#worked: lookup name
# Project 2

from graphics import *
from Person import *

user = []

parents = []

grandparents = []

siblings = []

win = GraphWin("Geneology", 600, 600)
win.setCoords(0, 5, 5, 0)

def main(): 
    
    print("Welcome, this is a program that lets you make a Geneology Tree!")
    greet = "Welcome, this is a program that lets you make a Geneology Tree! Enter L to load file or N for new"
    out = Text(Point(2.2,0.25),greet)
    out.draw(win)
    textEntry = Entry(Point(0.5,0.5),2)
    textEntry.draw(win)
    win.getMouse()
    load = textEntry.getText()
    win.getMouse()
    out.undraw()
    textEntry.undraw()

    if load == "L" or load == "l":
        open_file()
    elif load == "N" or load == "n":
        user_name = input("Enter your name and birth date separated by comma. (name, birthday)")

        """d = Text(Point(1.5,1),username)
        d.draw(win)
        textEntry = Entry(Point(1,1.2),30)
        textEntry.draw(win)
        win.getMouse()
        user_info= textEntry.getText()
        textEntry.undraw()"""

        try:
            user_info = user_name.split(",")
            user1 = Person(user_info[0], user_info[1], "user")
            user.append(user1)
            geneolgy_options()
        except IndexError:
            print("Make sure you entered birthday after the comma! Try again")
            main()
    

#GENEOLOGY OPTIONS
def geneolgy_options():
    option = input("Enter if you want to 'E' if you want to edit or enter 'Q' for query")
    if option == "E" or option == "e":
            edit_tree()
    elif option == "Q" or option == "q":
            query_tree()
    else:
        print("ERROR Invalid Command Input, at geneology options")
    


#creating file
def file_making():  
    create_file = open ("geneolgy.txt","w")
    print("The geneology file")
    user_line = ""
    for u in range(len(user)):
        user_out = user[u].name + "," + user[u].birthday #taking the name and bday from the class
        user_line = user_line + ":" + user_out
    print(user_line[1:], file = create_file)

    sib_line = ""
    sib_intro = "The siblings are:"
    for s in range(len(siblings)):
        sib_out = siblings[s].name + "," + siblings[s].birthday
        sib_line = sib_line + ":" + sib_out
    print(sib_intro, sib_line[1:], file = create_file)

    par_line = ""
    par_intro = "The parents are:"
    for p in range(len(parents)):
        par_out = parents[p].name + "," + parents[p].birthday
        par_line = par_line + ":" + par_out
    print(par_intro, par_line[1:], file = create_file)

    gpar_line = ""
    gpar_intro = "The grandparents are:"
    for g in range(len(grandparents)):
        gpar_out = grandparents[g].name + "," + grandparents[g].birthday
        gpar_line = gpar_line + ":" + gpar_out
    print(gpar_intro, gpar_line[1:],file = create_file)

    create_file.close

# End or Conitnue the program
def end_or_continue():
    result = input("Press 'C' if you want to continue with eiditng , 'S' if you want to save in a file and 'X' if you want to exit")
    if result == "C" or result == "c":
        geneolgy_options()
    elif result == "S" or result == "s":
        file_making()
        print ("Saved!")
        #end_or_continue()
    elif result == "X":
        print ("Bye Bye")
    else:
        print ("Invalid Command Entry.")
        end_or_continue()

#updated
def add_parent():
    parent = input("Enter the new person's name and birth date separated by comma. (name, birthday)")
    try:
        parent_info = parent.split(",")
        parent1 = Person(parent_info[0], parent_info[1], "parent" )
        parents.append(parent1)
        print ("Succesfully added")
    except IndexError:
        print("You did not entry properly. Make sure you entered birthday after the comma! Try again")
        add_parent()
    end_or_continue()

def remove_parent():
    remove = input ("Enter the first and last name of the parent you want to remove")
    for p in range(len(parents)):
        if remove == parents[p].name: 
            del parents[p]
            print (" Succesfully Removed!")
        else:
            print ("Something went wrong when removing the parent")


def add_grandparent():
    gpar = input("Enter the new person's name and birth date separated by comma. (name, birthday)")
    try:
        gpar_info = gpar.split(",")
        gpar1 = Person(gpar_info[0], gpar_info[1], "grandparent" )
        grandparents.append(gpar1)
        print ("Succesfully added!")
    except IndexError:
        print("Make sure you entered birthday after the comma! Try again")
        add_grandparent()

    end_or_continue()

def remove_grandparent():
    remove = input ("Enter the first and last name of the grandparent you want to remove")
    for g in range(len(grandparents)):
        if remove == grandparents[g].name: 
            del grandparents[g]
            print ("Succesfully Removed!")
        else:
            print ("Something went wrong when removing the grandparent")


def add_siblings():
    sibling = input("Enter the new person's name and birth date separated by comma. (name, birthday)")
    try:
        sib_info = sibling.split(",")
        sib1 = Person(sib_info[0], sib_info[1], "sibling" )
        siblings.append(sib1)
        print ("Succesfully added!")
    except IndexError:
        print("Make sure you entered birthday after the comma! Try again")
        add_siblings()

    end_or_continue()

def remove_sibling():
    remove = input(" Enter the first and last name of the sibling you want to remove")
    for s in range(len(siblings)):
        if remove == siblings[s].name: 
            del siblings[s]
            print (" Succesfully Removed!")
            end_or_continue()
        else:
            print ("Something went wrong when removing the sibling")

    
    

# Edit tree to add or remove
def edit_tree(): #UPDATED
    edit = input("Enter 'R' if you want to remove somebody or enter 'A' if you want to add someboy")
    section = input("Enter 'S' for sibling, 'P' for parent and 'G' for grandparents")
    if edit == "R" or edit == "r":
        #remove_name = input("Enter the first and last name of the person you want to remove")
        #Person.remove(remove_name)
        if section == "S" or section == "s":
            remove_sibling()
        elif section == "P" or section == "p":
             remove_parent()
        elif section == "G" or section == "g":
            remove_grandparent()
        else:
            print ("Invalid option")
            edit_tree()
    elif edit == "A" or edit == "a":
        if section == "S" or section == "s":
            add_siblings()
        elif section == "P" or section == "p":
             add_parent()
        elif section == "G" or section == "g":
            add_grandparent()
        else:
            print ("Invalid option")
            edit_tree()
    else:
        print ("ERROR")
        edit_tree()

#updated
def lookup_tree(): 
    try:
        look_name = input("Enter the full name of the person you are looking for")
        for p in range(len(parents)):
            if look_name == parents[p].name:
                print (look_name," is a parent who was born on:")
                print (parents[p].birthday)
            else:
                pass

        for s in range(len(siblings)):
            if look_name == siblings[s].name: 
                print (look_name," is a sibling who was born on:")
                print (siblings[s].birthday)
            else:
                pass

        for g in range(len(grandparents)):
            if look_name == grandparents[g].name:
                print (look_name," is a grandparent who was born on:")
                print (grandparents[g].birthday)
            else: 
                pass
    except:
        print ("Person not found. Please try again and remember it is case sensitive!")
        lookup_tree()


def open_file():
    
    infile = open('geneolgy.txt',"r")
    data = infile.read()
    #print (data)
    screen = Text(Point(2,2),data)
    screen.draw(win)
    win.getMouse()

    infile.close()
    end_or_continue()


#updated
def query_tree():
    choice = input("If you want to display the geneology, type 'D', and if you want to look up type 'L' and 'F' to search file")
    if choice == "D" or choice == "d":
        display_tree()
    elif choice == "L" or choice == "l":
        lookup_tree()
    elif choice == "F" or choice == "f":
        open_file()
    else:
        print ("Invalid answer")
        query_tree()

#updated
def display_tree(): 
    
    print( "Genealogy for:")
    u_intro = "The following is the family tree of: \n"
    userstuff = user[0].name + " , "+ user[0].birthday
    outuser = u_intro + userstuff
    display = Text(Point(1,0.5),outuser)
    display.draw(win)
    
    print ("\nGrandparents:")
    gpar = ""
    outgpar = ""
    gpar_intro = "The Grandparents of The Family are:\n"
    for g in range(len(grandparents)):
        gpar_out = grandparents[g].name + " , " + grandparents[g].birthday 
        gpar = (gpar + ":   " + gpar_out)
        outgpar = gpar_intro + gpar[1:]
    display3 = Text(Point(1,1),outgpar)
    display3.draw(win)
    
    print( "\nParents:")
    par = ""
    outpar = ""
    par_intro = "The Parents of The Family are:\n"
    for p in range(len(parents)):
        par_out = parents[p].name + " , " + parents[p].birthday #taking the name and bday from the class
        par = (par + ":   " + par_out)
        outpar = par_intro + par[1:]
    display2 = Text(Point(1,2),outpar)
    display2.draw(win)
   
    print( "\nSiblings:")
    sib = ""
    outsib = ""
    sib_intro = "The Siblings of The User are:\n"
    for s in range(len(siblings)):
        sib_out = siblings[s].name + " , " + siblings[s].birthday 
        sib = (sib + ":   " + sib_out)
        outsib = sib_intro + sib[1:]
    display4 = Text(Point(1,3),outsib)
    display4.draw(win)
    win.getMouse()  # pause for click in window
    win.close()
        
    


    end_or_continue()


main()   

    

