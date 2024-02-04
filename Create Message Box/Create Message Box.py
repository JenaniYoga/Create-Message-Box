from tkinter import Tk
from tkinter import messagebox

main=Tk()

messagebox.showinfo("Information","Please Insert Disk")
messagebox.showwarning("Warning","Don't Plug Charger")
messagebox.showerror("Error","Please Check the Disk")
messagebox.askquestion("Confirm","Do You Want To Close The Window")
messagebox.askokcancel("Close","Close The Window")
main.mainloop()