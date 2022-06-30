from tkinter import*
from tkinter import ttk


root = Tk()
root.title("Algebra | Smart Home")
root.configure(bg="#282828")





tabControl = ttk.Notebook(root)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
  
lock_door = Button(tab1,text="Lock the door", borderwidth=3, relief=RIDGE,bg="white", width=15, height=1)
lock_door.grid(row=1, column=0, padx=15, pady=5)

unlock_door = Button(tab1,text="Unlock the door", borderwidth=3, relief=RIDGE,bg="white", width=15, height=1)
unlock_door.grid(row=1, column=3, padx=15, pady=5)

ttk.Label(tab1, 
          text ="Upravljanje vratima").grid(column = 1, 
                               row = 0,
                               padx = 30,
                               pady = 30)  
ttk.Label(tab2,
          text ="").grid(column = 1,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)
  
tabControl.add(tab1, text ='Upravljanje vratima')
tabControl.add(tab2, text ='Settings')
tabControl.pack(expand = 1, fill ="both")





root.mainloop()