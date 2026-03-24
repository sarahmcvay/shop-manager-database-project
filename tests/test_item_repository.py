import pytest
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
        Item('banjo', 750.00, 9),
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
        Item('banjo', 750.00, 9),
        Item('nail polish', 15.50, 46),
        Item('hairbrush', 80.00, 2),
        Item('scarf', 20.00, 1)
    ]

"""
We can find an item using item_id 1
"""
def test_find_item_record_in_shop(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    item = repository.find(1)
    print(item)
    assert item == Item('high heels', 80.00, 8)


"""
We can find an item using item_id 2
"""
def test_find_item_2_in_shop(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    item = repository.find(2)
    print(item)
    assert item == Item('lipstick', 50.00, 28)
    # def find(self, item_id):
    #     rows = self._connection.execute(
    #         "SELECT * FROM items WHERE id = %s",
    #         [item_id]
    #     )
    #     row = rows[0]
    #     return Item(row["descript"], row["price"], row["quantity"])

"""
We can edit the items, e.g. change the price or add more stock (increase quanitity)
"""
@pytest.mark.skip
def test_item_edit(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    item = repository.find(1)
    # item.price = 39.99
    # item.quantity = 10

    repository.edit(item)

    newstocklist = repository.all()

    assert newstocklist == [
        Item('high heels', 39.99, 10),
        Item('lipstick', 50.00, 28),
        Item('mascara', 30.50, 40),
        Item('eyelash curlers', 10.00, 6),
        Item('bow tie', 30.00, 12),
        Item('diamond ring', 1000.00, 3),
        Item('necklace', 500.00, 7),
        Item('banjo', 750.00, 9),
        Item('nail polish', 15.50, 46),
        Item('hairbrush', 80.00, 2)
    ]

    # def edit(self, item):
    #     self._connection.execute(
    #         'UPDATE items SET price = %s, quantity =%s WHERE id = %s',
    #         [item.price, item.quantity, item.item_id]
    #     )