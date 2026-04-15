class BikeRental:
    def __init__(self, stock):
        self.stock = stock

    def display_bikes(self):
        print(f"Available bikes: {self.stock}")

    def rent_bike(self, num):
        if num <= 0:
            print("Enter valid number of bikes")
        elif num > self.stock:
            print("Not enough bikes available")
        else:
            self.stock -= num
            print(f"You rented {num} bike(s)")

    def return_bike(self, num):
        if num <= 0:
            print("Invalid return")
        else:
            self.stock += num
            print(f"You returned {num} bike(s)")


# Object
shop = BikeRental(10)

while True:
    print("\n1. Display Bikes")
    print("2. Rent Bike")
    print("3. Return Bike")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        shop.display_bikes()
    elif choice == 2:
        n = int(input("How many bikes: "))
        shop.rent_bike(n)
    elif choice == 3:
        n = int(input("Return bikes: "))
        shop.return_bike(n)
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
