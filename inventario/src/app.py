import os
import platform
import pandas as pd 





inventory = []
id_product_a = 0


def clear_screen():
     
#Esta funcion es la encargada de limpiar pantalla valida NT si es windows o prosix si es sistemas unix dependiendo si es windows hace un CLS de lo contario usa clear

      if os.name == 'nt':
        os.system('cls')
      else:
        os.system('clear')


def create_product():
    
# Esta funcion es la encargada de crear ID, NOMBRES, PRECIOS, Y CANTIDADES de cada productos 
    
    try:
        global id_product_a
        id_product_a +=1
        id_product = f"ID PR000{id_product_a}"
        if id_product_a >= 10:
           id_product = f"ID PR0{id_product_a}"
        elif id_product_a >= 100:
           id_product = f"ID PR {id_product_a}"   
         
        name_product = input("Enter the name of product: ").lower()
        price = float(input("Enter the price of product: "))
        quantity = int(input("Enter the quantity of product: "))

        # Validación
        if price > 0 and quantity > 0:
            product = {
                "id": id_product,
                "name": name_product,
                "price": price,
                "quantity": quantity
            }

            inventory.append(product)
            print(f"Product added successfully; ID created successfully. {id_product}")

        else:
            print("Enter valid values ​​(greater than 0).")

    except ValueError:
        print("Enter the requested value correctly.")

def show_inventory():
  
# Esta funcion es para mostrar inventario
    
    if len(inventory) == 0:
        print("The inventory is empty.")
    else:
        print("\n--- INVENTORY ---")
        for product in inventory:
            print(f"ID: {product['id']}|Producto: {product['name']} | Precio: {product['price']} | Cantidad: {product['quantity']}")



def total_value():
    
# Funcion para calcular el valor total de los productos cantidad por precio
     
    total = 0

    for product in inventory:
        total += product["price"] * product["quantity"]

    return total

def stadistics():
  
# Funcion para mostrar el valor total de los productos y la cantidad de productos total de los productos   
    
    show_inventory()

    total_products = 0

    for product in inventory:
        total_products += product["quantity"]

    print("\n--- ESTADÍSTICAS ---")
    print(f"Total inventory value: {total_value()}")
    print(f"Total quantity of products: {total_products}")

def search_products():

# Funcion encargada para buscar productos por ID o nombre
    
    show_inventory()
    
    search_term = input("Enter ID or name of product are you looking for: ")
    found = False
    for product in inventory:     
        if str(product["id"]) == search_term or search_term in product["name"]:
            print("Product finded")
            print(f"{'id'} | Name {product['name']} | Price{product['price']}")
            
            
            
            

def update_products():  
    show_inventory()
    if len(inventory)==0:
        return
    id_to_change = input("Add the ID or name of the product you wish to change: ")
    found = False
    for product in inventory:
        # Validamos contra ID o Nombre
        if product["id"].lower() == id_to_change or product["name"].lower() == id_to_change:
            print(f"\nEditing product: {product['name']}")
            
            try:
                # Pedimos nuevos datos
                product["name"] = input("New name: ").lower() or product["name"]
                product["price"] = float(input("New price: ") or product["price"])
                product["quantity"] = int(input("New quantity: ") or product["quantity"])
                
                print("\n[√] Product updated successfully!")
                found = True
                break
            except ValueError:
                print("\n[!] Error: Please enter valid numbers for price and quantity.")
                return

    if not found:
        print("\n[!] Product not found in the inventory.")



def delete_products():
    show_inventory()
    if len(inventory)==0:
        return
    id_to_change = input("Add the ID or name of the product you wish to change: ")
    for product in inventory:
        # Validamos contra ID o Nombre
        if product["id"].lower() == id_to_change or product["name"].lower() == id_to_change:
            print(f"\nproduct: {product['name']}")
            
            

def ascii_art():
    
# Se encarga de realizar el arte ascii y dectetar el sistema operativo para que en los distintos sistemas operativos salga bien entonces lo que hace es tomar con el condicional if sistema
# decteta el sistema y la variable sistema lo que hace es dectetar que so es por eso llama a la funcion .SYSTEM de la libreria platform y el print pinta de blanco las letras 
 
    sistema = platform.system()
    
    if sistema == "Windows":
        os.system('color')
        print(f"--- Ejecutando en {sistema} (Modo compatibilidad activado) ---\n")
    else:
        print(f"--- Ejecutando en {sistema} ---\n")
        
    banner = (r"""
          
 ██████╗ ██████╗ ██████╗ ███████╗██████╗     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗███╗   ███╗███████╗███╗   ██╗████████╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║       ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║       ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║       ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
 ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝       ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
                                                                                                                                                                                                  
            """)    
    print("\033[1;37m" + banner + "\033[0m")
    
    
    
    
def save_data():
    data_save = pd.DataFrame(inventory)
    data_save.to_csv('products.csv', index=False, encoding='UTF-8')
    print("Products successfully saved")
    

def read_data():
    global inventory
    try:
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, '..', 'products.csv')
        data = pd.read_csv(file_path)
        inventory = data.to_dict(orient='records')
       
        print("Data loaded successfully")
    except FileNotFoundError:
        print("File not found. Save data first.")
        
    
    
while True:
    # print("\n===== ORDER MANAGEMENT SYSTEM =====")
    
    ascii_art()
        
    print("1. Add product")
    print("2. Show Inventary")
    print("3. Calculate estadistics")
    print("4. Update Inventory")
    print("5. Delete Inventory")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")

    option = input("Choice your option: ")

    clear_screen()

    match option:
        case "1":
            create_product()
        case "2":    
            show_inventory()
        case "3":
            stadistics()
        case "4":
            update_products()
        case "5":
            delete_products()  
        case "6":
            save_data()
        case "7":
            read_data()             
        case "8":
            print("Exit ...")
            break 
        case _:
            print("Invalid Option, try again")