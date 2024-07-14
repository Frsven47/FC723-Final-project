import random

# Initialising the Burak 757 seating plan
seats = [['F' for _ in range(80)] for _ in range(6)]
for row in seats:
    row[38] = 'X'  # corridor
    row[39] = 'X'  # corridor
for i in range(76, 80):
    seats[3][i] = 'S'  # storage area
    seats[4][i] = 'S'  # storage area
    seats[5][i] = 'S'  # storage area

def display_seats():
    for row in seats:
        print(' '.join(row))

def check_availability(seat):
    row, col = seat_to_index(seat)
    return seats[row][col] == 'F'

def book_seat(seat):
    if check_availability(seat):
        row, col = seat_to_index(seat)
        seats[row][col] = 'R'
        return True
    return False

def free_seat(seat):
    row, col = seat_to_index(seat)
    if seats[row][col] == 'R':
        seats[row][col] = 'F'
        return True
    return False

def seat_to_index(seat):
    rows = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
    return rows[seat[-1]], int(seat[:-1]) - 1

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
            if book_seat(seat):
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


# operating menu
menu()
