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

    def edit(self, item):
        pass 
    # we want to be able to edit the items in the item repository
    # this will link to new items procured for sale in the shop
    # this will link to orders made, items removed from the shop

    def delete(self,item):
        pass 
    # we want to be able to delete from the shop system