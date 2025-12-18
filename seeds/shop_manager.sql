DROP TABLE IF EXISTS "items_orders";
-- DROP SEQUENCE IF EXISTS items_orders_id_seq;
DROP TABLE IF EXISTS "orders";
DROP SEQUENCE IF EXISTS orders_id_seq;
DROP TABLE IF EXISTS "items";
-- DROP SEQUENCE IF EXISTS items_id_seq;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    descript TEXT,
    price DECIMAL(10,2),
    quantity INT 
);

CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
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
INSERT INTO orders (customer, date) VALUES 
    ('piggy', '2025-12-24'),
    ('kermit', '2025-12-18'),
    ('camilla', '2025-11-17'),
    ('fozzie', '2025-11-13');

INSERT INTO items (descript, price, quantity) VALUES 
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