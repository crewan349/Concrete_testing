import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainMenu(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # Title header
        hdr_txt = "Please select what you want to do" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        self.options()

    def options(self):
        # creater the 3 options
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        newSamp = ttk.Button(self, text="New Sample", bootstyle=PRIMARY, command= NewSample)
        newSamp.pack(side=LEFT, padx=5, pady=10)

        streTest = ttk.Button(self, text="Strength Test", bootstyle=SECONDARY, command= StrengthTest)
        streTest.pack(side=LEFT, padx=5, pady=10)
        
        check = ttk.Button(self, text="Check Results", bootstyle=(SECONDARY))
        check.pack(side=LEFT, padx=5, pady=10)

class NewSample(ttk.Frame):
    def __init__(self):
        self.frame = ttk.Frame.winfo_toplevel
        super().__init__( padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # new sample veriables
        self.date = ttk.StringVar(value="")
        self.job = ttk.StringVar(value="")
        self.location = ttk.StringVar(value="")
        self.slump = ttk.StringVar(value="")
        self.air = ttk.StringVar(value="")
        self.temp = ttk.StringVar(value="")
        self.unitWeight = ttk.StringVar(value="")
        self.number = ttk.StringVar(value="")
        #???value for each age???

        # new sample header
        hdr_txt = "Please fill all fields" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        self.create_form_entry("date", self.date)
        self.create_form_entry("job", self.job)
        self.create_form_entry("location", self.location)
        self.create_form_entry("slump", self.slump)
        self.create_form_entry("air", self.air)
        self.create_form_entry("temp", self.temp)
        self.create_form_entry("unit weight", self.unitWeight)
        #???value for each age???
        self.create_button_box()

    def create_form_entry(self, label, variable):
        # Creates a single form entry
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_button_box(self):
        # Create the application buttonbox
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        # Print the contents to console and return the values.
        print("date: ", self.date.get())
        print("job: ", self.job.get())
        print("location: ", self.location.get())
        print("slump: ", self.slump.get())
        print("air: ", self.air.get())
        print("temp: ", self.temp.get())
        print("unit weight: ", self.unitWeight.get())
        self.forget()
        return self.date.get(), self.job.get(), self.location.get(), self.slump.get(), self.air.get(), self.temp.get(), self.unitWeight.get()

    def on_cancel(self):
        # Cancel and close the application.
        self.forget()


class StrengthTest(ttk.Frame):
    def __init__(self):
        super().__init__( padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
    
        # strenght test variables
        self.diameter = ttk.StringVar(value="")
        self.load = ttk.StringVar(value="")

        # new sample header
        hdr_txt = "Please fill all fields" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)
        
        self.create_form_entry("diameter", self.diameter)
        self.create_form_entry("load", self.load)
        self.create_button_box()

    def create_form_entry(self, label, variable):
        # Creates a single form entry
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_button_box(self):
        # Create the application buttonbox
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        checkDiameter = self.diameter.get()
        print(checkDiameter)
        if checkDiameter == '4' or checkDiameter == '6':
            if self.load.get().isdigit():
                # Print the contents to console and return the values.
                print("diameter: ", self.diameter.get())
                print("load: ", self.load.get())

                self.forget()
                return self.diameter.get(), self.load.get()

    
    def on_cancel(self):
        # Cancel and close the application.
        self.forget()

def checkNewSample(date, job, location, slump, air, temp, unitWeight):
    return True

if __name__ == "__main__":

    app = ttk.Window("Concrete Testing", "yeti", resizable=(False, False))
    MainMenu(app)
    app.mainloop()