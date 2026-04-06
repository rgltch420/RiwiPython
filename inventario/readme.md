# Inventory Management System in Python
![alt text](images.png)
## Project Description

The system provides features to:

- Add products with **auto-generated IDs**
- View the inventory
- Update and delete products
- Calculate inventory statistics
- Save and load data using CSV files

All interactions are performed through a **terminal-based menu**.


---

## 🚀 Key Features

- ✅ Automatic ID generation
- ✅ Data validation (price and quantity)
- ✅ Search products by name or ID
- ✅ Update existing products
- ✅ Delete products
- ✅ CSV data persistence
- ✅ Inventory statistics calculation
- ✅ Clean console interface (Windows & Linux compatible)

---
## 🧱 Project Structure (Modular Design)
project/
│
├── main.py # Entry point (main menu)
├── app.py # User interaction layer
└── service.py # Business logic and data handling


### 🔹 `main.py`
Handles:
- Program flow
- Menu system
- User options

### 🔹 `app.py`
Responsible for:
- User input (`input`)
- Output display (`print`)
- Connecting UI with logic

### 🔹 `service.py`
Contains:
- Inventory management
- ID generation
- File handling (CSV)
- Calculations

---

## 🛠 Technologies Used

- **Python 3**

### Libraries:

- `os` → Clear console
- `platform` → Detect operating system
- `pandas` → Handle CSV files

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone <https://github.com/rgltch420/RiwiPython.git>
cd <RiwiPython>