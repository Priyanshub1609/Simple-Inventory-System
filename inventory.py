class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} removed from inventory")
                return
        print("Product not found")

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_all_products(self):
        for product in self.products:
            print(product)
