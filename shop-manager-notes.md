# Research into different ways to do inventory 

Tkinter

w3resource suggested
    Products Table
        product_name, price
    Suppliers Table
        supplier_name, email
    Inventory Table
        product_id, quanitity, supplier_id, last_updated 
    Transactions Table
        transaction id, product id, transaction type, transaction date, quantity

# SQL Notes
Version 1: This mashes the tables together but needs refining to remove duplicate columns 
SELECT * 
FROM orders o
LEFT JOIN orders_items oi ON oi.order_id = o.id
LEFT JOIN items i ON i.id = oi.item_id
ORDER BY o.id, i.descript

Version 2: refined 
SELECT
	o.id AS order_id,
	o.customer,
	o.date,
	oi.quantity AS order_quantity,
	i.descript,
	i.price
FROM orders o
JOIN orders_items oi ON oi.order_id = o.id
JOIN items i ON i.id = oi.item_id
ORDER BY o.id, i.descript