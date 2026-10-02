import tkinter as tk
from tkinter import messagebox

# ---------------- Backend ----------------
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})

    def remove_item(self, item):
        self.items = [i for i in self.items if i["item"] != item]

    def get_total(self):
        return sum(i["price"] for i in self.items)

    def list_items(self):
        return [f"{i['item']} - ₹{i['price']}" for i in self.items]


# ---------------- Frontend ----------------
class ShoppingApp:
    def __init__(self, root):
        self.cart = ShoppingCart()

        root.title("Shopping Cart")
        root.geometry("400x400")

        # Product list
        self.products = {
            "Laptop": 50000,
            "Phone": 20000,
            "Headphones": 2000,
            "Keyboard": 1500,
            "Mouse": 800
        }

        tk.Label(root, text="Available Products", font=("Arial", 14)).pack(pady=10)

        # Dropdown menu for products
        self.selected_product = tk.StringVar(root)
        self.selected_product.set("Laptop")  # default
        product_menu = tk.OptionMenu(root, self.selected_product, *self.products.keys())
        product_menu.pack(pady=5)

        # Add to cart button
        tk.Button(root, text="Add to Cart", command=self.add_to_cart).pack(pady=5)

        # Cart display
        tk.Label(root, text="Your Cart", font=("Arial", 14)).pack(pady=10)
        self.cart_listbox = tk.Listbox(root, width=40, height=10)
        self.cart_listbox.pack(pady=5)

        # Total price
        self.total_label = tk.Label(root, text="Total: ₹0", font=("Arial", 12))
        self.total_label.pack(pady=10)

        # Checkout button
        tk.Button(root, text="Checkout", command=self.checkout).pack(pady=5)

    def add_to_cart(self):
        product = self.selected_product.get()
        price = self.products[product]
        self.cart.add_item(product, price)
        self.update_cart_display()

    def update_cart_display(self):
        self.cart_listbox.delete(0, tk.END)
        for item in self.cart.list_items():
            self.cart_listbox.insert(tk.END, item)
        self.total_label.config(text=f"Total: ₹{self.cart.get_total()}")

    def checkout(self):
        total = self.cart.get_total()
        if total == 0:
            messagebox.showinfo("Checkout", "Your cart is empty!")
        else:
            messagebox.showinfo("Checkout", f"Thank you for shopping!\nTotal Amount: ₹{total}")
            self.cart = ShoppingCart()
            self.update_cart_display()


# ---------------- Run App ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root)
    root.mainloop()
