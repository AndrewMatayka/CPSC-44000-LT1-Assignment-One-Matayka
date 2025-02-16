# Title: Assignment 1
# File_Name: assignment_one.py
# External_Files_Needed: N/A
# External_Files_Created: N/A
# Programmer_Names: Andrew Matayka & Aaron Matayka
# Email_Addresses: andrewjmatayka@lewisu.edu & aaronjmatayka@lewisu.edu
# Class_Information: CPSC 44000-LT1
# Submission_Date: 02/16/2025
# Explanation:
# Resources Used: https://phoenixnap.com/kb/python-power
# Resources Used: https://www.w3schools.com/python/gloss_python_specify_variable_type.asp
import math

# Function to take in the user's requested power value (n) and upper limit value (k) to use for the rest of the code.
def receive_input():
    while True:
        # Validates the input to ensure the correct range of data is entered
        try:
            # n is the power value the user enters
            n = int(input("Please enter the power n value (between 3 and 11): "))  # This is the power value for our equation

            if 2 >= n or n >= 12:
                print("n must be between 3 and 11. Try again.")
                continue

            # k is the upper limit value that the user enters
            k = int(input("Please enter the upper limit k value: "))  # This is the upper limit for our x and y variables
            if k <= 10:
                print("k must be greater than 10. Try again.")
                continue

            # Return the inputted values
            return n, k
        except ValueError:
            # Print out Error Code to user and restart input
            print("Invalid input. Please enter a valid integer.")

# Function to take the inputed power values and upper limit values and perform fermats iteration test using them. Returns statements to the user about near misses and which near miss was closest
def fermat_iteration(n, k):
    # Set MIN relative miss to infinity, used for tracking later on
    smallest_relative_miss = float('inf')

    # No current best anything, use these to know what was best
    best_x, best_y, best_z = None, None, None
    best_miss = None

    # For x and y in our upper range limit
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            # Get the sum of the x and y raised to power
            sum_powers = x ** n + y ** n
            # Find closest integer z
            z = int(math.pow(sum_powers, 1 / n))

            # Get z raised to n
            z_power = z ** n
            # Get z plus one raised to n
            z_plus_power = (z + 1) ** n

            # Find our absolute miss values for each z variable
            miss1 = abs(sum_powers - z_power)
            miss2 = abs(z_plus_power - sum_powers)

            # Which miss is the minimum, then get it relative to our value to make it comparable
            miss = min(miss1, miss2)
            relative_miss = miss / sum_powers

            # Is the new relative miss lowest than our best? If so commit to the variables named and record it
            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_x, best_y, best_z = x, y, z if miss1 < miss2 else z + 1
                best_miss = miss

                # Tell the user the found results and print to the screen. Wait for user input to validate user has seen
                print(f"New smallest near miss found:")
                print(f"x = {best_x}, y = {best_y}, z = {best_z}, n = {n}")
                print(f"Absolute miss: {best_miss}, Relative miss: {smallest_relative_miss:.6f}\n")
                input("Press Enter to continue...")

    # Tell the user the final results and print to the screen. Wait for user input to validate user has seen
    print("\nFinal smallest near miss:")
    print(f"x = {best_x}, y = {best_y}, z = {best_z}, n = {n}")
    print(f"Absolute miss: {best_miss}, Relative miss: {smallest_relative_miss:.6f}")
    input("Press Enter to continue...")


# Main Function for running code
if __name__ == '__main__':
    power, limit = receive_input()
    print()
    fermat_iteration(power, limit)