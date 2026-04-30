from datetime import date, datetime

events = {}

def add_event():
    event_name = input("Enter event name: ")
    date_input = input("Enter event date (YYYY-MM-DD): ")
    try:
        event_date = datetime.strptime(date_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return
    events[event_name] = event_date
    print(f'Success! "{event_name}" added successfully!')

def get_event_date(tup):
    return tup[1]

def list_events():
    if len(events) == 0:
        print("No events found.")
        return
    print('\nUpcoming Events!')

    sorted_events = sorted(events.items(), key=get_event_date)
    today = date.today()
    for e_name, e_date in sorted_events:
        days_remaining = (e_date - today).days
        print(f"{e_name} - {e_date} ({days_remaining} days remaining)")

def delete_event():
    event_to_delete = input("Enter the name of the event to delete: ")
    if event_to_delete in events:
        del events[event_to_delete]
        print(f'Success! "{event_to_delete}" deleted successfully!')
    else:
        print(f'Event "{event_to_delete}" not found.')

def main():
    while True:
        print("\nEvent Management System")
        print("1. Add Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_event()
        elif choice == '2':
            list_events()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
