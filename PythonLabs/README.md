# Lab Activity #9 – Working with Classes and Objects

*NOTE: This lab is not a team activity an may be completed individually.*

## Goals

Practice creating and using a Python class, including constructing instances
and calling methods.

### Prerequisites

This lab assumes that you have:

- read Chapter 10 in our textbook;
- basic experience with Python/IDLE and Git;
- fetched and merged the Lab09 instructions from the upstream repository.

### Skills Acquired/Reinforced Upon Completion

- Define a class with methods and instance variables.
- Create objects by calling the class constructor.
- Use objects by using the interface provided by the methods.

## Non-Object-Oriented base program

In this lab, you will refactor an existing program to use an object-oriented
style instead of separate, coordinated lists of strings and numbers.

Study the `RobotShop.py` program carefully and run it to see how it works.
Make sure you understand the program before modifying it in the next secction.
Feel free to discuss with your classmates and ask questions of your instructor
as needed.

## Migrating to an Object-Oriented approach

We are now going to change this program so that it uses classes, objects, and methods.

1. First, define a `Product` class that includes all the information about a single product.
    a. You will need a constructor to initialize new instances. Objects of this class
        should have three instance variables: name, price, and quantity in-stock.
    b. Add a method to your class that takes an integer count and determines whether
        that many of the product are in stock.
    c. Add another method that takes a count and returns the total cost of that many of
        the product.
    d. Finally, add a method that takes a count and removes that many of the product
        from the stock.
2. Next, replace the three product lists with a single list of `Product` instances.
3. Modify the rest of the code to correctly use the attributes and methods of the
    `Product`s in the list.
4. Test your program as you go and fix any syntax or logic errors in order to get it
    working correctly.
5. Add, commit, and push your final version.

## Completing this Lab

In order to receive full credit for this Lab activity:

1. The `Labs/Lab09` subfolder of your repository must contain a modofied version
    of `RobotShop.py` that meets the requirements above.
2. Your script must contain your full name in the header comment at the top.
3. Your repository's commit history must show at least one commit for the
    `RobotShop.py` file.
4. All of the above must be pushed to GitHub so that I can see it.

Congratulations! You've completed Lab #9.
