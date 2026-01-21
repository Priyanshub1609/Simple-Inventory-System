from store import Store
from product import Product

# Create Store
my_store = Store("Tech Store")

# Create Products
p1 = Product("Laptop", 60000, "Electronics")
p2 = Product("Mobile", 30000, "Electronics")
p3 = Product("Headphones", 2000, "Accessories")

# Add Products
my_store.inventory.add_product(p1)
my_store.inventory.add_product(p2)
my_store.inventory.add_product(p3)

# Show Summary
my_store.show_summary()

# Operator Overloading Test
print("\nCombined Price of Laptop and Mobile:", p1 + p2)
