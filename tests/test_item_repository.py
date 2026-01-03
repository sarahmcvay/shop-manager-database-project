from lib.item_repository import *
from lib.item import *

"""
We can return all the items stocked in the shop
"""
def test_get_all_items(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    stock = repository.all()
    # print(type(orders[0].date), orders[0].date) check format of date

    assert stock == [
        Item('high heels', 80.00, 8),
        Item('lipstick', 50.00, 28),
        Item('mascara', 30.50, 40),
        Item('eyelash curlers', 10.00, 6),
        Item('bow tie', 30.00, 12),
        Item('diamond ring', 1000.00, 3),
        Item('necklace', 500.00, 7),
        Item('handbag', 750.00, 9),
        Item('nail polish', 15.50, 46),
        Item('hairbrush', 80.00, 2)
    ]

"""
We can create a new item in the database 
"""
def test_new_item_added(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    repository.create(Item('scarf', 20.00, 1))

    newstocklist = repository.all()

    assert newstocklist == [
        Item('high heels', 80.00, 8),
        Item('lipstick', 50.00, 28),
        Item('mascara', 30.50, 40),
        Item('eyelash curlers', 10.00, 6),
        Item('bow tie', 30.00, 12),
        Item('diamond ring', 1000.00, 3),
        Item('necklace', 500.00, 7),
        Item('handbag', 750.00, 9),
        Item('nail polish', 15.50, 46),
        Item('hairbrush', 80.00, 2),
        Item('scarf', 20.00, 1)
    ]