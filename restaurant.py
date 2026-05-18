def restaurant():
    total_bill = 0

    while True:

        print("\n---Restaurant Menu---")
        print("1.Pizza=200")
        print("2.Burger=100")
        print("1.Pasta=150")
        print("4.Exit")

        choice = int(input("Enter your choice"))

        if choice == 1:
            qty = int(input("Enter Pizza quantity:"))
            total_bill+=200*qty

            print("Pizza Added")

        elif choice == 2:
            qty = int(input("Enter Burger quantity:"))
            total_bill+=100*qty

            print("Burger Added")

        elif choice == 3:
            qty = int(input("Enter Pasta quantity:"))
            total_bill+=150*qty

            print("Pasta Added")

        elif choice == 4:
            print("Total Bill=",total_bill)
            print("Thank you Visit Again")

            break

        else:

            print("Invalid choice")

restaurant()

        

