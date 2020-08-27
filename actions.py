import random

#from classes import Product

def discover(player):
    #action will allow the user a 50% chance to discover a resource. This is intended to be limited on a per day base
    now = input("What are you looking for?")
    if random.randint(0,1):
        print(f"You have discovered {now}! It has been added to your list of resources.")
        player.resources.append(now)
    else:
        print(f"You searched and were unable to discover anything")
        return
  
def create(player):
    #set up a loop that asks for resources and checks if each one is available. Then creates a product that contains those resources in a list
    creating = True
    while creating:
        resources = []
        now = input("What will you use to make this product?")
        if now in player.resources:
            print(f"{now} has been added.")
            resources.append(now)
        else:
            print(f"{now} is not available to you at this time.")
        
        if "y" in input("Would you like to add another resource?"):
            continue
        else:
            print("Your product contains:")
        for x in resources:
            print(x)
        if "y" in input("Would you like to finalize this product?"):
            name = input("What is the name?\n")
            name = Product(name,resources)
            creating = False
        else:
            print("Product creation canceled...")
            creating = False
