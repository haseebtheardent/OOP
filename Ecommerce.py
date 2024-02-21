class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product):
        for item in self.items:
            if item["product"] == product:
                self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def __str__(self):
        cart_str = "Shopping Cart:\n"
        for item in self.items:
            cart_str += f"{item['product']} x{item['quantity']}\n"
        cart_str += f"Total: ${self.calculate_total():.2f}"
        return cart_str


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity=1):
        self.shopping_cart.add_item(product, quantity)

    def remove_from_cart(self, product):
        self.shopping_cart.remove_item(product)

    def checkout(self):
        total = self.shopping_cart.calculate_total()
        print(f"Thank you, {self.name}! Your total is ${total:.2f}.")
        self.shopping_cart = ShoppingCart()

# Sample usage
# Create some products
product1 = Product(1, "T-shirt", 15.99)
product2 = Product(2, "Jeans", 29.99)
product3 = Product(3, "Sneakers", 49.99)

# Create a customer
customer = Customer("Alice", "alice@example.com")

# Add products to the customer's cart
customer.add_to_cart(product1, 2)
customer.add_to_cart(product2)
customer.add_to_cart(product3)

# Display the cart contents and total
print(customer.shopping_cart)

# Checkout
customer.checkout()