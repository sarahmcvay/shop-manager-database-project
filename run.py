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
from lib.order_repository import OrderRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/shop_manager.sql")

    def run(self):
        print("Welcome to the muppety boutique inventory system")
        print("what would you like to do?")
        print("1 - List all items in stock")
        print("2 - Create new item in shop")
        print("3 - List all orders")
        print("4 - List all orders with corresponding items")
        print("5 - Create new order")
        choice = input("Enter your choice:  ")
    
        if choice == "1": 
            item_repository = ItemRepository(self._connection)
            items = item_repository.all()
            for item in items:
                print (f"{item.descript}: price £{item.price}, stock {item.quantity}")

        if choice == "3":
            order_repository = OrderRepository(self._connection)
            orders = order_repository.all()
            for order in orders:
                print(f"Customer: {order.customer}, Date: {order.date}")

        if choice == "4":
            order_repository = OrderRepository(self._connection)
            orders = order_repository.all_orders_with_items()
            for order in orders:
                print(f"Customer: {order['customer']}, Date: {order['date']}")
                for item in order["items"]:
                    print(
                        f"  - {item['descript']}"
                        f"(qty: {item['quantity']}, price: £{item['price']})"
                    )
                # print(order)

# can I print items in the order? 

        # elif choice == "3":
        #     print("Functionality coming soon!")

        # elif choice == "4":
        #     print("Functionality coming soon!")
        
        # elif choice == "5":
        #     print("Functionality coming soon!")

        else: 
            return print("Please try again, invalid entry.")

if __name__ == "__main__":
    app = Application()
    app.run()