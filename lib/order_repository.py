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

    def find_items_in_order(self, order_id):
# allows the user find the items connected to a single order
        rows = self._connection.execute(
            # select all the items associated with the order
            "SELECT items.descript, items.price, items.quantity "
            # find that in
            "FROM orders "
            # link tables together
            # join table first, matching records in join table with orders
                "JOIN orders_items ON orders_items.order_id = orders.id "
            # then match items to records in join table 
                "JOIN items ON orders_items.item_id = items.id " \
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

        # see shop manager notes for thinking.

    def all_orders_with_items(self):
        rows = self._connection.execute(
            "SELECT o.id AS order_id, o.customer, o.date, "
            "oi.quantity AS order_quantity, i.descript, i.price "
            "FROM orders o "
            "JOIN orders_items oi ON oi.order_id = o.id "
            "JOIN items i ON i.id = oi.item_id "
            "ORDER BY o.id, i.descript "
        )
        orders_dict = {} # dict allows us to group rows by order_id
        for row in rows: 
            order_id = row["order_id"]
        
        # if we haven't seen the order yet, create an entry in the dict
            if order_id not in orders_dict: 
                orders_dict[order_id] = {
                    "id": order_id,
                    "customer": row["customer"],
                    "date": row["date"],
                    "items": []
                }

        # add the item (if there is one)
            if row["descript"] is not None:
                orders_dict[order_id]["items"].append({
                    "descript": row["descript"],
                    "quantity": row["order_quantity"],
                    "price": row["price"]
                    })

        return list(orders_dict.values())



    # def remove_items_in_an_order_from_stock(self):
    #     pass 

# def find_by_customer_name(self, order_id):
    # search by customer name, can find the date of the order. 