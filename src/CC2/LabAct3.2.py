name = input("Enter your name: ")
age = int(input("Enter your age: "))
show_price = {
    "daytime": {
        "children": 50,
        "adults": 100,
        "seniors": 80,
    },
    "evening": {
        "children": 70,
        "adults": 120,
        "seniors": 100,
    }
}   

match input("Enter show time: ").lower():
    case "daytime":
        price = show_price["daytime"]

        if age < 0:
            print("Error! Entered age is negative.")
        elif age <= 4:
            print(f"Ticket price: Free")
        elif age <= 17:
            print(f"Ticket price: PHP{price['children']}")
        elif age <= 64:
            print(f"Ticket price: PHP{price['adults']}")
        else:
            print(f"Ticket price: PHP{price['seniors']}")
    case "evening":
        price = show_price["evening"]

        if age < 0:
            print("Error! Entered age is negative.")
        elif age <= 4:
            print(f"Ticket price: Free")
        elif age <= 17:
            print(f"Ticket price: PHP{price['children']}")
        elif age <= 64:
            print(f"Ticket price: PHP{price['adults']}")
        else:
            print(f"Ticket price: PHP{price['seniors']}")

