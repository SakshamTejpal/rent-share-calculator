from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import csv
import os

print(os.listdir())
file_dict = {}

def readCSV():    
    # Open and read CSV file
    file_name = "Values.csv" 

    with open(Path.cwd().parent/file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        # Skip header 
        header = next(reader)
        print("Header:", header)

        i = 0

        for row in reader: 
            for value in row:  # Iterate through each value 
                file_dict[header[i]] = float(value)
                i+=1
                print(value)

    # For debugging
    print(file_dict)

readCSV()

# Function to calculate the share
def calculate_share(event=None):
    people = 2
    try:
        utilities = float(utilities_entry.get())
        rent = file_dict["rent"]
        internet = file_dict["internet"]
        Room1 = file_dict["room1"]
        Room2 = file_dict["room2"]
        share = ((rent + internet + utilities - (Room1 + Room2)) / people)
        result_label.config(text=f"Each roommates's share: {share:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for utilities.")

# Create the main window
root = tk.Tk()
root.title("Share Calculator")

# Create and place the widgets
tk.Label(root, text="Enter the amount for utilities:").grid(row=0, column=0, padx=10, pady=10)
utilities_entry = tk.Entry(root)
utilities_entry.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate_share)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Bind the Enter key to the calculate_share function
utilities_entry.bind("<Return>", calculate_share)

# Run the application
root.mainloop()
