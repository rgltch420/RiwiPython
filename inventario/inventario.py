import os
import pprint
inventory ={}


def create_product():
   while True:
        try:
            id_input = input("Enter the id of product: ").strip()
            name_product = input("Enter the name of product: ").strip()
            price_input = input("Enter the price of product: ").strip()
            quantity_input = input("Enter the quantity of product: ").strip()
            os.system("cls" if os.name == "nt" else "clear") 
            if not (id_input and name_product and price_input and quantity_input):
                 print("No dejes campos vacios o vacios")
                 continue
            id_product = int(id_input)
            price = float(price_input)
            quantity = int(quantity_input)
            if id_product < 0 or price < 0 or quantity < 0:
                  print("Ingresa solo numeros positivos por encima de 0")
                  continue
            os.system("cls" if os.name == "nt" else "clear")
            inventory[id_product] = {"name": name_product, "price": price, "quantity": quantity}
            return inventory, price, quantity, id_product,name_product 
        except ValueError:
            print("Error: ID, Precio y Cantidad deben ser números.")
        

def total_value(id_product):
    return inventory[id_product]["price"] * inventory[id_product]["quantity"]



while True:
    try:
        option_products_requier = int(input("enter the quantity of products required: "))
        if option_products_requier < 1:
            print("Debe ser al menos 1 producto")
            continue
        value_inventario = 0
        for _ in range(option_products_requier):
            id_create = create_product()
            value_inventario += total_value(id_create)
            print(f"Producto {id_create} añadido")
        os.system("cls" if os.name == "nt" else "clear")    
        print("--- inventario final ---")
        pprint.pprint(inventory)  
        break                
        
    except ValueError:
            print("Ingresa un numero entero positivo para la cantidad de productos")         

         
    


