
# 📦 Inventory Management Program (Python)
~/Riwi Projects/images.png
## 📖 Description

This project is a **simple inventory management program written in Python**.
The program allows a user to **enter products, their prices, and quantities**, and then it calculates the **total cost of each product automatically**.

At the end, the program shows a **complete inventory with all the products entered**.

The goal of this program is to demonstrate basic programming concepts such as:

* Variables
* Dictionaries
* Functions
* Loops
* Error handling
* User input
* Basic calculations

This program runs **entirely in the terminal** and interacts with the user through text prompts.

---

# 🎯 Objective of the Program

The main objective of this program is to **create a small inventory system** that allows a user to:

1. Enter how many products they want to register.
2. Input the **name**, **price**, and **quantity** of each product.
3. Automatically calculate the **total cost**.
4. Store the information inside a **dictionary called `inventory`**.
5. Display the final inventory at the end.

---

# 🧠 Conceptual Explanation (Very Simple)

Imagine you have a **toy store** 🧸.

You want to write down:

* the name of the toy
* how much it costs
* how many you have

This program is like a **notebook that remembers all your toys**.

Each time you add a toy, the program writes it inside a **special Python dictionary** called:

```
inventory
```

Inside that notebook, every product will look like this:

```
Toy Car
   price: 10
   quantity: 5
   total_cost: 50
```

---

# 🛠 Technologies Used

* **Python 3**
* Standard Python libraries:

  * `os`
  * `pprint`

No external libraries are required.

---

# 📚 Libraries Used

## 1️⃣ `os`

```
import os
```

This library allows Python to **communicate with the operating system**.

In this program it is used to **clear the terminal screen**.

Example used in the code:

```
os.system("cls" if os.name == "nt" else "clear")
```

Explanation:

* If the system is **Windows**, it runs `cls`
* If the system is **Linux or Mac**, it runs `clear`

This keeps the terminal **clean and easy to read**.

---

## 2️⃣ `pprint`

```
import pprint
```

`pprint` means **pretty print**.

It prints complex data structures (like dictionaries) in a **clean and readable format**.

Example:

```
pprint.pprint(inventory)
```

Instead of printing everything in one messy line, it prints it nicely organized.

---

# 📦 Global Variable

```
inventory = {}
```

This creates an **empty dictionary**.

Think of it like an **empty box** where we will store all the products.

Each product will be saved like this:

```
inventory["product_name"] = {
    "precio": price,
    "cantidad": quantity,
    "costo_total": total_cost
}
```

So the dictionary might look like:

```
{
 "Apple": {
     "precio": 2,
     "cantidad": 10,
     "costo_total": 20
 }
}
```

---

# 🔧 Function: `create_product()`

This function is responsible for **creating and storing a product in the inventory**.

```
def create_product():
```

---

# 🔁 Infinite Loop

```
while True:
```

This loop means:

> "Keep asking the user for information until the data is correct."

If the user makes a mistake, the program **does not crash**.
Instead, it **asks again**.

---

# ⌨️ Asking the User for Data

The program asks the user for three things:

```
name_product = input("Enter the name of product: ").strip()
price_input = input("Enter the price of product: ").strip()
quantity_input = input("Enter the quantity of product: ").strip()
```

Explanation:

* `input()` lets the user type something.
* `.strip()` removes extra spaces.

Example:

User types:

```
  apple
```

`.strip()` converts it to:

```
apple
```

---

# 🧹 Clearing the Screen

```
os.system("cls" if os.name == "nt" else "clear")
```

This clears the terminal so the screen does not become messy.

---

# ⚠️ Checking Empty Fields

```
if not (name_product and price_input and quantity_input):
```

This checks if the user **left any field empty**.

Example of bad input:

```
name:
price:
quantity: 5
```

If something is empty, the program prints:

```
No dejes campos vacios
```

and asks again.

---

# 🔢 Converting Data Types

```
price = float(price_input)
quantity = int(quantity_input)
```

Explanation:

Users type numbers as **text**, so we convert them:

| Input  | Converted To |
| ------ | ------------ |
| "10.5" | float        |
| "5"    | int          |

This allows the program to **perform calculations**.

---

# 🚫 Checking Negative Numbers

```
if price < 0 or quantity < 0:
```

This prevents invalid data.

Example of invalid input:

```
price: -5
```

The program will show:

```
Ingresa solo numeros positivos
```

---

# 🧮 Calculating Total Cost

```
total_cost = price * quantity
```

Example:

```
price = 10
quantity = 5
```

Result:

```
total_cost = 50
```

---

# 💾 Saving the Product

The product is stored inside the dictionary:

```
inventory[name_product] = {
    "precio": price,
    "cantidad": quantity,
    "costo_total": total_cost
}
```

Example result:

```
{
 "Laptop": {
   "precio": 500,
   "cantidad": 2,
   "costo_total": 1000
 }
}
```

---

# 🔙 Returning the Product Name

```
return name_product
```

This sends the product name back to the main program so we can print:

```
Producto añadido con éxito
```

---

# ⚠️ Error Handling

```
except ValueError:
```

This happens when the user types something invalid.

Example:

```
price: ten
```

Python cannot convert `"ten"` into a number, so it triggers the error.

The program then shows:

```
Error: ID, Precio y Cantidad deben ser números.
```

---

# 🔁 Main Program Loop

The program starts with:

```
while True:
```

This loop controls the entire program.

---

# 📥 Asking How Many Products

```
num_products = int(input("enter the quantity of products required: "))
```

Example:

```
3
```

The program will ask the user to register **3 products**.

---

# 🚫 Preventing Invalid Amounts

```
if num_products < 1:
```

This prevents values like:

```
0
-5
```

The program requires **at least one product**.

---

# 🔁 Product Registration Loop

```
for _ in range(num_products):
```

If the user entered:

```
3
```

The loop will run **3 times**.

Example output:

```
Registro de producto 1
Registro de producto 2
Registro de producto 3
```

---

# 📢 Success Message

After adding a product:

```
print(f"¡Producto '{added_name}' añadido con éxito!")
```

Example:

```
Producto 'Apple' añadido con éxito
```

---

# 🧹 Clearing the Screen Again

Before showing the final inventory, the screen is cleared again:

```
os.system("cls" if os.name == "nt" else "clear")
```

---

# 📊 Showing Final Inventory

```
pprint.pprint(inventory)
```

Example output:

```
{
 'Apple': {'precio': 2.0, 'cantidad': 10, 'costo_total': 20.0},
 'Milk': {'precio': 3.5, 'cantidad': 4, 'costo_total': 14.0}
}
```

---

# ▶️ Example Execution

Example run of the program:

```
enter the quantity of products required: 2

--- Registro de producto 1 ---
Enter the name of product: Apple
Enter the price of product: 2
Enter the quantity of product: 10

Producto 'Apple' añadido con éxito!

--- Registro de producto 2 ---
Enter the name of product: Milk
Enter the price of product: 3
Enter the quantity of product: 5

Producto 'Milk' añadido con éxito!
```

Final output:

```
--- inventario final ---

{
 'Apple': {'precio': 2.0, 'cantidad': 10, 'costo_total': 20.0},
 'Milk': {'precio': 3.0, 'cantidad': 5, 'costo_total': 15.0}
}
```

---

# 💡 Concepts Demonstrated

This project demonstrates several important programming concepts:

* Functions
* Dictionaries
* Loops (`while`, `for`)
* Error handling (`try/except`)
* User input
* Data validation
* Arithmetic operations
* Modular code design

---

# 🚀 Possible Improvements

This program could be improved by adding:

* Product IDs
* Delete products
* Update products
* Save inventory to a file
* Load inventory from a file
* Graphical interface

---

