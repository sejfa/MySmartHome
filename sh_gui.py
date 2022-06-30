from tkinter import*
from tkinter import ttk
from datetime_utils import*

root = Tk()
root.title("Algebra | Smart Home")
root.configure(bg="#282828")


tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
  
lock_door = Button(tab1,text="Lock the door", borderwidth=3, relief=RIDGE,bg="white", width=15, height=1)
lock_door.grid(row=1, column=0, padx=5, pady=5)

unlock_door = Button(tab1,text="Unlock the door", borderwidth=3, relief=RIDGE,bg="white", width=15, height=1)
unlock_door.grid(row=1, column=3, padx=5, pady=5)


ttk.Label(tab1, text ="Upravljanje vratima").grid(column = 1, row = 0, padx = 30, pady = 30)  


def date_frame():
    def refresh_time():
        now_time = formatted_time()
        quote_label.configure(text=now_time)
        quote_label.after(1000, refresh_time)

    dateandtime = Frame(root, borderwidth= 2, relief=RIDGE,bg="#282828", width=100, height=50)
    dateandtime.grid(row=0, column=0, padx=15, pady=5)
    today = formatted_date()
    now_time = formatted_time()

    date_label = Label(dateandtime, bg="#282828",fg="white",
    text=today, font=("Arial", 8))

    date_label.grid(row=0, column=0, padx=10, pady=5)

    quote_label = Label(dateandtime, bg="#282828",fg="white",
    text=today, font=("Arial", 10))
    quote_label.grid(row=0, column=1, padx=10, pady=5)

    refresh_time()

def settings_frame():
    change_color = Button(tab2, text="Change color", borderwidth=2, relief=RIDGE,bg="white", width=15,height=1)
    change_color.grid(row=1, column=0, padx=5, pady=5)

tabControl.add(tab1, text ='Upravljanje vratima')
tabControl.add(tab2, text ='Settings')
tabControl.grid(row=1, column=0, padx=10, pady=5)



settings_frame()
date_frame()
root.mainloop()