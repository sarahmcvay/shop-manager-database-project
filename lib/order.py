
class Order: 
    def __init__(self, customer, date):
        self.customer = customer
        self.date = date

    def __eq__(self, other):
        # return self.__dict__ == other.__dict__
        if not isinstance(other, Order):
            return False 
        return (
            self.customer == other.customer and
            self.date == other.date
        )