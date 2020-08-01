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