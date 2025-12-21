from lib.order import *
from lib.item import *
import datetime

class OrderRepository: 
    def __init__(self, connection): 
        self._connection = connection

    def all(self): 
# allows user to create list of all orders, with customer name
        rows = self._connection.execute('SELECT * from orders')
        orderlist = []
        for row in rows: 
            item = Order(
                row["customer"],
                str(row["date"]),
            )
            orderlist.append(item)
        return orderlist
    
    def find(self, order_id):
# allows user to find the date on which an order was placed, by order_id
        rows = self._connection.execute(
            'SELECT * from orders WHERE id = %s',
            [order_id]
        )
        row = rows[0]
        return Order(
            # row["id"],
            row["customer"],
            row["date"]
            # str(row["date"])
        )

# def find_by_customer_name(self, order_id):
    # search by customer name, can find the date of the order. 

    def find_items_in_order(self, order_id):
# allows the user find the items connected to a single order
        rows = self._connection.execute(
            # select all the items associated with the order
            "SELECT items.descript, items.price, items.quantity "
            # find that in
            "FROM orders "
            # link tables together
            # join table first, matching records in join table with orders
                "JOIN items_orders ON items_orders.order_id = orders.id "
            # then match items to records in join table 
                "JOIN items ON items_orders.item_id = items.id " \
                "WHERE orders.id = %s", [order_id]
        )
        itemsinorder = []
        for row in rows: 
            item = Item(
                row['descript'],
                row['price'],
                row['quantity'],
            )
            itemsinorder.append(item)
        
        return itemsinorder

