from tkinter import *
from PIL import ImageTk,Image
from datetime import *
from tkinter import messagebox
import time
import MainDeshboard
import customtkinter
class Deshboard:

    def __init__(self, window):
         self.window = window
         self.window.title('Pharmacy Management System')
         screen_width = self.window.winfo_screenwidth()
         screen_height = self.window.winfo_screenheight()
         self.window.geometry(f'{screen_width}x{screen_height}')
         self.window.resizable(0, 0)
         self.window.config(background='#eff5f6')
         self.header = customtkinter.CTkFrame(self.window,fg_color='#009df4',width=1220,height=100)
         self.header.place(x=300,y=0)
         self.main_body = Frame(self.window,bg='linen' ) 
         MainDeshboard.MainDeshbord(self.main_body)
         self.main_body.place(x=300,y=110,width=1220,height=640)
         self.user_name_icon_img= Image.open('image/icon_user.png')
         new_width = 50
         new_height = 55  
         self.user_name_icon_img = self.user_name_icon_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.user_name_icon_img)
         self.user_name_icon_img_lbl = Label(self.header,image=photo,bg='#009df4',cursor="hand2")
         self.user_name_icon_img_lbl.image =photo
         self.user_name_icon_img_lbl.place(x =1140,y=5)

         self.user_name_icon_img_lbl.bind("<Button-1>", self.toggle_profile_options)
         self.profile_options_frame = Frame(self.window, bg="white", bd=1, relief="ridge")
         self.profile_options_frame.place(x=1340, y=100, width=150, height=100)
         self.profile_options_frame.place_forget() 


         self.user_Prof_icon_img= Image.open('image/user_prf.png')
         new_width = 35
         new_height = 35  
         self.user_Prof_icon_img = self.user_Prof_icon_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.user_Prof_icon_img)
         self.user_name_icon_img_lbl = Label(self.profile_options_frame,image=photo,bg='white',cursor="hand2")
         self.user_name_icon_img_lbl.image =photo
         self.user_name_icon_img_lbl.place(x =10,y=5)
         self.user_name_icon_img_lbl.bind("<Button-1>", self.toggle_profile_options)

         self.user_prf_name_lbl =  Label(self.profile_options_frame,text='View Profile',bg='white',fg='black',font=('yu gothic ui',13,'bold'),cursor="hand2")
         self.user_prf_name_lbl.place(x=52, y=8)
         self.user_prf_name_lbl.bind("<Button-1>", self.view_profile)

         self.user_logout_icon_img= Image.open('image/logout.png')
         new_width = 35
         new_height = 35  
         self.user_logout_icon_img = self.user_logout_icon_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.user_logout_icon_img)
         self.logout_icon_img_lbl = Label(self.profile_options_frame,image=photo,bg='white',cursor="hand2")
         self.logout_icon_img_lbl.image =photo
         self.logout_icon_img_lbl.place(x =10,y=55)

         self.user_logout_lbl =  Label(self.profile_options_frame,text='logout',bg='white',fg='black',font=('yu gothic ui',13,'bold'),cursor="hand2")
         self.user_logout_lbl.place(x=52, y=58)
         self.user_logout_lbl.bind("<Button-1>", self.logout)

         self.clock_icon_img= Image.open('image/clock.png')
         new_width = 25
         new_height = 25  
         self.clock_icon_img = self.clock_icon_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.clock_icon_img)
         self.clock_icon_img_lbl = Label(self.header,image=photo,bg='#009df4',cursor="hand2")
         self.clock_icon_img_lbl.image =photo
         self.clock_icon_img_lbl.place(x =980,y=65)
         
         self.date_time = Label(self.header)
         self.date_time.place(x=1020,y=65)
         self.show_time()
        


         self.side_bar = customtkinter.CTkFrame(self.window,fg_color='#ffffff',width=300,height=750)
         self.side_bar.place(x=0,y=0)

         self.sign_in_img = Image.open('image/user.png')
         new_width = 130
         new_height = 130 
         self.sign_in_img = self.sign_in_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.sign_in_img)
         self.sign_in_img_lbl = Label(self.side_bar,image=photo,bg='white')
         self.sign_in_img_lbl.image =photo
         self.sign_in_img_lbl.place(x =70,y=20)
         self.user_name_lbl =  Label(self.side_bar,text='ADMIN',bg='white',fg='black',font=('yu gothic ui',15,'bold'))
         self.user_name_lbl.place(x=100, y=155)

         self.menu_icon1 = Image.open('image/dashboard.png')
         new_width = 35
         new_height = 35 
         self.menu_icon1 = self.menu_icon1.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.menu_icon1)
         self.menu_icon1_lbl = Label(self.side_bar,image=photo,bg='white')
         self.menu_icon1_lbl.image =photo
         self.menu_icon1_lbl.place(x =30,y=200)

         self.menu_lbl1 =  Label(self.side_bar,text='Dashboard',bg='#ffffff',font=('yu gothic ui',15,'bold')
                                ,bd=0,cursor='hand2',activebackground='#ffffff')
         self.menu_lbl1.place(x=85, y=200)
         self.menu_lbl1.bind("<Button-1>", self)
         
         self.menu_icon2 = Image.open('image/customer.png')
         new_width = 35
         new_height = 35 
         self.menu_icon2 = self.menu_icon2.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.menu_icon2)
         self.menu_icon2_lbl = Label(self.side_bar,image=photo,bg='white')
         self.menu_icon2_lbl.image =photo
         self.menu_icon2_lbl.place(x =30,y=250)

         self.menu_lbl2 =  Label(self.side_bar,text='Customer',bg='#ffffff',font=('yu gothic ui',15,'bold')
                                ,bd=0,cursor='hand2',activebackground='#ffffff')
         self.menu_lbl2.place(x=85, y=250)
         self.menu_lbl2.bind("<Button-1>", self)
         
         self.menu_icon3 = Image.open('image/drugs.png')
         new_width = 35
         new_height = 35 
         self.menu_icon3 = self.menu_icon3.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.menu_icon3)
         self.menu_icon3_lbl = Label(self.side_bar,image=photo,bg='white')
         self.menu_icon3_lbl.image =photo
         self.menu_icon3_lbl.place(x =30,y=300)

         self.menu_lbl3 =  Label(self.side_bar,text='Medicine',bg='#ffffff',font=('yu gothic ui',15,'bold')
                                ,bd=0,cursor='hand2',activebackground='#ffffff')
         self.menu_lbl3.place(x=85, y=300)
         self.menu_lbl3.bind("<Button-1>", self)
         
         self.menu_icon4 = Image.open('image/supplier.png')
         new_width = 35
         new_height = 35 
         self.menu_icon4 = self.menu_icon4.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.menu_icon4)
         self.menu_icon4_lbl = Label(self.side_bar,image=photo,bg='white')
         self.menu_icon4_lbl.image =photo
         self.menu_icon4_lbl.place(x =30,y=350)

         self.menu_lbl4 =  Label(self.side_bar,text='Supplier',bg='#ffffff',font=('yu gothic ui',15,'bold')
                                ,bd=0,cursor='hand2',activebackground='#ffffff')
         self.menu_lbl4.place(x=85, y=350)
         self.menu_lbl4.bind("<Button-1>", self)
         
         self.menu_icon5 = Image.open('image/return.png')
         new_width = 35
         new_height = 35 
         self.menu_icon5 = self.menu_icon5.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.menu_icon5)
         self.menu_icon5_lbl = Label(self.side_bar,image=photo,bg='white')
         self.menu_icon5_lbl.image =photo
         self.menu_icon5_lbl.place(x =30,y=400)

         self.menu_lbl5 =  Label(self.side_bar,text='Return',bg='#ffffff',font=('yu gothic ui',15,'bold')
                                ,bd=0,cursor='hand2',activebackground='#ffffff')
         self.menu_lbl5.place(x=85, y=400)
         self.menu_lbl5.bind("<Button-1>", self)
         
         self.menu_icon6 = Image.open('image/hr.png')
         new_width = 35
         new_height = 35 
         self.menu_icon6 = self.menu_icon6.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.menu_icon6)
         self.menu_icon6_lbl = Label(self.side_bar,image=photo,bg='white')
         self.menu_icon6_lbl.image =photo
         self.menu_icon6_lbl.place(x =30,y=450)

         self.menu_lbl6 =  Label(self.side_bar,text='Human Resources',bg='#ffffff',font=('yu gothic ui',15,'bold')
                                ,bd=0,cursor='hand2',activebackground='#ffffff')
         self.menu_lbl6.place(x=85, y=450)
         self.menu_lbl6.bind("<Button-1>", self)
         
         self.menu_icon7 = Image.open('image/finance.png')
         new_width = 35
         new_height = 35 
         self.menu_icon7 = self.menu_icon7.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.menu_icon7)
         self.menu_icon7_lbl = Label(self.side_bar,image=photo,bg='white')
         self.menu_icon7_lbl.image =photo
         self.menu_icon7_lbl.place(x =30,y=500)

         self.menu_lbl7 =  Label(self.side_bar,text='Finance',bg='#ffffff',font=('yu gothic ui',15,'bold')
                                ,bd=0,cursor='hand2',activebackground='#ffffff')
         self.menu_lbl7.place(x=85, y=500)
         self.menu_lbl7.bind("<Button-1>", self)
         
         self.menu_icon8 = Image.open('image/report.png')
         new_width = 35
         new_height = 35 
         self.menu_icon8 = self.menu_icon8.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.menu_icon8)
         self.menu_icon8_lbl = Label(self.side_bar,image=photo,bg='white')
         self.menu_icon8_lbl.image =photo
         self.menu_icon8_lbl.place(x =30,y=550)

         self.menu_lbl8 =  Label(self.side_bar,text='Report',bg='#ffffff',font=('yu gothic ui',15,'bold')
                                ,bd=0,cursor='hand2',activebackground='#ffffff')
         self.menu_lbl8.place(x=85, y=550)
         self.menu_lbl8.bind("<Button-1>", self)
         
         self.menu_icon9 = Image.open('image/setting.png')
         new_width = 35
         new_height = 35 
         self.menu_icon9 = self.menu_icon9.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.menu_icon9)
         self.menu_icon9_lbl = Label(self.side_bar,image=photo,bg='white')
         self.menu_icon9_lbl.image =photo
         self.menu_icon9_lbl.place(x =30,y=600)

         self.menu_lbl9 =  Label(self.side_bar,text='Setting',bg='#ffffff',font=('yu gothic ui',15,'bold')
                                ,bd=0,cursor='hand2',activebackground='#ffffff')
         self.menu_lbl9.place(x=85, y=600)
         self.menu_lbl9.bind("<Button-1>", self)

         
         


    def toggle_profile_options(self, event):
        if self.profile_options_frame.winfo_ismapped():
            self.profile_options_frame.place_forget()  # Hide the profile options
        else:
            self.profile_options_frame.place(x=1340, y=100, width=180, height=100)  # Show the profile options

    def view_profile(self,event):
        messagebox.showinfo("User Profile", "Displaying user profile information...")

    def logout(self,event):
        response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if response:
            self.quit()  # Exit the program
            messagebox.showinfo("Logged Out", "You have been logged out successfully.")
    def show_time(self):
        self.time =time.strftime("%H:%M:%S")
        self.date =time.strftime("%d.%m.%Y")
        self.text =f"{self.date} - {self.time}"
        self.date_time.configure(text=self.text,font=('yu gothic ui',13,'bold'),bg='#009df4',fg='white')
        self.date_time.after(100,self.show_time)

def main():
     window = Tk()
     Deshboard(window)
     window.mainloop()

if __name__ == '__main__':
     main()


