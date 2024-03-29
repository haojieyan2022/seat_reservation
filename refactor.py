import random
import string

class SeatReservation:
    def __init__(self, rows, cols):
        # Initialize SeatReservation object with specified rows and columns
        self.rows = rows
        self.cols = cols
        # Create a 2D list to represent seats, initially all seats are free ('F')
        self.seats = [[{'status': 'F', 'reference': None, 'customer_data': None} for _ in range(cols)] for _ in range(rows)]

    def generate_reference(self):
        """Generate a random booking reference with 8 alphanumeric characters."""
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return reference

    def is_reference_unique(self, reference):
        """Check if the generated reference is unique."""
        for row in self.seats:
            for seat in row:
                if seat['reference'] == reference:
                    return False
        return True

    def get_unique_reference(self):
        """Generate a unique reference."""
        while True:
            reference = self.generate_reference()
            if self.is_reference_unique(reference):
                return reference

    def display_seats(self):
        """Display the current availability of seats in the reservation system."""
        print("Current seat availability:")
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.seats[row][col]['status'], end=" ")
            print()

    def check_seat_availability(self, row, col):
        """Check if the given seat at row and col exists."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            print("Seat does not exist.")
            return
        if self.seats[row][col]['status'] == 'F':
            print("Seat is available.")
        else:
            print("Seat is already booked.")

    def book_seat(self, row, col, customer_data):
        """Book a seat at the given row and column if it's available."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            print("Seat does not exist.")
            return
        if self.seats[row][col]['status'] == 'F':
            reference = self.get_unique_reference()
            self.seats[row][col]['status'] = 'R'
            self.seats[row][col]['reference'] = reference
            self.seats[row][col]['customer_data'] = customer_data
            print("Seat booked successfully. Reference:", reference)
        else:
            print("Sorry, the seat is already booked.")

    def vacate_seat(self, row, col):
        """Vacate a previously booked seat at the given row and column."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            print("Seat does not exist.")
            return
        if self.seats[row][col]['status'] == 'R':
            self.seats[row][col]['status'] = 'F'
            self.seats[row][col]['reference'] = None
            self.seats[row][col]['customer_data'] = None
            print("Seat vacated successfully.")
        else:
            print("No reservation found for this seat.")

    def display_reservation_status(self):
        """Display the current reservation status of all seats."""
        print("Current reservation status:")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[row][col]['status'] == 'R':
                    print(f"Seat at row {row+1}, col {col+1} is reserved. Reference: {self.seats[row][col]['reference']}, Customer Data: {self.seats[row][col]['customer_data']}")
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
            name = input("Enter customer's name: ")
            passport = input("Enter customer's passport number: ")
            customer_data = {'name': name, 'passport': passport}
            reservation_system.book_seat(row, col, customer_data)

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
