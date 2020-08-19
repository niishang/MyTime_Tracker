from tkinter import *
import csv
import datetime
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master
        # widget can take all window
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Open", command=self.open_csv)
        fileMenu.add_command(label="Exit", command=self.exit_program)
        menu.add_cascade(label="File", menu=fileMenu)
        current_datetime_object = datetime.datetime.now()
        current_datetime_str = current_datetime_object.strftime('%d/%m/%Y %H:%M:%S')
        self.L1 = Label(self, text="My Task Tracker",).grid(row=0,column=1)
        self.L2 = Label(self, text="Task Start Time",).grid(row=1,column=0)
        self.L3 = Label(self, text="Task End Time",).grid(row=2,column=0)
        self.L4 = Label(self, text="Hours Worked",).grid(row=3,column=0)
        self.L4 = Label(self, text="Amount Earned $",).grid(row=4,column=0)
        self.E1 = Entry(self, bd =5)
        self.E1.grid(row=1,column=1)
        Entry.insert(self.E1,0, current_datetime_str)
        self.E2 = Entry(self, bd =5)
        self.E2.grid(row=2,column=1)
        Entry.insert(self.E2,0, current_datetime_str)
        self.E3 = Entry(self, bd =5)
        self.E3.grid(row=3,column=1)
        self.E4 = Entry(self, bd =5)
        self.E4.grid(row=4,column=1)
        self.B=Button(self, text ="Submit", command=self.calculate).grid(row=5,column=1,) 
        with open('tracker.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile,
                                    quotechar=',', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(["Start_Period", "End_Period", "Total_Hours", "Amount_Earned"])
    def calculate(self):
        start_date_str = Entry.get(self.E1)
        start = datetime.datetime.strptime(start_date_str, '%d/%m/%Y %H:%M:%S')
        end_date_str = Entry.get(self.E2)
        end = datetime.datetime.strptime(end_date_str, '%d/%m/%Y %H:%M:%S')  
        time_elapsed = end - start
        total_hours = round(time_elapsed.total_seconds() / 3600, 2)
        self.E3.delete(0, 'end')
        Entry.insert(self.E3,0, total_hours)
        total_amount_earned = round(total_hours * 5, 2)
        self.E4.delete(0, 'end')
        Entry.insert(self.E4,0, total_amount_earned)
        with open('tracker.csv', 'a+', newline='') as csvfile:
            csv_writer = csv.writer(csvfile,
                                    quotechar=',', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([start_date_str, end_date_str, str(total_hours), str(total_amount_earned)])
    def exit_program(self):
        exit()
    def open_csv(self):
        import os
        os.system("start tracker.csv")
        
root = Tk()
app = Window(root)
root.wm_title("My Tracker App")
root.geometry("380x380")
root.mainloop()