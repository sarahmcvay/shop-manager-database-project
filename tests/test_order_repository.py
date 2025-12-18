from lib.order_repository import *
from lib.order import *

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
    ]
    