import os
import pprint
inventory ={}


def create_product():
   while True:
        try:
            name_product = input("Enter the name of product: ").strip()
            price_input = input("Enter the price of product: ").strip()
            quantity_input = input("Enter the quantity of product: ").strip()
            os.system("cls" if os.name == "nt" else "clear") 
            if not (name_product and price_input and quantity_input):
                 print("No dejes campos vacios o vacios")
                 continue
            
            price = float(price_input)
            quantity = int(quantity_input)

            if price < 0 or quantity < 0:
                  print("Ingresa solo numeros positivos por encima de 0")
                  continue
            
            total_cost = price * quantity
            inventory[name_product]={
                 "precio": price,
                 "cantidad": quantity,
                 "costo_total": total_cost
            }
            return name_product
        except ValueError:
            print("Error: ID, Precio y Cantidad deben ser números.")
        

while True:
    try:
        num_products = int(input("enter the quantity of products required: "))
        if num_products < 1:
            print("Debe ser al menos 1 producto")
            continue
        for _ in range(num_products):
            print(f"\n--- Registro de producto {_ + 1} ---")
            added_name = create_product()
            print(f"¡Producto '{added_name}' añadido con éxito!")
        os.system("cls" if os.name == "nt" else "clear")    
        print("--- inventario final ---")
        pprint.pprint(inventory)  
        break                
        
    except ValueError:
            print("Ingresa un numero entero positivo para la cantidad de productos")         

         
    


