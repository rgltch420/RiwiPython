import os
inventory = []

def clear_screen():
     
#Esta funcion es la encargada de limpiar pantalla valida NT si es windows o prosix si es sistemas unix dependiendo si es windows hace un CLS de lo contario usa clear

      if os.name == 'nt':
        os.system('cls')
      else:
        os.system('clear')


def create_product():
    
# Esta funcion es la encargada de crear ID, NOMBRES, PRECIOS, Y CANTIDADES de cada productos 

    try:
        id_product = int(input("Enter the id of product: "))
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
            print(f"Producto: {product['name']} | Precio: {product['price']} | Cantidad: {product['quantity']}")



def total_value():
    
# Funcion para calcular el valor total de los productos cantidad por precio
     
    total = 0

    for product in inventory:
        total += product["price"] * product["quantity"]

    return total

def statistics():
  
# Funcion para mostrar el valor total de los productos y la cantidad de productos total de los productos   
    
    
    if len(inventory) == 0:
        print("No products registered")
        return

    total_products = 0

    for product in inventory:
        total_products += product["quantity"]

    print("\n--- ESTADÍSTICAS ---")
    print(f"Total inventory value: {total_value()}")
    print(f"Total quantity of products: {total_products}")

def search_products():

# Funcion encargada para buscar productos por ID o nombre
    
    if not inventory:
        print("Empty storage")
        return
    search_term = input("Enter ID or name of product are you looking for: ")
    found = False
    for product in inventory:     
        if str(product["id"]) == search_term or search_term in product: 
            print("Product finded")
            print(f"ID{'id'} | Name {product['name']} | Price{product['price']}")



while True:
    print("\n===== ORDER MANAGEMENT SYSTEM =====")
    print("1. Add product")
    print("2. Show Inventary")
    print("3. Calculate estadistics")
    print("4. Exit")

    option = input("Choice your option: ")

    clear_screen()

    match option:
        case "1":
            create_product()
        case "2":    
            show_inventory()
        case "3":
            statistics()
        case "4":
            print("Exit ...")
            break 
        case _:
            print("Invalid Option, try again")

    # if option == "1":
    #     create_product()

    # elif option == "2":
    #     show_inventory()

    # elif option == "3":
    #     statistics()

    # elif option == "4":
    #     print("Saliendo...")
    #     break

    # else:
        # print("Opción inválida, intenta nuevamente")