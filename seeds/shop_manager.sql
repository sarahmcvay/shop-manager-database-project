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

-- seed data
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