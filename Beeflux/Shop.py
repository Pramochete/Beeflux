class Shop:

    def __init__(self, listOfItemsEn):
        self.listOfItems = listOfItemsEn

    def items(self):
        print ()
        print ("Items in shop: ")
        for item in self.listOfItems:
            print (item)
    
    def items_cost(self, requestCostOfItems):
        returnCostOfItem = {"apple" : "$2",
                            "potato" : "$1",
                            "tomato" : "$2",
                            "chillies" : "$0.9",
                            "spinach" : "$1.5",
                            }
        chechKeys = returnCostOfItem.keys()
        if requestCostOfItems in chechKeys:
            print ("Cost of {} is {}".format(requestCostOfItems, returnCostOfItem[requestCostOfItems]))
        else:
            print("The item {} doesn't exist in our store".format(requestCostOfItems))
   
    def sold_item(self, soldItem):
        if soldItem in self.listOfItems:
            self.listOfItems.remove(soldItem)
        else:
            print("The item you need is unavailable")
            

class Customer:
    
    def buy_item(self):
        print("Enter the name of the item you wish to buy: ")
        self.buy = input()
        return self.buy

user = Shop(['apple','potato', 'tomato', 'chillies', 'spinach'])
customer = Customer()
while True:
    print ("Enter 1 to display the available items: ")
    print ("Enter 2 to display cost of item: ")
    print ("Enter 3 to buy an item: ")
    print ("Enter 4 to exit")
    userChoice = int(input())
    if userChoice is 1:
        user.items()
    elif userChoice is 2:
        print("Enter the item: ")
        requestCostOfItems = input()
        user.items_cost(requestCostOfItems)
    elif userChoice is 3:
        soldItem = customer.buy_item()
        user.sold_item(soldItem)
    elif userChoice is 4:
        quit()
