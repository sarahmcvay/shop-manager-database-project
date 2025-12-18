# Shop Manager, Database Design

## STEP 1: Understand Requirements 
As a shop manager
1) So I can know which items I have in stock: 
-  I want to keep a list of my shop items with their name and unit price.
-  I want to know what quantity (a number) I have for each item.
2) So I can manage items:
-  I want to be able to create a new item.
3) So I can know which orders were made:
- I want to keep a list of orders with their customer name.
- I want to assign each order to their corresponding item. 
- I want to know on which date an order was placed. 
4) So I can manage orders:
- I want to be able to create a new order.

### Extract Nouns 

--> stock, items, name, price, quantity
--> order, customer, date

## STEP 2: Set Out Tables 

### Table 1: orders
| Column  | Type     | Notes    |
|---------|----------|----------|
| id      | SERIAL | Primary key |
| customer | TEXT | Customer name |
| date   | DATE | Order date |

### Table 2: items
| Column  | Type     | Notes    |
|---------|----------|----------|
| id      | SERIAL | Primary key |
| description | TEXT | Descriptive name of the item being sold |
| price   | DECIMAL | Pounds and pence |
| quantity | INT | Number of items in stock |

### Join table: items_orders
| Column  | Type     | Notes    |
|---------|----------|----------|
| order_id | INT | Foreign key -> orders(id)| 
| unit_id  | INT | Foreign key -> items(id) |
| quantity | INT | Number of units in the order |

## STEP 2: Write SQL

```sql
DROP TABLE IF EXISTS "items_orders";
DROP TABLE IF EXISTS "orders";
DROP TABLE IF EXISTS "items";

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer TEXT,
  date DATE
);

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  unit TEXT,
  price DECIMAL(10,2),
  quantity INT 
);

CREATE TABLE items_orders (
  item_id INT NOT NULL,
  order_id INT NOT NULL,
  quantity INT NOT NULL,
  CONSTRAINT fk_item 
    FOREIGN KEY (item_id) REFERENCES items(id) ON DELETE CASCADE,
  CONSTRAINT fk_order 
    FOREIGN KEY(order_id) REFERENCES orders(id) ON DELETE CASCADE,
  PRIMARY KEY (item_id, order_id)
);
```
## STEP 3: Seed data 
```sql
INSERT INTO orders (customer, date) VALUES 
    ('piggy', '2025-12-24'),
    ('kermit', '2025-12-18'),
    ('camilla', '2025-11-17'),
    ('fozzie', '2025-11-13');

INSERT INTO items (discription, price, quantity) VALUES 
    ('high heels', 80.00, 8),
    ('lipstick', 50.00, 28),
    ('mascara', 30.50, 40),
    ('eyelash curlers', 10.00, 6),
    ('bow tie', 30.00, 12),
    ('diamond ring', 1000.00, 3),
    ('necklace', 500.00, 7),
    ('handbag', 750.00, 9),
    ('nail polish', 15.50, 46),
    ('hairbrush', 80.00, 2);

INSERT INTO items_orders (order_id, item_id, quantity) VALUES
(1, 1, 5), -- piggy, high heels x 5
(1, 2, 3), -- piggy, lipstick x 3
(2, 6, 1), -- kermit, diamond ring x 1
(2, 7, 1), -- kermit, necklace x 1
(2, 8, 1), -- kermit, handbag x 1
(3, 3, 2), -- camilla, mascara x 2
(3, 4, 1), -- camilla, eyelash curler x 1
(3, 9, 2), -- camilla, nail polish x 2
(4, 10, 2), -- fozzie, hairbrush x 2
(4, 5, 6); -- fozzie, bow ties x 6

```
## STEP 4: Create the tables
```bash
psql shop_manager < seeds/shop_manager.sql
```

## STEP 5: Methods for user functionality 
```python
class OrderRepository: 
    def __init__(): 
        pass 
    def all(): 
        pass 
    def find():
        pass 
    def create(): 
        pass 

class Order:
    def __init__(): 
        pass
    def __eq__():
        pass
    def __rep__(): 
        pass 

class ItemRepository: 
    def __init__(): 
        pass 
    def all(): 
        pass
    def find(): 
        pass 
    def create(): 
        pass 

class Item: 
    def __init__(): 
        pass 
    def __eq__(): 
        pass
    def __repr__(): 
        pass 


```