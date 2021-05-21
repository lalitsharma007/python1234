from tkinter import  *
from tkinter import messagebox
win=Tk()

result1 = messagebox.askokcancel("title","do you really?")
print(result1)

result2 = messagebox.askyesno("title2","do you really?")
print(result2)

result3 = messagebox.askyesnocancel("title3","do you really?")
print(result3)
messagebox.showinfo('title','a tk message')
messagebox.showwarning('warning', 'a tk message')
messagebox.showerror('error', 'a tk error')
win.mainloop()

