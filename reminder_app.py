import datetime
from tkinter import *
import tkinter.messagebox as messagebox


class MedicationReminder:
    def __init__(self):
        self.window = Tk() 
        self.window.title("Medication Reminder")
        
        # User inputs  
        self.name_label = Label(text="Medication Name:")  
        self.name_entry = Entry()
        self.dosage_label = Label(text="Dosage:")
        self.dosage_entry = Entry()
        self.time_label = Label(text="Time to Take:")
        self.time_entry = Entry()
        
        # Schedule list
        self.listbox = Listbox()
        
        # Buttons
        self.add_button = Button(text="Add Medication", command=self.add_med)  
        self.remove_button = Button(text="Remove", command=self.remove_med)
        self.show_button = Button(text="Show Reminders", command=self.open_reminders)

        # Visual layout
        self.layout_components()
        
    def layout_components(self):
        # Layout code   
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)  
        self.dosage_label.grid(row=1, column=0)
        self.dosage_entry.grid(row=1, column=1)
        self.time_label.grid(row=2, column=0)  
        self.time_entry.grid(row=2, column=1)
        self.listbox.grid(row=5, column=0, columnspan=4)
        self.add_button.grid(row=3, column=0, pady=10)
        self.remove_button.grid(row=3, column=1) 
        self.show_button.grid(row=3, column=2)

    def add_med(self):
        # Gets user input and adds to schedule
        name = self.name_entry.get()
        dosage = self.dosage_entry.get()
        time = self.time_entry.get()
        
        # Checks for valid time
        try: 
            time_dt = datetime.datetime.strptime(time, "%H:%M")
            dosage_int = int(dosage)
            self.listbox.insert(END, f"{name}, {dosage}mg, at {time}") 
        except ValueError:
            messagebox.showerror(title="Invalid Input", message="Please enter valid time and dosage")
        
    def remove_med(self):
        self.listbox.delete(ANCHOR)
        
    def open_reminders(self):
       messagebox.showinfo(title="Medication Reminders", message=self.listbox.get(0, END)) 
        
if __name__ == '__main__':
    app = MedicationReminder()
    app.window.mainloop()