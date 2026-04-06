from app import *
while True:
    
    # ascii_art()
        
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