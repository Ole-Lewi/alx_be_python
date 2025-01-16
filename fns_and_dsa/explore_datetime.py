from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time in "YYYY-MM-DD HH:MM:SS" format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Ask the user for the number of days to add
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=number_of_days)
    
    # Print the future date in "YYYY-MM-DD" format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Main function to call the above functions
def main():
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date()

if __name__ == "__main__":
    main()
