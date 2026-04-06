import platform
from service import *

def clear_screen():  
#Esta funcion es la encargada de limpiar pantalla valida NT si es windows o prosix si es sistemas unix dependiendo si es windows hace un CLS de lo contario usa clear

      if os.name == 'nt':
        os.system('cls')
      else:
        os.system('clear')
          
def create_product():
# Esta funcion es la encargada de crear ID, NOMBRES, PRECIOS, Y CANTIDADES de cada productos 
    try:
          
        id_product = generate_id() 
        name_product = input("Enter the name of product: ").lower()
        price = float(input("Enter the price of product: "))
        quantity = int(input("Enter the quantity of product: "))

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
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗███╗   ███╗███████╗███╗   ██╗████████╗
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                                                                                                                                     
                                                                                                                                                     
                                                                                                                                                                                                  
            """)    
    print("\033[1;37m" + banner + "\033[0m")
  
