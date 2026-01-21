class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product(Name: {self.name}, Price: ₹{self.price}, Category: {self.category})"

    def __add__(self, other):
        return self.price + other.price
