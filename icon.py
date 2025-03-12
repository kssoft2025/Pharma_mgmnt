import customtkinter as ctk

# Create the main window
window = ctk.CTk()

# Create the header frame with custom background color
header = ctk.CTkFrame(window, bg_color='blue', width=1220, height=100)
header.place(x=300, y=0)  # Correct placement of the frame

# Run the window
window.mainloop()