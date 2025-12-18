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

### Table 1: items
| Column  | Type     | Notes    |
|---------|----------|----------|
| id      | SERIAL | Primary key |
| item | TEXT | Descriptive name of the item |
| price   | DECIMAL | Pounds and pence |
| quantity | INT | Number of items in stock |

### Table 2: orders
| Column  | Type     | Notes    |
|---------|----------|----------|
| id      | SERIAL | Primary key |
| customer | TEXT | Customer name |
| date   | DATE | Order date |

### Join table: items_orders
| Column  | Type     | Notes    |
|---------|----------|----------|
| item_id  | INT | Foreign key -> items(id) |
| order_id | INT | Foreign key -> orders(id)|
| quantity | INT | Number of items in the order |

## STEP 2: Write SQL

```sql
DROP TABLE IF EXISTS "items_orders";
DROP TABLE IF EXISTS "orders";
DROP TABLE IF EXISTS "items";

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  item TEXT,
  price DECIMAL(10,2),
  quantity INT 
);

DROP TABLE IF EXISTS "orders";
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer TEXT,
  date DATE
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
INSERT INTO items (item, price, quantity) VALUES 
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

INSERT INTO orders (customer, date) VALUES 
    ('piggy', '2025-12-24'),
    ('kermit', '2025-12-18'),
    ('camilla', '2025-11-17'),
    ('fozzie', '2025-11-13');

INSERT INTO items_orders (item_id, order_id, quantity) VALUES
(1, 1, 5), -- piggy, 5 high heels
(2, 1, 3), -- piggy, 3 lipstick
(6, 2, 1), -- kermit, 1 diamond ring
(7, 2, 1), -- kermit, 1 necklace
(8, 2, 1), -- kermit, 1 handbag
(3, 3, 2), -- camilla, 2 mascara
(4, 3, 1), -- camilla, 1 eyelash curler
(9, 3, 2), -- camilla, 2 nail polish
(10, 4, 2), -- fozzie, 2 hairbrush 
(5, 4, 6); -- fozzie, 6 bow ties 

```
## STEP 4: Create the tables
```bash
psql shop_manager < shop_manager.sql
```

