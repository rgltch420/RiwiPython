import os


inventory = []

def create_product():
    try:
        id_product = int(input("Enter the id of product: "))
        name_product = input("Enter the name of product: ")
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
            print(f"Producto ID {id_product} agregado correctamente")

        else:
            print("Ingresa valores correctos (mayores a 0)")

    except ValueError:
        print("Ingresa el valor solicitado correctamente")

def show_inventory():
    if len(inventory) == 0:
        print("El inventario está vacío")
    else:
        print("\n--- INVENTORY ---")
        for product in inventory:
            print(f"Producto: {product['name']} | Precio: {product['price']} | Cantidad: {product['quantity']}")



def total_value():
    total = 0

    for product in inventory:
        total += product["price"] * product["quantity"]

    return total

def statistics():
    if len(inventory) == 0:
        print("No hay productos registrados")
        return

    total_products = 0

    for product in inventory:
        total_products += product["quantity"]

    print("\n--- ESTADÍSTICAS ---")
    print(f"Valor total del inventario: {total_value()}")
    print(f"Cantidad total de productos: {total_products}")



while True:
    print("\n===== ORDER MANAGEMENT SYSTEM =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    option = input("Seleccione una opción: ")

    os.system("clear")

    if option == "1":
        create_product()

    elif option == "2":
        show_inventory()

    elif option == "3":
        statistics()

    elif option == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida, intenta nuevamente")