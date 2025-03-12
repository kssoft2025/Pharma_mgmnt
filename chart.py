import tkinter as tk
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Setup the root window
root = tk.Tk()
root.geometry("800x600")

# Create the customtkinter frame
main_body = ctk.CTkFrame(root, width=800, height=600)
main_body.pack(fill="both", expand=True)

# Create the mat_card7 inside the main_body
mat_card7 = ctk.CTkFrame(main_body, width=560, height=340, fg_color='white')
mat_card7.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

# Data for the pie chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [25, 35, 20, 20]

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(5, 3))  # Adjust the size to fit the frame

# Create the pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'orange', 'green', 'purple'])

# Equal aspect ratio ensures that pie chart is drawn as a circle.
ax.axis('equal')

# Add title to the pie chart
ax.set_title('Pie Chart Example')

# Embed the Matplotlib plot in the tkinter window
canvas = FigureCanvasTkAgg(fig, master=mat_card7)  # Pass the mat_card7 as the master widget
canvas.get_tk_widget().pack(fill="both", expand=True)

# Display the plot
canvas.draw()

# Start the tkinter main loop
root.mainloop()
