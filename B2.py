import random
import string

# Initialising the Burak 757 seating plan
seats = [['F' for _ in range(80)] for _ in range(6)]
for row in seats:
    row[38] = 'X'  # corridor
    row[39] = 'X'  # corridor
for i in range(76, 80):
    seats[3][i] = 'S'  # storage area
    seats[4][i] = 'S'  # storage area
    seats[5][i] = 'S'  # storage area

booking_references = set()
customers = {}

def generate_booking_reference():
    while True:
        ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if ref not in booking_references:
            booking_references.add(ref)
            return ref

def display_seats():
    for row in seats:
        print(' '.join(row))

def seat_to_index(seat):
    # Assuming seat is in the format "1A", "20C", etc.
    row = int(seat[:-1]) - 1  # Seat number part, converted to index (0-based)
    column = ord(seat[-1].upper()) - ord('A')  # Seat letter part, converted to index (0-based)
    return row, column

def check_availability(seat):
    row, col = seat_to_index(seat)
    return seats[row][col] == 'F'

def book_seat(seat, customer_details):
    if check_availability(seat):
        row, col = seat_to_index(seat)
        ref = generate_booking_reference()
        seats[row][col] = ref
        customers[ref] = customer_details
        return True
    return False

def free_seat(seat):
    row, col = seat_to_index(seat)
    ref = seats[row][col]
    if ref in booking_references:
        seats[row][col] = 'F'
        del customers[ref]
        booking_references.remove(ref)
        return True
    return False

def menu():
    while True:
        print("\nMenu:")
        print("1. Check seat availability")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Display seat status")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            seat = input("Enter seat number (e.g., 1A): ")
            if check_availability(seat):
                print(f"Seat {seat} is available.")
            else:
                print(f"Seat {seat} is not available.")
        elif choice == '2':
            seat = input("Enter seat number (e.g., 1A): ")
            customer_details = input("Enter customer details: ")
            if book_seat(seat, customer_details):
                print(f"Seat {seat} has been booked.")
            else:
                print(f"Seat {seat} cannot be booked.")
        elif choice == '3':
            seat = input("Enter seat number (e.g., 1A): ")
            if free_seat(seat):
                print(f"Seat {seat} has been freed.")
            else:
                print(f"Seat {seat} cannot be freed.")
        elif choice == '4':
            display_seats()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

# Run the menu
menu()
