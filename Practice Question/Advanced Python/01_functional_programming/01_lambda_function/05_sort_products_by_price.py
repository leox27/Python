"""
#5. Sort Products by Price
products = [
    ("Laptop", 75000),
    ("Mouse", 1200),
    ("Keyboard", 2500),
    ("Monitor", 15000)
]

Use sorted() with a lambda function to sort products by price from lowest to highest.
Expected:
[
    ('Mouse', 1200),
    ('Keyboard', 2500),
    ('Monitor', 15000),
    ('Laptop', 75000)
]
"""

products = [
    ("Laptop", 75000),
    ("Mouse", 1200),
    ("Keyboard", 2500),
    ("Monitor", 15000)
]

sorted_price = sorted(products, key=lambda x: x[1])
print(sorted_price)
'''
[('Mouse', 1200), ('Keyboard', 2500), ('Monitor', 15000), ('Laptop', 75000)]
'''
