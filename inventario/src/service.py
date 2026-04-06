import pandas as pd 
import os

inventory = []
id_product_a = 0

def generate_id():
    global id_product_a
    id_product_a +=1
    if id_product_a >= 10:
       return f"ID PR0{id_product_a}"
    elif id_product_a >= 100:
       return f"ID PR {id_product_a}" 
    else:
        return f"ID PR000{id_product_a}"

def total_value():
# Funcion para calcular el valor total de los productos cantidad por precio
     
    total = 0

    for product in inventory:
        total += product["price"] * product["quantity"]

    return total

def save_data():
    data_save = pd.DataFrame(inventory)
    data_save.to_csv('products.csv', index=False, encoding='UTF-8')
    print("Products successfully saved")
    
def read_data():
    global inventory
    
    invalid_rows = 0
    loaded_products = []

    try:
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, '..', 'products.csv')

        data = pd.read_csv(file_path, encoding='utf-8')

        
        data.columns = [col.strip().lower() for col in data.columns]

        required = {"name", "price", "quantity"}

        if not required.issubset(set(data.columns)):
            print("Error: The CSV file must contain at least: name, price, quantity")
            return

        global id_product_a
        max_id = 0

        if "id" in data.columns:
            for _, row in data.iterrows():
                try:
                    raw_id = str(row["id"])
                    number = ''.join(filter(str.isdigit, raw_id))

                    if number:
                        number = int(number)
                        if number > max_id:
                            max_id = number
                except:
                    continue

        if max_id > id_product_a:
            id_product_a = max_id

       
        for _, row in data.iterrows():
            try:
                name = str(row["name"]).lower()
                price = float(row["price"])
                quantity = int(row["quantity"])

                if price < 0 or quantity < 0:
                    raise ValueError

                if "id" in data.columns and pd.notna(row["id"]) and str(row["id"]).strip() != "":
                    id_value = str(row["id"])
                else:
                    id_value = generate_id()

                product = {
                    "id": id_value,
                    "name": name,
                    "price": price,
                    "quantity": quantity
                }

                loaded_products.append(product)

            except (ValueError, TypeError):
                invalid_rows += 1

        if len(inventory) > 0:
            opti = input(
                "Overwrite current inventory?\n"
                "S = Replace\n"
                "N = Merge\n").lower()
        else:
            opti = "s"

      
        if opti == "s":
            inventory.clear()
            inventory.extend(loaded_products)

      
        elif opti == "n":
            action = "Merged inventory"

            for new_product in loaded_products:
                found = False

                for product in inventory:
                    if product["name"] == new_product["name"]:
                       
                        product["quantity"] += new_product["quantity"]

                        if product["price"] != new_product["price"]:
                            product["price"] = new_product["price"]

                        found = True
                        break

                if not found:
                    inventory.append(new_product)

        else:
            print("Invalid option")
            return

        print("\n--- LOAD SUMMARY ---")
        print(f"Products loaded: {len(loaded_products)}")
        print(f"Invalid rows omitted: {invalid_rows}")
        print(f"Action taken: {action}")

    except FileNotFoundError:
        print("Error: File not found.")
    except UnicodeDecodeError:
        print("Error: File encoding problem.")
    except Exception as e:
        print(f"Unexpected error: {e}")




