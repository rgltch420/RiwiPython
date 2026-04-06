from app import *
while True:
    
    ascii_art()
        
    print("1. Add product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Calculate estadistics")
    print("5. Show Inventary")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")

    option = input("Choice your option: ")

    clear_screen()

    match option:
        case "1":
            create_product()
        case "2":
            update_products()
        case "3":
            delete_products()  
        case "4":
            stadistics()
        case "5":    
            show_inventory()
        case "6":
            save_data()
        case "7":
            read_data()             
        case "8":
            print("Exit ...")
            break 
        case _:
            print("Invalid Option, try again")