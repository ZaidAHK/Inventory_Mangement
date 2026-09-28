# Inventory Management System

A Python-based inventory management system built using **Python and JSON**. This project allows administrators and users to manage products, track inventory, process sales, calculate revenue and profit, and generate receipts.

## Features

* Admin login
* User login
* Add new users
* Add new products
* Product IDs
* View available products
* Track product stock
* Sell products
* Automatic stock deduction
* Calculate total sales
* Calculate profit
* Generate unique receipt numbers
* Generate receipts
* Store sales history
* JSON-based data storage
* Command-line interface

## Project Structure

```text
inventory-management-system/
│
├── inventory.py
├── products.json
├── users.json
├── sales.json
├── receipt.txt
├── README.md
├── .gitignore
└── LICENSE
```

## How It Works

The system separates inventory data from sales data.

### Products

`products.json` stores information about products:

```json
{
    "product_id": 1001,
    "product": "Wireless Mouse",
    "stock": 50,
    "price": 799,
    "profit margin": 20
}
```

### Users

`users.json` stores registered users:

```json
{
    "username": "example",
    "password": "example123"
}
```

### Sales

`sales.json` stores completed transactions:

```json
{
    "receipt_no": 100,
    "product": "Wireless Mouse",
    "quantity": 2,
    "sale_amount": 1598,
    "profit": 319.6
}
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/inventory-management-system.git
```

### 2. Open the project

```bash
cd inventory-management-system
```

### 3. Run the program

```bash
python inventory.py
```

No external Python packages are required. The project uses Python's built-in `json` and `os` modules.

## Main Menu

When the program starts, you will see:

```text
Main Menu:
1. Admin Login
2. User Login
3. Exit
```

### Admin Features

After successful admin authentication:

```text
Admin Menu:
1. Add User
2. Login User
3. Add Product
4. View Products
5. Sell Product
6. View Sales
7. Exit
```

### User Features

Users can:

* View products
* Sell products
* View sales
* Exit the user menu

## Sales Calculation

The system calculates the sale amount using:

```python
sale_amount = quantity * price
```

Profit is calculated using:

```python
profit = sale_amount * (profit_margin / 100)
```

For example, if a product costs ₹799 and 2 units are sold:

```text
Sale Amount = 2 × ₹799
Sale Amount = ₹1598
```

With a 20% profit margin:

```text
Profit = ₹1598 × 20 / 100
Profit = ₹319.60
```

## Receipt System

Each completed sale receives a unique receipt number.

The first sale starts at:

```text
Receipt No: 100
```

The next transactions become:

```text
Receipt No: 101
Receipt No: 102
Receipt No: 103
```

A receipt is also saved to:

```text
receipt.txt
```

Example:

```text
Receipt
Receipt No: 100
Product: Wireless Mouse
Quantity Sold: 2
Price: ₹799
Total: ₹1598
Profit: ₹319.60
```

## Technologies Used

* **Python**
* **JSON**
* **Object-Oriented Programming**
* **File Handling**
* **Dictionaries**
* **Lists**
* **Loops**
* **Functions**
* **Exception Handling**

## Current Limitations

This project is designed primarily as a learning project.

Some limitations include:

* Passwords are currently stored in plain text.
* The application uses JSON instead of a database.
* The interface is command-line based.
* There is no password hashing.
* There are no advanced user permissions.
* It is not designed for multiple users accessing the data simultaneously.

## Future Improvements

Possible improvements include:

* Tkinter GUI
* SQLite database
* Password hashing
* Product search
* Edit products
* Delete products
* Low-stock alerts
* Product categories
* Sales reports
* Daily/monthly revenue reports
* Inventory valuation
* CSV export
* PDF invoices
* User roles and permissions
* Database-backed authentication
* Dashboard with charts

## Learning Goals

This project was built to practice:

* Python classes and objects
* JSON data management
* File handling
* CRUD-style operations
* Inventory logic
* Sales calculations
* Authentication logic
* Working with structured data

## Disclaimer

This is an educational project and should not be used as a production inventory system without additional security, authentication, validation, database management, and error handling.

## License

This project is licensed under the MIT License.
