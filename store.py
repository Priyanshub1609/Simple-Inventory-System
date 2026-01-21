class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))
        category = input("Enter product category: ")

        product = Product(name, price, category)
        self.inventory.add_product(product)

    def show_summary(self):
        print(f"\nStore Name: {self.store_name}")
        print("Products in Inventory:")
        self.inventory.show_all_products()
        print("Total Inventory Value: ₹", self.inventory.get_total_value())
