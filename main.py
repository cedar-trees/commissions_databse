import sqlite3
# from commission import Commission

conn = sqlite3.connect('commission.db')

c = conn.cursor()


##create commission table

# c.execute(""" CREATE TABLE commission_types (
#          item_id TEXT,
#           item_name TEXT,
#           colourway TEXT,
#           price INT,
#           completion_time TEXT )""")

##Insert commission types into table

# c.execute("""INSERT INTO commission_types (item_id, item_name, colourway, price, completion_time)
#           VALUES('DD101', 'Doodle Dudes', 'Black & White', 250, '2 weeks'),
#                 ('DD102', 'Doodle Dudes', 'Colour', 300, '2 weeks'),
#                 ('DaDo201', 'Daruma Dogs', 'Black & White', 300, '2 weeks'),
#                 ('DaDO202', 'Daruma Dogs', 'Colour', 400, '2 weeks'),
#                 ('LC203', 'Lucky Cats', 'Black & White', 300, '2 weeks'),
#                 ('LC204', 'Lucky Cats', 'Colour', 400, '2 weeks'),
#                 ('Po301', 'Portraits', 'Black & White', 400, '2 weeks'),
#                 ('Po302', 'Portraits', 'Colour', 500, '2 weeks'),
#                 ('A401', 'A4 Comm', 'Black & White', 1500, '2 weeks'),
#                 ('A402', 'A4 Comm', 'Colour', 2000, '2 weeks'),
#                 ('A3501', 'A3 Comm', 'Black & White', 2500, '3 weeks'),
#                 ('A3502', 'A3 Comm', 'Colour', 3000, '3 weeks')""")

##Create customer table

# c.execute(""" CREATE TABLE customers (
#           name TEXT,
#           delivery_address TEXT,
#           instagram_handle TEXT)""")

# c.execute(""" INSERT INTO customers (name, delivery_address, instagram_handle)
#           VALUES('Jane Doe', '123 Corn Road', 'janedough'),
#                 ('Lara Smith', '24 Apple Lane', 'laaaaara'),
#                 ('Mia Trudouw', '8 Lettuce Close', 'miamoo'),
#                 ('Rebekah Solomon', '21 Morning Street', 'bekkysaurus')""")

##Create commission orders table

# c.execute(""" CREATE TABLE orders (
#           instagram_handle TEXT,
#           item_id TEXT,
#           payment BOOLEAN,
#           payment_date DATE,
#           in_progress TEXT)""")

# c.execute(""" INSERT INTO orders (instagram_handle, item_id, payment, payment_date, in_progress)
#           VALUES('janedough', 'LC203', 'YES', '20240903', 'COMPLETED'),
#                 ('laaaaara', 'A3501', 'NO', '20240905', 'NO'),
#                 ('miamoo', 'DaDo201', 'YES', '20240905', 'YES'),
#                 ('bekkysaurus', 'DD101', 'YES', '20240908', 'NO')""")

##Check which commissions are in progress

# in_progress = c.execute(""" SELECT in_progress
#           FROM orders""")

##Now we can see that Jane has a completed commission.

##Use Outer join to find out Jane Doe's address for the completed order

# c.execute(""" SELECT * FROM customers 
#           LEFT OUTER JOIN orders ON customers.instagram_handle = orders.instagram_handle
#           WHERE name = 'Jane Doe' """)
# print(c.fetchall())


# conn.commit()
conn.close()