#
# Robot Shop - Objects and Classes Lab
#
# Author: Jumin Shrestha
"""First, define a Product class that includes all the information about a single product. 
a. You will need a constructor to initialize new instances. Objects of this class should have three instance variables: 
name, price, and quantity in-stock. 
b. Add a method to your class that takes an integer count and determines whether that many of the product are in stock. 
c. Add another method that takes a count and returns the total cost of that many of the product. 
d. Finally, add a method that takes a count and removes that many of the product from the stock.
Next, replace the three product lists with a single list of Product instances.
Modify the rest of the code to correctly use the attributes and methods of the Products in the list.
Test your program as you go and fix any syntax or logic errors in order to get it working correctly.
Add, commit, and push your final version.
"""


class Product:

    def __init__(self,name,price,quantity_in_stock):
        self.name = name
        self.price = float(price)
        self.quantity_in_stock = float(quantity_in_stock)
    
    def in_stock (prod_id,count):
        if products[prod_id].quantity_in_stock >= count:
            return ("y")
        else:
            return ("n")
    
    def cost(self, count):
        price = self.price * count
        print (price) 

    def remove_from_stock (self, prod_id,count):
        products[prod_id].quantity_in_stock -= count


products = [Product ("Ultrasonic range finder",2.50,4),
            Product ("Servo motor", 14.99, 10),
            Product ("Servo controller", 44.95,5),
            Product ("Microcontroller Board", 34.95,7),
            Product ("Laser range finder",149.99,2),
            Product ("Lithium polymer battery", 8.99, 8)]



def print_stock():
    print()
    print("Available Products")
    print("------------------")
    print(products[0].name + " " + str(products[0].price))
    print(products[1].name + " " + str(products[1].price))
    print(products[2].name + " " + str(products[2].price))
    print(products[3].name + " " + str(products[3].price))
    print(products[4].name + " " + str(products[4].price))
    print(products[5].name + " " + str(products[5].price))

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock()
        vals = input("Enter product ID followed by the quantity you wish to buy (or 'quit' to exit): ").split(" ")
        if vals[0] == "quit": break
        prod_id = int(vals[0])
        count = int(vals[1])
        # look up the product ID in the products list to get the desired Product instance

        if Product.in_stock(prod_id,count) == "y": # use the quantity property of the Product instance
            if cash >= products[prod_id].price * count:
                Product.remove_from_stock(prod_id,count)  #decrease in stock
                cash -= products[prod_id].price * count  # decrease money
                print("You purchased", count, products[prod_id].name,".")
                print(f"You have ${cash:.2f} remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", products[prod_id])

main()