import tkinter as tk
from tkinter import messagebox

class PharmacyDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pharmacy Dashboard")
        self.geometry("600x400")
        
        # Sample data for medications (name, price, stock)
        self.medications = [
            {"name": "Aspirin", "price": 5.99, "stock": 120},
            {"name": "Paracetamol", "price": 2.99, "stock": 200},
            {"name": "Ibuprofen", "price": 7.99, "stock": 85}
        ]
        
        # Set up the GUI components
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self, text="Pharmacy Dashboard", font=("Arial", 24))
        title_label.pack(pady=10)

        # Summary Panel
        summary_frame = tk.Frame(self)
        summary_frame.pack(pady=10)

        total_medications_label = tk.Label(summary_frame, text=f"Total Medications: {len(self.medications)}", font=("Arial", 12))
        total_medications_label.grid(row=0, column=0, padx=10)

        total_stock_label = tk.Label(summary_frame, text=f"Total Stock: {self.get_total_stock()}", font=("Arial", 12))
        total_stock_label.grid(row=0, column=1, padx=10)

        # Medication List Table
        self.medication_list_frame = tk.Frame(self)
        self.medication_list_frame.pack(pady=20)

        self.create_medication_table()

        # Add Medication Button
        add_button = tk.Button(self, text="Add Medication", command=self.show_add_medication_form)
        add_button.pack(pady=10)

    def create_medication_table(self):
        """ Creates the medication list table """
        for widget in self.medication_list_frame.winfo_children():
            widget.destroy()
        
        # Header Row
        header = tk.Label(self.medication_list_frame, text="Name | Price | Stock", font=("Arial", 12, "bold"))
        header.grid(row=0, column=0, columnspan=3, pady=10)

        # List all medications
        for idx, med in enumerate(self.medications):
            row = tk.Frame(self.medication_list_frame)
            row.grid(row=idx+1, column=0, columnspan=3, pady=5)

            name_label = tk.Label(row, text=med["name"], width=20)
            name_label.grid(row=0, column=0)

            price_label = tk.Label(row, text=f"${med['price']:.2f}", width=10)
            price_label.grid(row=0, column=1)

            stock_label = tk.Label(row, text=med["stock"], width=10)
            stock_label.grid(row=0, column=2)

    def get_total_stock(self):
        """ Calculate total stock from all medications """
        return sum(med["stock"] for med in self.medications)

    def show_add_medication_form(self):
        """ Display the form to add a new medication """
        add_window = tk.Toplevel(self)
        add_window.title("Add Medication")

        name_label = tk.Label(add_window, text="Medication Name:")
        name_label.grid(row=0, column=0, padx=10, pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        price_label = tk.Label(add_window, text="Price:")
        price_label.grid(row=1, column=0, padx=10, pady=5)
        price_entry = tk.Entry(add_window)
        price_entry.grid(row=1, column=1, padx=10, pady=5)

        stock_label = tk.Label(add_window, text="Stock:")
        stock_label.grid(row=2, column=0, padx=10, pady=5)
        stock_entry = tk.Entry(add_window)
        stock_entry.grid(row=2, column=1, padx=10, pady=5)

        def add_medication():
            try:
                name = name_entry.get()
                price = float(price_entry.get())
                stock = int(stock_entry.get())
                
                if not name or price <= 0 or stock < 0:
                    messagebox.showerror("Invalid Input", "Please enter valid medication details.")
                    return
                
                # Add new medication to the list
                self.medications.append({"name": name, "price": price, "stock": stock})
                self.create_medication_table()
                add_window.destroy()
                
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid price and stock values.")

        add_button = tk.Button(add_window, text="Add Medication", command=add_medication)
        add_button.grid(row=3, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    app = PharmacyDashboard()
    app.mainloop()
