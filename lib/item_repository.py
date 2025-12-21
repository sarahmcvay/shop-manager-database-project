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