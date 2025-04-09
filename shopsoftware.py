
class Product:
    def __init__(self, name, price, quantity):
        self.name = name  
        self.price = price 
        self.quantity = quantity 

    def update_quantity(self, quantity_sold):
        """Update the product quantity after a sale"""
        if self.quantity >= quantity_sold:
            self.quantity -= quantity_sold
            return True
        return False

    def __str__(self):
        return f"{self.name} | Price: {self.price} | Quantity: {self.quantity}"

class Shop:
    def __init__(self, shop_name, address, contact):
        self.shop_name = shop_name 
        self.address = address
        self.contact = contact
        self.products = [] 
        self.tax_rate = 0.1  
        self.sales = []  

    def add_product(self, name, price, quantity):
        """Add a new product to the shop"""
        product = Product(name, price, quantity)
        self.products.append(product)

    def delete_product(self, product_name):
        """Delete a product from the shop"""
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Product '{product_name}' has been deleted.")
                return True
        print(f"Product '{product_name}' not found.")
        return False

    def display_products(self):
        """Display all available products"""
        if not self.products:
            print("No products available.")
            return
        print("\nAvailable Products:")
        for product in self.products:
            print(product)

    def sell_product(self, product_name, quantity_sold):
        """Sell a product, reduce its quantity, and return the price"""
        for product in self.products:
            if product.name == product_name:
                if product.update_quantity(quantity_sold):
                    total_price = product.price * quantity_sold
                    print(f"Sold {quantity_sold} of {product_name}.")
                    return total_price, product.price
        print(f"Error: Not enough stock or product '{product_name}' not found.")
        return 0, 0

    def generate_invoice(self, sold_items):
        """Generate the invoice for sold products"""
        print("\n--- INVOICE ---")
        print(f"Shop Name: {self.shop_name}")
        print(f"Address: {self.address}")
        print(f"Contact: {self.contact}")
        print("-" * 40)

        total_price = 0
        total_tax = 0
        for item in sold_items:
            product_name, quantity, price_per_unit = item
            subtotal = price_per_unit * quantity
            tax = subtotal * self.tax_rate
            total_price += subtotal
            total_tax += tax
            print(f"{product_name} | Qty: {quantity} | Price: {price_per_unit} | Subtotal: {subtotal} | Tax: {tax}")

        total_amount = total_price + total_tax
        print("-" * 40)
        print(f"Total Price: {total_price}")
        print(f"Total Tax: {total_tax}")
        print(f"Total Amount: {total_amount}")

def main():
    shop = Shop("Tech World", "katraj, Pune City", "Phone: 000-000-0000")

    while True:
        print("\n--- Shop Management ---")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. Display Products")
        print("4. Sell Product")
        print("5. Generate Invoice")
        print("6. Exit")
                
        
        choice = input("Enter your choice from up: ")

        if choice == '1':  
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            shop.add_product(name, price, quantity)
            print(f"Product '{name}' added successfully.")

        elif choice == '2': 
            name = input("Enter product name to delete: ")
            shop.delete_product(name)

        elif choice == '3':  
            shop.display_products()

        elif choice == '4':  
            product_name = input("Enter product name to sell: ")
            quantity_sold = int(input("Enter quantity to sell: "))
            price, unit_price = shop.sell_product(product_name, quantity_sold)
            if price > 0:
                sold_items = [(product_name, quantity_sold, unit_price)]

        elif choice == '5':  
            shop.generate_invoice(sold_items)

        elif choice == '6':  
            print("Exiting... Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    

