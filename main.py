import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# python3 -m pip install -U matplotlib
# club_name[0],player_name[1],age[2],position[3],club_involved_name[4],fee[5],transfer_movement[6],transfer_period[7],fee_cleaned[8],league_name[9],year[10],season[11],country[12]
canvas = None
# Define a function to create and display the plot
def create_plot(player_name):
    global canvas

    year = []
    teams = []
    from_team = []

    with open('serie-a.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
    for player_name in rows:
        if player_name_input in player_name[1]:
            year.append(int(player_name[10]))
            teams.append(player_name[4])
            from_team.append(player_name[0])

    # Create x and y data
    team_dict = {team: i for i, team in enumerate(set(teams))}
    x = [team_dict[team] for team in teams]

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.set_facecolor('lightgrey')
    plt.xticks(range(len(team_dict)), team_dict.keys())
    plt.yticks(year)
    plt.plot(x, year, 'o', markerfacecolor='orange', color='lightgreen')

    # Add title and axis labels
    plt.title(player_name_input, loc='center')
    plt.xlabel('Teams')
    plt.ylabel('Year')

    # Create a FigureCanvasTkAgg object and embed it in the window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack()

    # Update message label after plot is created
    message = player_name_input + " moved from " + from_team[0] + " to " + teams[-1] + " for a fee of " + rows[-1][5]
    label.config(text=message)

    # Update message label after plot is created
    message = player_name_input + " moved from " + from_team[0] + " to " + teams[-1] + " for a fee of " + rows[-1][5]
    label.config(text=message)
    label.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

# Define a function to handle the user input
def submit():
    global player_name_input, canvas
    player_name_input = entry.get()
    if canvas is not None:
        canvas.get_tk_widget().destroy()
    create_plot(player_name_input)

# Create the Tkinter window
window = tk.Tk()
window.title("Foorball is played by open minded people")
window.geometry('1000x800')
window.configure(bg='#F9F6EE')
window.configure(borderwidth=10, relief="sunken")

# Define font
my_font = ("Monospaced", 18, "bold")

# Add a label and an entry box for user input
label = tk.Label(window, text="Enter player name:", font=my_font)
label.configure(bg='#F9F6EE')
label.config(fg="red")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a new style
style = ttk.Style()
style.configure('my.TButton', background='lightgreen')
style.configure('my.TButton', font=('Arial', 12, 'bold'))

# Add a submit button that calls the submit function
button = ttk.Button(window, text="Go to player transfer details", command=submit, style='my.TButton')
button.pack()

# Add a label for the message
message_label = tk.Label(window, text="", font=my_font)
message_label.configure(bg='#F9F6EE')
message_label.pack()

# Start the main event loop
window.mainloop()


