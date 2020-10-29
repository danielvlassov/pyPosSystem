# POS System
# Daniel Vlassov
# Making a fully functional POS system with inventory, purchasing, all the fun quirks
# 10/19/2020

# Init createItem
def createItem(productCode, item, regularPrice, startingStock, salePrice):

    # start Indent
    # This will turn into a Dictionary inside a list just like the model shown
    # Returns the call

    return [{productCode: item}, regularPrice, startingStock, salePrice]
# end 

# Init clearArea 
# quick function for screen spacing
def clearArea():
    # start indent
    # prints spaces then 32 lines, returns
    print("")
    print("-" * 32)
    print("")
    return

# end indent

# Init menu function
def menu(inventory):
    # start indent
    # Prints options availible to choose, and selects an input from the list
    print("1. Cash Register")
    print("2. Inventory Control")
    print("3. Additional Modifications")
    print("4. Shutdown")
    menuItem = int(input())
    # checks between the user choices and calls the correct functions / etc to continue
    if menuItem == 1:
        cashRegister(inventory)
    elif menuItem == 2:
        inventoryControl(inventory)
    elif menuItem == 3:
        print("Additonal")
        # DO NOT IMPLEMENT
        # Maybe using a SQL storage instead for security reasons?
        # Using classes would help and more creative freedom
    elif menuItem == 4:
        print("Shutting Down || Goodbye!")
        return
    # if incorrect choice, prints invaild and returns to func
    else:
        print("Invaild!")
        menu(inventory)
    # end indent

# Init listInventory
# Called from inventoryControl() function to list current inventory 
def listInventory(inventory):
    # prins description, spacing, and inventory
    print("Item ID: Name, Initial Price, Quantity, Sale Price")
    print("")
    print(inventory)
    print("")
    # waits for user input to continue, then calls inventoryControl() function to return
    input("\nPress Enter to Return \n")
    inventoryControl(inventory)
# end indent

# subset of inventoryControl() called to add item or start a sale, or return
def addRemove(inventory):
    # lists user choices
    print("1. Add Item")
    print("2. Initialize Sale")
    print("3. Main Menu")
    # input to wait for user choice, then checks between choices and calls correct function
    addRemoveChoice = int(input(""))
    if addRemoveChoice == 1:
        addInv(inventory)
    elif addRemoveChoice == 2:
        removeInv(inventory)
    elif addRemoveChoice == 3:
        menu(inventory)
    # if incorrect choice, prints invaild and returns to func
    else:
        print("Invaild!")
        return
# end indent

# init addInv func
# adds new products into inventory
def addInv(inventory):
    # requests user inputs for products name, inventory amount,  price
    # quantity, and sets its own product code by adding 10001 to current inv ammount
    tempName = input("Enter the product name: ")
    invAmount = len(inventory)
    tempPrice = float(input("Enter Item Price ($): "))
    tempQuan = int(input("Enter Quantity Stocked: "))
    tempNum = 10001 + invAmount
    # calls createItem function to make new inventory addition
    inventory = inventory + [
        createItem(tempNum, tempName, tempPrice, tempQuan, tempPrice)
    ]
    print("")
    print(inventory)
    # waits for user input to return to inventoryControl()
    input("Press Enter to Return!")
    inventoryControl(inventory)
# end indent

# init removeInv function (changed to sale but kept funcName)
def removeInv(inventory):
    # prints current inventory
    print(inventory)
    # prints spacing
    print("")
    # inputs for user choices such as product ID and percent sale
    choice = int(input("Enter your product ID you wish to add a sale to: "))
    percent = int(input("What percentage sale do you wish to apply?: "))
    # sale percentage calculated by 100 - percent choice, divided by 100 (to * later)
    sale = (100 - percent) / 100
    # changes the sale price in inventory[] with regularPrice * sale#
    inventory[choice - 10001][3] = round(inventory[choice - 10001][1] * sale, 2)
    # Prints applied and calls inventoryControl()
    print("Applied!")
    inventoryControl(inventory)
# end indent

# init restock() function
def restock(inventory):
    # prints inventory
    print(inventory)
    # prints spacing
    print("\n"*2)
    # which product code to restocl
    reCode = int(input("Enter the product code you wish to restock: "))
    # how much to restock
    howMuch = int(input("By how much?: "))
    # adds the ammount chosen into the products inventory 
    inventory[reCode - 10001][2] += howMuch
    # print success and calls inventoryControl
    print("Success!")
    inventoryControl(inventory)
# end indent
    
# init inventoryControl()
def inventoryControl(inventory):
    # calls clearArea() to look nicer
    clearArea()
    # prints user choices and then selects the appropriate function to call, if None
    # selected properly, reruns function
    print("1. List Inventory")
    print("2. Add/Sale Inventory")
    print("3. Restock Items")
    print("4. Main Menu")
    inventoryMenu = int(input())
    clearArea()
    if inventoryMenu == 1:
        listInventory(inventory)
    elif inventoryMenu == 2:
        addRemove(inventory)
    elif inventoryMenu == 3:
        restock(inventory)
    elif inventoryMenu == 4:
        menu(inventory)
    else:
        print("Invaild!")
        inventoryControl(inventory)
# end indent

# init reciept function
def reciept(inventory, name, purchases, rollingCost):
    # sets init vars such as tempNum, tax, and total calculated beforehand
    tempNum = 0
    tax = round(rollingCost * 0.13, 2)
    total = round(rollingCost + tax, 2)
    # spacing and text for reciept
    print("\n"*5)
    print("Thank you for shopping with us!")
    print("-"*32)
    # prints cashier
    print(f"Your cashier is: {name}")
    print("-"*32)
    # prints reader info
    print("Amount | Code | Name | Price")
    # prints purchases
    print(purchases)
    print("-"*32)
    print("")
    # prints all costs and stuff, cool cool
    print(f"Cost: ${rollingCost}")
    print(f"Tax: ${tax}")
    print("")
    print(f"Your total for today is:")
    print("$",total)
    print("-"*32)
    # waits for user input to return to main menu
    goThru = input("Press enter to shop again!\n")
    menu(inventory)
# end indent

# init cashRegister func
def cashRegister(inventory):
    # init vars set for future use
    go = True
    purchases = ""
    purchaseCode = []
    purchaseAmt = []
    rollingCost = 0.00
    # grabs name input
    name = input("What is your name? ")
    # waits to see if purchase goin or not
    purchaseMade = input("Is a purchase being made (y/n)? ")
    # if yes, :
    if purchaseMade == "y" or purchaseMade == "Y":
        # 2 while go: true to repeat until finished
        while go:
            while go:
                # Gets a product code -> checks that product code for actual items
                productCode = int(input("What is the product code? "))
                checkItem = findItem(inventory, productCode)

                # If an item was returned
                if checkItem:
                    correctItem = input(f"Is the item {checkItem} (y/n)? ")

                    # Ensures the user has confirmed the item
                    if correctItem == "y" or correctItem == "Y":
                        # We have an item
                        break
                else:
                    # Incorrect id, print an error and ask for another
                    print("Error.  Provide another id.")
            # User input for ammount to buy 
            amnt = int(input("How many? "))
            # confirms purchase with either Y y or N n
            confirm = input(f"You'd like to purchase {amnt} of {checkItem} (y/n) ")
            # if confirmed:
            if confirm == "y" or confirm == "Y":
                # calls findCost function to find cost of item
                cost = findCost(inventory, productCode)
                # calculates rollingCost each itiration by cost * amnt, rounded 2
                rollingCost += round(cost * amnt,2)
                # calls updateInventory function to edit the amnt that was purchased
                inventory = updateInventory(inventory, productCode, amnt * -1)
                # adds each new line of purchase each itiration, with amnt, code, item, cost
                purchases += f"{amnt}   {productCode}   {checkItem}    {cost}\n"

                print(purchases)
            # user input to purchase again or not
            purchaseAgain = input("Would you like to add another item (y/n)? ")
            # if yes, runs shop again while keeping values, 
            if purchaseAgain == "y" or purchaseAgain == "Y":
                continue
            # else, stops itirating and calls reciept function for final total etc
            else:
                go = False
                reciept(inventory, name, purchases, rollingCost)
    # returns inventory for the cashreg func
    return inventory

# init updateInventory()
def updateInventory(inventory, itemId, amnt):
    # adds (or removes in this case) amnt from inventory[]
    inventory[int(itemId) - 10001][2] += amnt
    # returns
    return inventory
# end indent

# init findCost
def findCost(inventory, itemId):
    # finds len of inventory and stores it
    invAmount = len(inventory)
    # checks to see if code vaild or not
    if 10001 <= itemId and itemId <= invAmount + 10000:
        # prints inv and itId
        print(inventory, itemId)
        # returns the cost of item
        return inventory[itemId - 10001][3]
    else:
        # invld or no cost returns false
        return False
# end indent

# init findItem()
def findItem(inventory, itemId):
    # checks inv len and assigns to a var
    invAmount = len(inventory)
    # checks to see if it is vaild code or not
    if 10001 <= itemId and itemId <= invAmount + 10000:
        print(inventory, itemId)
        # returns itemName
        return inventory[itemId - 10001][0][itemId]
    else:
        # invaild aka go home false bla bla
        return False
# end indent

# init the main() function 
def main():
    # creates initial inventory as required by asgnment then calls menu()
    inventory = [createItem(10001, "apples", 4.99, 500, 4.99)]
    menu(inventory)

# calls main()
main()