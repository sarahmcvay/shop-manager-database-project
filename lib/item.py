
class Item: 
    def __init__(self, descript, price, quantity):
        self.descript = descript
        self.price = price
        self.quantity = quantity
    
    def __eq__(self, other):
        # return self.__dict__ == other.__dict__
        if not isinstance(other, Item):
            return False 
        return (
            self.descript == other.descript and
            self.price == other.price and
            self.quantity == other.quantity
        ) 
    
    def __repr__(self):
        return f"Album({self.title}, {self.release_year}, {self.artist_id})"