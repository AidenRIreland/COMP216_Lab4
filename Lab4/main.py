import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
class Survey(tk.Tk):

    def __init__(self,title :str) ->None:
        super().__init__()
        self.title(title)
        self.geometry('560x300')
        self.create_styles()
        self.container = Frame(self)#Create frame
        self.container.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.create_variables()
        self.create_ui(self.container)
        self.init_ui()

    def create_styles(self):
        style = Style(self)
        style.configure('.', background='#80cc80', foreground='black')
    
    def create_variables(self):
        self.name = StringVar()
        self.residency_var = StringVar()
        self.program_combo_value = StringVar()
        self.coursecheck = StringVar()
    def init_ui(self):
        self.name.set('Narendra Pershad')
        self.residency_var.set('dom')
        self.program_combo_value.set('Health')
        self.coursecheck.set('COMP100')
    
    def create_ui(self, parent):
        #row one for title
        label = Label(parent, text="ICET Student Survey", font=('Arial', 18, "bold italic"))
        label.place(relx= 0.15, rely=0.008, relwidth=0.5, relheight=0.15)
        #row two
        name_label = Label(parent, text="Full name:")
        name_label.place(relx=0.02, rely=0.15)
        name_entry = Entry(parent, textvariable=self.name)
        name_entry.place(relx=0.2, rely=0.15, relwidth=0.38, relheight=0.098) 
        #Row Three
        residency_label = Label(parent, text="Residency:")
        residency_label.place(relx=0.02, rely=0.25)
        radio_domestic = Radiobutton(parent, text="Domestic", variable=self.residency_var, value="dom")
        radio_domestic.place(relx=0.2, rely=0.25)
        radio_international = Radiobutton(parent, text="International", variable=self.residency_var, value="intl")
        radio_international.place(relx=0.2, rely=0.35)
        #Row 4
        program_label = Label(parent, text="Program:")
        program_label.place(relx=0.02, rely=0.45)
        program_combo = Combobox(parent, textvariable=self.program_combo_value, values=["Health", "Software", "AI", "Gaming"])
        program_combo.place(relx=0.2, rely=0.45, relwidth=0.3, relheight=0.098)
        #row 5 
        courses_label = Label(parent, text="Courses:")
        courses_label.place(relx=0.02, rely=0.60)
        course1_check = Checkbutton(parent, text = "Programming I", variable = self.coursecheck, onvalue ="COMP100", offvalue='')
        course1_check.place(relx=0.2, rely=0.60, relwidth=0.3, relheight=0.098)
        course2_check = Checkbutton(parent, text = "Web Programming Design", variable = self.coursecheck, onvalue ="COMP213", offvalue='')
        course2_check.place(relx=0.2, rely=0.70, relwidth=0.3, relheight=0.098)
        course3_check = Checkbutton(parent, text = "Software Engineering", variable= self.coursecheck, onvalue ="COMP120", offvalue='')
        course3_check.place(relx=0.2, rely=0.80, relwidth=0.3, relheight=0.098)
        #Row 6(Buttons)
    

        reset = Button(parent, text="Reset", command=self.init_ui)
        reset.place(relx=0.02, rely=0.9, relwidth=0.25)
        ok = Button(parent, text="Ok",command=self.ok_handler)
        ok.place(relx=0.3, rely=0.9, relwidth=0.25)
        exit = Button(parent, text='Exit', command=self.quit)
        exit.place(relx=0.6, rely=0.9, relwidth=0.25)
    def ok_handler(self):
        output = f'''
        Name    : {self.name.get()}
        Program : {self.program_combo_value.get()}
        Residency    : {self.residency_var.get()}
        Course   : {self.coursecheck.get()}
        '''
        messagebox.showinfo('Information', output)
app = Survey('Centennial College')
app.mainloop()