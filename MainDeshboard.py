from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class MainDeshbord:
    
    def __init__(self, window):
        self.window = window
        screen_width = 1240
        screen_height = 740
        #self.window.geometry(f'{screen_width}x{screen_height}')
        #self.window.resizable(True, True)
        #self.window.config(background='#eff5f6')
        
        # Create a scrollable frame
        self.main_body = customtkinter.CTkScrollableFrame(self.window, orientation='vertical', width=1240, height=740) 
        self.main_body.grid(row=0, column=0, sticky="nsew")
        
        # Configure grid rows and columns to expand
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1,minsize=200)
        
        self.main_body.grid_rowconfigure(0, weight=1)
        self.main_body.grid_columnconfigure(0, weight=1,minsize=200)
        
        # Define the frames (cards)
        
        self.mat_card1 = self.create_card(self.main_body, 'image/customer.png', 'Total Customers', 0, 0)
        self.mat_card2 = self.create_card(self.main_body, 'image/team.png', 'Total Suppliers', 0, 1)
        self.mat_card3 = self.create_card(self.main_body, 'image/sales.png', "Today's Sales", 0, 2)
        self.mat_card4 = self.create_card(self.main_body, 'image/spending.png', "Today's Expense", 1, 0)
        self.mat_card5 = self.create_card(self.main_body, 'image/outofstock.png', 'Out Of Stocked', 1, 1)
        self.mat_card6 = self.create_card(self.main_body, 'image/expired.png', 'Expire Date', 1, 2)
        
        # Special larger card (mat_card7) that spans two columns
        self.mat_card7 = customtkinter.CTkFrame(self.main_body, width=560, height=340, fg_color='white')
        self.mat_card7.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
        Month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY']
        categories = ['A', 'B', 'C', 'D', 'E']
        values= [10, 20, 15, 30, 25]
        values2 = [12, 18, 17, 25, 22]
        bar_width = 0.35
        fig, ax = plt.subplots(figsize=(5, 3))  # Adjust the size to fit the frame
        index = np.arange(len(Month))
        ax.bar(index - bar_width / 2, values, bar_width, label='Sales', color='blue')
        ax.bar(index + bar_width / 2, values2, bar_width, label='Expence', color='orange')

        ax.set_title('Monthly Progress')
        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')
        ax.set_xticks(index)
        ax.set_xticklabels(Month)

# Add a legend to the plot
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.mat_card7)  # Pass the mat_card7 as the master widget
        canvas.get_tk_widget().pack(fill="both", expand=True)
        canvas.draw()
        
        self.mat_card8 = customtkinter.CTkFrame(self.main_body, width=360, height=340, fg_color='white')
        self.mat_card8.grid(row=2, column=2,  padx=20, pady=20, sticky="nsew")
        labels = ['Purchase', 'Sales', 'Expences', 'Revenue']
        sizes = [25, 35, 20, 20]

        fig, ax = plt.subplots(figsize=(3, 2))  # Adjust the size to fit the frame
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=80, colors=['skyblue', 'orange', 'green', 'purple'])
        ax.axis('equal')
        ax.set_title('Pie Chart')
        canvas = FigureCanvasTkAgg(fig, master=self.mat_card8)  # Pass the mat_card7 as the master widget
        canvas.get_tk_widget().pack(fill="both", expand=True)
        canvas.draw()


        self.mat_card9 = customtkinter.CTkFrame(self.main_body, width=480, height=340 )
        self.mat_card9.grid(row=3, column=0,columnspan = 3, padx=20, pady=20, sticky="nsew")

        self.mat_card91 = customtkinter.CTkFrame(self.mat_card9, width=580, height=340,fg_color='white' )
        self.mat_card91.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.mat_card92 = customtkinter.CTkFrame(self.mat_card9, width=560, height=340,fg_color='white' )
        self.mat_card92.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.mat_card10 = customtkinter.CTkFrame(self.main_body, width=480, height=340 ,fg_color='white')
        self.mat_card10.grid(row=4, column=0,columnspan = 3, padx=20, pady=20, sticky="nsew")


    def create_card(self, parent, icon_path, label, row, column):
        mat_card = customtkinter.CTkFrame(parent, width=360, height=240, fg_color='white')
        mat_card.grid(row=row, column=column,columnspan=1,padx=20, pady=20, sticky="nsew")

        # Load icon and resize it
        icon = Image.open(icon_path)
        icon = icon.resize((125, 125), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(icon)
        
        icon_label = Label(mat_card, image=photo, bg='white')
        icon_label.image = photo
        icon_label.place(x=30, y=60)

        # Labels for the card
        label1 = Label(mat_card, text=label, bg='#ffffff', font=('yu gothic ui', 20, 'bold'))
        label1.place(x=50, y=15)

        label2 = Label(mat_card, text='view', bg='#ffffff', font=('yu gothic ui', 15, 'bold'),
                       bd=0, activebackground='#ffffff', cursor='hand2', fg='blue')
        label2.place(x=280, y=190)

        return mat_card
def on_closing():
    # Handle the cleanup process or just destroy the root window
    Tk().destroy()

#def main():
 #   window = Tk()
 #   MainDeshbord(window)
 #   window.mainloop()

#if __name__ == '__main__':
#    main()
