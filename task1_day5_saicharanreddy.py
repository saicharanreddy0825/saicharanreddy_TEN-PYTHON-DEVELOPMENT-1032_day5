# SMART INVENTORY MANAGEMENT SYSTEM

inventory = {}
categories = set()


while True:

    print("\n===== SMART INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Update Inventory")
    print("3. Search Product")
    print("4. Display Inventory")
    print("5. Low Stock Alert")
    print("6. Out of Stock Alert")
    print("7. Category Management")
    print("8. Inventory Report")
    print("9. Delete Product")
    print("10. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":

        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        supplier = input("Enter Supplier: ")

        inventory[product_id] = {
            "name": name,
            "category": category,
            "qty": qty,
            "price": price,
            "supplier": supplier
        }

        categories.add(category)

        print("Product Added Successfully!")
    elif choice == "2":

        product_id = input("Enter Product ID: ")

        if product_id in inventory:

            new_qty = int(input("Enter New Quantity: "))
            new_price = float(input("Enter New Price: "))

            inventory[product_id]["qty"] = new_qty
            inventory[product_id]["price"] = new_price

            print("Inventory Updated Successfully!")

        else:
            print("Product Not Found!")
    elif choice == "3":

        keyword = input("Enter Product ID or Name: ").lower()

        results = []

        for pid, details in inventory.items():

            if keyword == pid.lower() or keyword == details["name"].lower():
                results.append((pid, details))

        if len(results) > 0:

            print("\nSearch Results")

            for item in results:
                print(item)

        else:
            print("No Product Found!")
    elif choice == "4":

        if len(inventory) == 0:
            print("Inventory Empty!")

        else:

            print("\nID\tName\tCategory\tQty\tPrice\tSupplier")

            for pid, details in inventory.items():

                print(
                    pid,
                    details["name"],
                    details["category"],
                    details["qty"],
                    details["price"],
                    details["supplier"],
                    sep="\t"
                )
    elif choice == "5":

        threshold = 10

        print("\nLow Stock Products")

        found = False

        for pid, details in inventory.items():

            if details["qty"] < threshold:

                print(pid, "-", details["name"],
                      "- Quantity:", details["qty"])

                found = True

        if not found:
            print("No Low Stock Products!")
    elif choice == "6":

        found = False

        print("\nOut of Stock Products")

        for pid, details in inventory.items():

            if details["qty"] == 0:

                print(pid, "-", details["name"])

                found = True

        if not found:
            print("No Out of Stock Products!")
    elif choice == "7":

        print("\nAvailable Categories:")

        for category in categories:
            print(category)
    elif choice == "8":

        total_items = 0
        total_value = 0

        category_summary = {}

        for pid, details in inventory.items():

            total_items += details["qty"]

            total_value += details["qty"] * details["price"]

            cat = details["category"]

            if cat in category_summary:
                category_summary[cat] += details["qty"]
            else:
                category_summary[cat] = details["qty"]

        report = (total_items, total_value)

        print("\n===== INVENTORY REPORT =====")

        print("Total Items:", report[0])
        print("Total Inventory Value:", report[1])

        print("\nCategory Wise Summary")

        for cat, qty in category_summary.items():
            print(cat, ":", qty)
    elif choice == "9":

        product_id = input("Enter Product ID to Delete: ")

        if product_id in inventory:

            del inventory[product_id]

            print("Product Deleted Successfully!")

        else:
            print("Product Not Found!")
    elif choice == "10":

        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
