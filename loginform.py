from tkinter import *
from PIL import ImageTk,Image

class loginform:

    def __init__(self, window):
         self.window = window
         screen_width = self.window.winfo_screenwidth()
         screen_height = self.window.winfo_screenheight()
         self.window.geometry(f'{screen_width}x{screen_height}')
         self.window.resizable(0, 0)

         self.bg_frame = Image.open('image/bg.png')
         photo = ImageTk.PhotoImage(self.bg_frame)
         self.pg_panel = Label(self.window,image =photo)
         self.pg_panel.image = photo
         self.pg_panel.pack(fill='both', expand ='yes')

         self.lgn_frame = Frame(self.window, bg="#040405",width='1000',height=600)
         self.lgn_frame.place(x =250,y=80)

         self.text = "WELCOME"
         self.heading=Label(self.lgn_frame,text=self.text,font=('yu gothic ui',25,'bold'),bg='#040405',fg ='white')
         self.heading.place(x=80,y=30,width=300,height=30)

         self.side_img = Image.open('image/vector.png')
         photo = ImageTk.PhotoImage(self.side_img)
         self.side_img_lbl = Label(self.lgn_frame,image=photo,bg='#040405')
         self.side_img_lbl.image =photo
         self.side_img_lbl.place(x =5,y=100)

         self.sign_in_img = Image.open('image/user.png')
         new_width = 100
         new_height = 100  
         self.sign_in_img = self.sign_in_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.sign_in_img)
         self.sign_in_img_lbl = Label(self.lgn_frame,image=photo,bg='#040405')
         self.sign_in_img_lbl.image =photo
         self.sign_in_img_lbl.place(x =660,y=60)

         self.sign_in_lbl = Label(self.lgn_frame,text='Sign In',bg='#040405',fg='white',font=('yu gothic ui',17,'bold'))
         self.sign_in_lbl.place(x=670,y=160)

         self.user_name_lbl =  Label(self.lgn_frame,text='User Name',bg='#040405',fg='white',font=('yu gothic ui',13,'bold'))
         self.user_name_lbl.place(x=550, y=220)
         self.user_name_ent = Entry(self.lgn_frame,highlightthickness=0,relief=FLAT,bg='#040405',fg='#6b6a69',font=('yu gothic ui',12,'bold'))
         self.user_name_ent.place(x =590,y =250)    
         self.user_name_lin=Canvas(self.lgn_frame,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
         self.user_name_lin.place(x=550,y=290)    

         self.user_name_icon_img= Image.open('image/usricon.png')
         new_width = 45
         new_height = 35  
         self.user_name_icon_img = self.user_name_icon_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.user_name_icon_img)
         self.user_name_icon_img_lbl = Label(self.lgn_frame,image=photo,bg='#040405')
         self.user_name_icon_img_lbl.image =photo
         self.user_name_icon_img_lbl.place(x =540,y=250)

         self.Password_lbl =  Label(self.lgn_frame,text='Password',bg='#040405',fg='white',font=('yu gothic ui',13,'bold'))
         self.Password_lbl.place(x=550, y=320)
         self.Password_lbl_ent = Entry(self.lgn_frame,highlightthickness=0,relief=FLAT,bg='#040405',fg='#6b6a69',font=('yu gothic ui',12,'bold'))
         self.Password_lbl_ent.place(x =590,y =350)    
         self.Password_lin=Canvas(self.lgn_frame,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
         self.Password_lin.place(x=550,y=390)    

         self.Password_icon_img= Image.open('image/lock.png')
         new_width = 35
         new_height = 35  
         self.Password_icon_img = self.Password_icon_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.Password_icon_img)
         self.Password_icon_img_lbl = Label(self.lgn_frame,image=photo,bg='#040405')
         self.Password_icon_img_lbl.image =photo
         self.Password_icon_img_lbl.place(x =550,y=350)


         self.lgn_btn_img = Image.open('image/login.png')
         new_width = 255
         new_height = 80 
         self.lgn_btn_img = self.lgn_btn_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.lgn_btn_img)
         self.lgn_btn_img = Label(self.lgn_frame,image=photo,bg='#040405')
         self.lgn_btn_img.image =photo
         self.lgn_btn_img.place(x =580,y=400)


         self.lgn_btn = Button(self.lgn_btn_img,text='LOGIN',font=('yu gothic ui',13,'bold'),width=17,
                     bg ='#0a2ea0',cursor='hand2',activebackground='#0a2ea0',fg='white',relief='flat',highlightthickness=0)
         self.lgn_btn.place(x = 28 , y =22)

         self.forgot_btn = Button(self.lgn_frame,text='Forgot Password',font=('yu gothic ui',13,'bold underline'),width=17,
                     bg ='#040405',cursor='hand2',activebackground='#040405',fg='white',relief='flat',highlightthickness=0)
         self.forgot_btn.place(x = 620 , y =470)

         self.sgnup_lbl = Label(self.lgn_frame,text = 'No Account yet ?',font=('yu gothic ui',13,'bold'),bg='#040405',fg='white')
         self.sgnup_lbl.place(x=550,y=520)


         self.sgn_btn_img = Image.open('image/login.png')
         new_width = 180
         new_height = 60 
         self.sgn_btn_img = self.sgn_btn_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
         photo = ImageTk.PhotoImage(self.sgn_btn_img)
         self.sgn_btn_img = Label(self.lgn_frame,image=photo,bg='#040405')
         self.sgn_btn_img.image =photo
         self.sgn_btn_img.place(x =720,y=505)
         self.sgn_btn = Button(self.sgn_btn_img,text='SIGN UP',font=('yu gothic ui',11,'bold'),width=14,
                     bg ='#0a2ea0',cursor='hand2',activebackground='#0a2ea0',fg='white',relief='flat',highlightthickness=0)
         self.sgn_btn.place(x = 25, y =14)


   

       
def page():
    window = Tk()
    loginform(window)
    window.mainloop() 

if  __name__ == '__main__':
    page() 