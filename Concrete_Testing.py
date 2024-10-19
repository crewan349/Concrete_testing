import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pandas as pd
import csv

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
        self.create_form_entry("date (MM-DD-YYYY)", self.date)
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

        lbl = ttk.Label(master=container, text=label.title(), width=20)
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
        #on_submit will check the user input
        # check to make sure a date was entered
        checkDate = False
        check = 0
        dateArray = self.date.get().split('-')
        if len(dateArray) == 3:
            if 1 <= int(dateArray[0]) <= 12:
                if 1 <= int(dateArray[1]) <= 31:
                    if 1000 <= int(dateArray[2]) <= 9999:
                         checkDate = True                
        if checkDate == False:
            errorMessage = ttk.Label(master=self, text="Date must be MM-DD-YYYY", width=50)
            errorMessage.pack(fill=X, pady=10)
            check += 1 

        # job and location just need to not be empty
        if self.job.get() == '':
            check +=1
            errorMessage = ttk.Label(master=self, text="Job must have data", width=50)
            errorMessage.pack(fill=X, pady=10)
        if self.location.get() == '':
            check +=1
            errorMessage = ttk.Label(master=self, text="location must have data", width=50)
            errorMessage.pack(fill=X, pady=10)
        
        # slump must be to the quarter inch
        try:
            slumpVal = self.slump.get()
            if not '.' in slumpVal:
                slumpVal = slumpVal + '.'
            if 1 < float(slumpVal) < 12:
                val = float('.' + slumpVal.split('.')[1] + '0')
                if val == .25 or val == .5 or val == .75 or val == 0:
                    checkSlump = True
        except:
            checkSlump = False

        if not checkSlump:
            check +=1
            errorMessage = ttk.Label(master=self, text="Slump most be rounded to the nearest quarter inch", width=50)
            errorMessage.pack(fill=X, pady=10)

        #the air must be put in to the nearist tenth
        checkAir = False
        try:
            if self.air.get().isdigit():
                checkAir = True
            airVal = self.air.get().split('.')
            if len(airVal) == 2:
                if len(airVal[1]) <= 1 and airVal[0].isdigit(): 
                    if airVal[1].isdigit() or airVal[1] == '':
                        checkAir = True
        except:
            checkAir = False

        if not checkAir:
            check +=1
            errorMessage = ttk.Label(master=self, text="Air should be rounded to the nearist tenth", width=50)
            errorMessage.pack(fill=X, pady=10)

        #temp value just needs to be a whole number
        if not self.temp.get().isdigit():
            check +=1
            errorMessage = ttk.Label(master=self, text="Tempature should be rounded to the nearist whole number", width=50)
            errorMessage.pack(fill=X, pady=10)

        #unit wight must be rounded to the tenth
        checkUW = False
        try:
            if self.unitWeight.get().isdigit():
                checkUW = True
            uWVal = self.unitWeight.get().split('.')
            if len(uWVal) == 2:
                if len(uWVal[1]) <= 1 and uWVal[0].isdigit(): 
                    if uWVal[1].isdigit() or uWVal[1] == '':
                        checkUW = True
        except:
            checkUW = False

        if not checkUW:
            check +=1
            errorMessage = ttk.Label(master=self, text="Unit weight should be rounded to the nearist tenth", width=50)
            errorMessage.pack(fill=X, pady=10)
        
        #if all cheks pass add to csv file
        if check <1:
            self.forget()

            rowCount = 0
            with open('tests.csv', 'r') as csvRead:
                reader = csv.reader(csvRead)
                rowCount = sum(1 for row in reader)
                print(rowCount)
                csvRead.close()

            #newRow = {'date': self.date.get(), 'job': self.job.get(),'location': self.location.get(), 'slump': self.slump.get(), 
            # 'air': self.air.get(), 'temp': self.temp.get(), 'unit weight': self.unitWeight.get(),}
            newRow = [rowCount, self.date.get(), self.job.get(), self.location.get(), self.slump.get(), self.air.get(), 
                      self.temp.get(), self.unitWeight.get(), '*']

            with open('tests.csv', 'a', newline='') as csvEdit:
                writer = csv.writer(csvEdit)
                writer.writerow(newRow)
                csvEdit.close()

            return True

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

if __name__ == "__main__":

    app = ttk.Window("Concrete Testing", "yeti", resizable=(False, False))
    MainMenu(app)
    app.mainloop()