class SeatReservation:
    def __init__(self, rows, cols):
        # Initialize SeatReservation object with specified rows and columns
        self.rows = rows
        self.cols = cols
        # Create a 2D list to represent seats, initially all seats are free ('F')
        self.seats = [['F' for _ in range(cols)] for _ in range(rows)]

    def display_seats(self):
        # Display the current availability of seats in the reservation system
        print("Current seat availability:")
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.seats[row][col], end=" ")
            print()

    def check_seat_availability(self, row, col):
        # Check if the given seat at row and col exists
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            print("Seat does not exist.")
            return
        # Check availability of a specific seat at given row and column
        if self.seats[row][col] == 'F':
            print("Seat is available.")
        else:
            print("Seat is already booked.")

    def book_seat(self, row, col):
        # Check if the given seat at row and col exists
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            print("Seat does not exist.")
            return
        # Book a seat at given row and column if it's available
        if self.seats[row][col] == 'F':
            self.seats[row][col] = 'R'
            print("Seat booked successfully.")
        else:
            print("Sorry, the seat is already booked.")

    def vacate_seat(self, row, col):
        # Check if the given seat at row and col exists
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            print("Seat does not exist.")
            return
        # Vacate a previously booked seat at given row and column
        if self.seats[row][col] == 'R':
            self.seats[row][col] = 'F'
            print("Seat vacated successfully.")
        else:
            print("No reservation found for this seat.")

    def display_reservation_status(self):
        # Display the current reservation status of all seats
        print("Current reservation status:")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[row][col] == 'R':
                    print(f"Seat at row {row+1}, col {col+1} is reserved.")
        print("End of reservation status.")

# Main program
if __name__ == "__main__":
    rows = 6  # Assume there are 6 rows
    cols = 10  # Assume there are 10 seats per row
    reservation_system = SeatReservation(rows, cols)

    while True:
        print("\nMenu:")
        print("1. Check seat availability")
        print("2. Book a seat")
        print("3. Vacate a seat")
        print("4. Display reservation status")
        print("5. Exit the program")

        choice = input("Please enter your choice: ")

        if choice == '1':
            row = int(input("Please enter the row number of the seat (starting from 1): ")) - 1
            col = int(input("Please enter the column number of the seat (starting from 1): ")) - 1
            reservation_system.check_seat_availability(row, col)

        elif choice == '2':
            row = int(input("Please enter the row number of the seat to book (starting from 1): ")) - 1
            col = int(input("Please enter the column number of the seat to book (starting from 1): ")) - 1
            reservation_system.book_seat(row, col)

        elif choice == '3':
            row = int(input("Please enter the row number of the seat to vacate (starting from 1): ")) - 1
            col = int(input("Please enter the column number of the seat to vacate (starting from 1): ")) - 1
            reservation_system.vacate_seat(row, col)

        elif choice == '4':
            reservation_system.display_reservation_status()

        elif choice == '5':
            print("The program has exited.")
            break

        else:
            print("Invalid option, please try again.")
