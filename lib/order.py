
class Order: 
    def __init__(self, customer, order_date):
        self.customer = customer
        self.order_date = order_date

    def __eq__(self, other):
        # return self.__dict__ == other.__dict__
        if not isinstance(other, Order):
            return False 
        return (
            self.customer == other.customer and
            self.order_date == other.order_date
        )