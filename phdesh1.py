import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Sample Medication Data
medications = [
    {"name": "Aspirin", "price": 5.99, "stock": 120},
    {"name": "Paracetamol", "price": 2.99, "stock": 200},
    {"name": "Ibuprofen", "price": 7.99, "stock": 85},
    {"name": "Antibiotic", "price": 15.99, "stock": 50},
    {"name": "Cough Syrup", "price": 4.99, "stock": 75}
]

class PharmacyDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pharmacy Dashboard")
        self.geometry("800x600")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Frame for Card Layout
        main_frame = tk.Frame(self)
        main_frame.pack(pady=20)

        # Create cards for total medication count, total stock, etc.
        self.create_card(main_frame, "Total Medications", len(medications), 0)
        self.create_card(main_frame, "Total Stock", self.get_total_stock(), 1)
        self.create_card(main_frame, "Total Value", self.get_total_value(), 2)

        # Create a frame for the chart below the cards
        chart_frame = tk.Frame(self)
        chart_frame.pack(pady=20)

        # Create and display the bar chart
        self.create_bar_chart(chart_frame)

    def create_card(self, parent, title, value, row):
        card_frame = tk.Frame(parent, width=200, height=100, bg="#f1f1f1", relief="solid", bd=2)
        card_frame.grid(row=row, column=0, padx=10, pady=10)

        # Title of the card
        title_label = tk.Label(card_frame, text=title, font=("Arial", 12), bg="#f1f1f1")
        title_label.pack(pady=5)

        # Value inside the card
        value_label = tk.Label(card_frame, text=str(value), font=("Arial", 16, "bold"), bg="#f1f1f1")
        value_label.pack(pady=5)

    def get_total_stock(self):
        return sum(med["stock"] for med in medications)

    def get_total_value(self):
        return sum(med["price"] * med["stock"] for med in medications)

    def create_bar_chart(self, parent):
        # Prepare the data for the chart
        names = [med["name"] for med in medications]
        stocks = [med["stock"] for med in medications]

        # Create a Matplotlib figure
        fig, ax = plt.subplots(figsize=(6, 4))

        ax.bar(names, stocks, color="skyblue")
        ax.set_title("Stock of Medications")
        ax.set_xlabel("Medication")
        ax.set_ylabel("Stock Quantity")

        # Embed the plot in Tkinter
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    app = PharmacyDashboard()
    app.mainloop()
