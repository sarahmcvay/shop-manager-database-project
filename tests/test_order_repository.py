from lib.order_repository import *
from lib.order import *
from lib.item import *
import datetime

"""
We can return all the orders, with data reflecting seed information correctly
"""
def test_get_all_orders(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    orders = repository.all()
    # print(type(orders[0].date), orders[0].date) check format of date

    assert orders == [
        Order('piggy', '2025-12-24'),
        Order('kermit', '2025-12-18'),
        Order('camilla', '2025-11-17'),
        Order('fozzie', '2025-11-13'),
        Order('gonzo', '2025-12-19'),
    ]
    
""" 
We can look up an order by its id and see which date the transaction happened
"""
def test_get_date_for_order_with_order_id(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    orderinfo = repository.find(1)
    print(type(orderinfo.date))

    # assert orderinfo == Order('piggy', '2025-12-24')
    assert orderinfo == Order("piggy", datetime.date(2025, 12, 24)) 
# convered to datetime.  May need to look at all function, which is set to str. 
    
"""
We can fetch the items linked to an order_id
"""
def test_order_links_to_one_item_order(db_connection): 
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    itemlist = repository.find_items_in_order(1)

    assert itemlist == [
        Item('high heels', 80.00, 8),
        Item('lipstick', 50.00, 28)
    ]
# I think i need an order_item class to get the right order quanitity number


