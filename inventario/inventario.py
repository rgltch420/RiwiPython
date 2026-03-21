import os
import pprint
inventory = []


def create_product():
    id_product = int(input("Enter the id of product: "))
    name_product = input("Enter the name of product: ")
    price = float(input("Enter the price of product: "))
    quantity = int(input("Enter the quantity of product: "))
    os.system("clear") 

    inventory[id_product] = {"name": name_product, "price": price, "quantity": quantity}


    return inventory, price, quantity, id_product,name_product

def total_value(id_product):
    totalprice = inventory[id_product]["price"] * inventory[id_product]["quantity"]
    return totalprice


option_products_requier = int(input("enter the quantity of products required: "))
quantity_product_requier = 0

while quantity_product_requier < option_products_requier:
    quantity_product_requier += 1  
    try:
        inventory, price, quantity, id_product,name_product = create_product()

        if price > 0 and quantity > 0:
            print(f"Felicitaciones el producto id: {id_product} fue añadido exitosamente")
            
            
        else:
            print("Ingresa valores correctos solicitados")
    except ValueError:
        print("Ingresa el valor solicitado correctamente") 
               
else:
    os.system("clear")
    print("Agregaste productos correctamente")
    for key, value in inventory.items():
        print(f"{key}")
       
        # for key,value in value.items():
        #     print(f"{value}")
      

         
    


