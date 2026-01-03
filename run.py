# user stories 
# - want to see a list of shop items and how many available 
# - message, new item added when I add stock (create a new item)
# - want to see a list of orders and customer names with a date
# - message new order created when a new order is put through the system
# 
#  generate a report showing regarding inventory status
# creates the menu for navigation 

from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.order_repository import *

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/shop_manager.sql")

    def run(self):
        print("Welcome to the muppety boutique inventory system")
        print("what would you like to do?")
        print("1 - List all items in stock")
        print("2 - Add item to stock")
        print("3 - List all orders")
        print("4 - Add new order")
        choice = input("Enter your choice:  ")
    
        if choice == "1":
            item_repository = ItemRepository(self._connection)
            items = item_repository.all()
            for item in items:
                print (f"{item.descript}: price £{item.price}, stock {item.quantity}")
        
        else: 
            return print("Functionality coming soon!")

if __name__ == "__main__":
    app = Application()
    app.run()