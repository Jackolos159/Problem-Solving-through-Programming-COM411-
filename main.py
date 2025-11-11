# --------------------------------------------------------------
# File: week8/plots.py
# Author: Jack Foreshew
# Description:
#   Week 8 – Data Visualisation Tasks
#   This script demonstrates creating line plots using matplotlib.
# --------------------------------------------------------------

import matplotlib.pyplot as plt
import random


# --------------------------------------------------------------
# TASK 1: Basic Line Graph
# --------------------------------------------------------------
def display_line(x_values, y_values):
    """Displays a basic line plot using the supplied x and y values."""
    plt.plot(x_values, y_values)
    plt.title("Basic Line Plot")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.grid(True)
    plt.show()


def run_task1():
    """Creates x and y lists and displays a simple line plot."""
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display_line(x_values, y_values)


# --------------------------------------------------------------
# TASK 2: Customised Line Graphs (Squares)
# --------------------------------------------------------------
def small():
    """Displays a small red dotted square with circle markers."""
    x = [1, 1, 2, 2, 1]
    y = [1, 2, 2, 1, 1]
    plt.plot(x, y, 'r:o', label="Small Square")


def medium():
    """Displays a medium green dashed square around the small square."""
    x = [0, 0, 3, 3, 0]
    y = [0, 3, 3, 0, 0]
    plt.plot(x, y, 'g--s', label="Medium Square")


def large():
    """Displays a large blue solid square around the medium square."""
    x = [-1, -1, 4, 4, -1]
    y = [-1, 4, 4, -1, -1]
    plt.plot(x, y, 'b-p', label="Large Square")
    plt.title("Customised Line Graphs")
    plt.legend()
    plt.axis("equal")
    plt.show()


def run_task2():
    """Displays all three squares."""
    small()
    medium()
    large()


# --------------------------------------------------------------
# TASK 3: Path with Line Plots
# --------------------------------------------------------------
def coordinate():
    """Prompts user for x and y coordinates and returns a tuple (x, y)."""
    x = float(input("Enter x value: "))
    y = float(input("Enter y value: "))
    return (x, y)


def path():
    """Retrieves 4 sets of coordinates from the user."""
    print("Retrieving path...")
    x_values = []
    y_values = []
    for i in range(4):
        print(f"--- Coordinate {i+1} ---")
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values, y_values]


def run_task3():
    """Draws a line plot based on user-input coordinates."""
    values = path()
    plt.plot(values[0], values[1], 'r--o')
    plt.title("User Path Line Plot")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.grid(True)
    plt.show()


# --------------------------------------------------------------
# TASK 4: Data Dictionary and Plots
# --------------------------------------------------------------
def data():
    """Collects user preferences for line style, color, and marker."""
    paths = {}
    paths['line'] = input("Enter line style (:, --, -): ")
    paths['color'] = input("Enter color (r, g, b): ")
    paths['marker'] = input("Enter marker (o, s, ^): ")
    return paths


def generate():
    """Generates multiple line plots based on user input and random data."""
    num = int(input("How many lines would you like to display? "))

    for i in range(num):
        values = data()
        x_values = random.sample(range(1, 11), 5)
        y_values = random.sample(range(1, 11), 5)
        style = values['color'] + values['line'] + values['marker']
        plt.plot(x_values, y_values, style, label=f"Line {i+1}")

    plt.title("User Customised Line Plots")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.legend()
    plt.grid(True)
    plt.show()


def run_task4():
    """Runs the data dictionary-based plot generator."""
    print("Running....")
    generate()
    print("Done!")


# --------------------------------------------------------------
# MAIN MENU (LOOPING)
# --------------------------------------------------------------
def main_menu():
    """Displays the main menu and loops until the user quits."""
    while True:
        print("\n=== Week 8 – Data Visualisation ===")
        print("1. Task 1 – Basic Line Graph")
        print("2. Task 2 – Customised Squares")
        print("3. Task 3 – User Path Plot")
        print("4. Task 4 – Data Dictionary and Plots")
        print("Q. Quit")

        choice = input("Enter the task number (1–4) or Q to quit: ").strip().lower()

        if choice == "1":
            run_task1()
        elif choice == "2":
            run_task2()
        elif choice == "3":
            run_task3()
        elif choice == "4":
            run_task4()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# --------------------------------------------------------------
# Run program
# --------------------------------------------------------------
if __name__ == "__main__":
    main_menu()
