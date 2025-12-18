from lib.order import *

class OrderRepository: 
    def __init__(self, connection): 
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from orders')
        orderlist = []
        for row in rows: 
            item = Order(
                row["customer"],
                str(row["date"]),
            )
            orderlist.append(item)
        return orderlist