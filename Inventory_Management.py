import json 
class inventory:
    admin = [{"username": "yitzerk", "password": "adminYitz@ims"}]

    def login_admin(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for admin_user in inventory.admin:
            if admin_user["username"] == username and admin_user["password"] == password:
                print("Login successful!")
                return True

        print("Invalid username or password.")
        return False

    def admin_menu(self):
        if not self.login_admin():
            return
        while True:
            print("\nAdmin Menu:")
            print("1. Add User")
            print("2. Login User")
            print("3. Add Product")
            print("4. View Products")
            print("5. Sell Product")
            print("6. View Sales")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                self.add_users()
            elif choice == "2":
                self.login_user()
            elif choice == "3":
                self.add_product()
            elif choice == "4":
                self.view_products()
            elif choice == "5":
                self.sell_product()
            elif choice == "6":
                self.view_sales()
            elif choice == "7":
                print("Exiting admin menu.")
                break
            else:
                print("Invalid choice. Please try again.")
    def add_users(self):
        username = input("Enter new username: ")
        password = input("Enter new password: ")

        new_user = {"username": username,"password": password}

        with open("users.json", "a") as userfile:
            json.dump(new_user, userfile)

        print("New user added successfully.")

    def login_user(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        with open("users.json", "r") as userfile:
            users = json.load(userfile)

        for user in users:
            if user["username"] == username and user["password"] == password:
                print("Login successful!")
                return True

        print("Invalid username or password.")
        return False
    def user_menu(self):
        if self.login_user():
            while True:
                print("\nUser Menu:")
                print("1. View Products")
                print("2. Sell Product")
                print("3. View Sales")
                print("4. Exit")

                choice = input("Enter your choice (1-4): ")

                if choice == "1":
                    self.view_products()
                elif choice == "2":
                    self.sell_product()
                elif choice == "3":
                    self.view_sales()
                elif choice == "4":
                    print("Exiting user menu.")
                    break
                else:
                    print("Invalid choice. Please try again.")
    def add_product(self):
        product_name = input("Enter product name: ")
        stock = int(input("Enter stock quantity: "))
        price = float(input("Enter product price: "))
        profit_margin = float(input("Enter profit margin percentage: "))

        new_product = {
            "product": product_name,
            "stock": stock,
            "price": price,
            "profit margin": profit_margin,
            "stock sold": 0,
            "net sales": 0,
            "Net Profit":0}

        with open("products.json", "a") as productfile:
            json.dump(new_product, productfile)

        print("Product added successfully.")
    def view_products(self):
        with open("products.json", "r") as productfile:
            products = json.load(productfile)

        if not products:
            print("No products available.")
            return

        print("Available Products:")
        for product in products:
            print(f"Product: {product['product']}, Stock: {product['stock']}, Price: {product['price']}, Profit Margin: {product['profit margin']}%")
    def sell_product(self):
     product_name = input("Enter product name to sell: ")
     quantity = int(input("Enter quantity to sell: "))

     with open("products.json", "r") as productfile:
        products = json.load(productfile)
 
     for product in products:
        if product["product"].lower() == product_name.lower():
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                return
            if quantity > product["stock"]:
                print("Not enough stock available.")
                return
            product["stock"] -= quantity
            sale_amount = quantity * product["price"]
            profit = sale_amount * (product["profit margin"] / 100)
            with open("sales.json", "r") as salesfile:
                sales = json.load(salesfile)
            receipt_no = sales[-1]["receipt_no"] + 1 if sales else 100
            sale = {"receipt_no": receipt_no,
                "product": product["product"],
                "quantity": quantity,
                "sale_amount": sale_amount,
                "profit": profit}
            sales.append(sale)
            with open("products.json", "w") as productfile:
                json.dump(products, productfile, indent=4)
            with open("sales.json", "w") as salesfile:
                json.dump(sales, salesfile, indent=4)
            receipt = (
                f"Receipt:\n"
                f"Receipt No: {receipt_no}\n"
                f"Product: {product['product']}\n"
                f"Quantity Sold: {quantity}\n"
                f"Price: ₹{product['price']}\n"
                f"Total: ₹{sale_amount}\n"
                f"Profit: ₹{profit}")
            with open("receipt.txt", "w") as receiptfile:
                receiptfile.write(receipt)

            print(receipt)
            return

     print("Product not found.")
    def view_sales(self):
        with open("sales.json", "r") as salesfile:
            sales = json.load(salesfile)

        if not sales:
            print("No sales records available.")
            return

        print("Sales Records:")
        for sale in sales:
            print(f"Receipt No: {sale['receipt_no']}, Product: {sale['product']}, Quantity Sold: {sale['quantity']}, Sale Amount: ₹{sale['sale_amount']}, Profit: ₹{sale['profit']}")



def main():
    inv = inventory()
    while True:
        print("\nMain Menu:")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            inv.admin_menu()
        elif choice == "2":
            inv.user_menu()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
# main()
i = inventory()
i.add_product()