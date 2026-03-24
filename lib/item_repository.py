from lib.item import *

class ItemRepository: 
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows =self._connection.execute(
            'SELECT * from items'
        )
        stockeditems = []
        for row in rows:
            thing = Item( 
                row["descript"],
                row["price"], 
                row["quantity"]
            )
            stockeditems.append(thing)
        return stockeditems


    def create(self, item):
        self._connection.execute(
            'INSERT INTO items (descript, price, quantity) VALUES(%s, %s, %s)',
            [item.descript, item.price, item.quantity]
        )
        return None
        # when added create a message saying new item was added? 


    def find(self, item_id):
        rows = self._connection.execute(
            "SELECT * FROM items WHERE id = %s",
            [item_id]
        )
        row = rows[0]
        return Item(row["descript"], row["price"], row["quantity"])


    def edit(self, item):
        self._connection.execute(
            'UPDATE items SET price = %s, quantity =%s WHERE descript = %s',
            [item.price, item.quantity, item.descript]
        )
    # I want to be able to edit items
    # e.g. to procure extra quanitity of items already for sale in the shop or edit price
    # In this system I will not log supplier info, could do through seperate table, see notes. 


    # def delete(self,item):
    #     pass 
    # I want to be able to delete from the shop system? 
    # or maybe you want to keep the items listed but just see stock is zero.