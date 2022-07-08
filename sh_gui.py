from tkinter import*
from tkinter import ttk
from Meteo.meteo import MeteoData

from datetime_utils import*
from Meteo import*


root = Tk()
root.title("Algebra | Smart Home")
root.configure(bg="#282828")




tabControl = ttk.Notebook(root)
tabControl.grid(row=1,column=0,padx=5,pady=5)


tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)  


def create_datetime_frame():
    def refresh_time():
        now_time = formatted_time()
        time_label.configure(text=now_time)
        time_label.after(1000, refresh_time)

    datetime_frame = Frame(
        root, width=100, height=50, bg="#282828"
    )
    datetime_frame.grid(row=0, column=0, padx=5, pady=5)

    today = formatted_date()
    now_time = formatted_time()

    date_label = Label(
        datetime_frame, bg="#282828", fg="white",
        text=today, font=("Arial", 9)
    )
    date_label.grid(row=0, column=0, padx=5, pady=5)
    time_label = Label(
        datetime_frame, bg="#282828", fg="white",
        text=now_time, font=("Arial", 9)
    )
    time_label.grid(row=0, column=3, padx=5, pady=5)
    refresh_time()

create_datetime_frame()


def create_meteo_frame():
    meteo_frame = Frame(
        tab3, width=200, height=100, bg="#282828"
    )
    meteo_frame.grid(row=0, column=0, padx=15, pady=15)

    def refresh_temperature():
        zagreb_forecast = MeteoData() # poslali smo request na API
        temperature_data = zagreb_forecast.get_formatted_meteo_data()

        location_label.configure(text=temperature_data["location"])
        temperature_label.configure(text=f"{temperature_data['current_temperature']} °C")
        humidity_label.configure(text=temperature_data["humidity"])
        last_refresh_label.configure(text=temperature_data["last_refresh"])
        location_label.after(1000 * 60, refresh_temperature) 

    location_label = Label(
        meteo_frame, bg="#282828", fg="white", text="", font=("Arial", 10)
    )
    location_label.grid(row=0, column=0, padx=10, pady=10)

    temperature_label = Label(
        meteo_frame, bg="#282828", fg="white", text="", font=("Arial", 10)
    )
    temperature_label.grid(row=1, column=0, padx=10, pady=10)

    humidity_label =Label(
        meteo_frame, bg="#282828", fg="white", text="", font=("Arial", 10)
    )
    humidity_label.grid(row=2, column=0, padx=10, pady=10)

    last_refresh_label = Label(
        meteo_frame, bg="#282828", fg="white", text="", font=("Arial", 10)
    )
    last_refresh_label.grid(row=3, column=0, padx=10, pady=10)

    refresh_temperature()
create_meteo_frame()




lock_door = Button(tab1,text="Lock the door", borderwidth=3, relief=RIDGE,bg="white", width=15, height=1)
lock_door.grid(row=1, column=0, padx=15, pady=5)

unlock_door = Button(tab1,text="Unlock the door", borderwidth=3, relief=RIDGE,bg="white", width=15, height=1)
unlock_door.grid(row=1, column=3, padx=15, pady=5)


refresh = Button(tab3, text="Refresh",borderwidth=3, relief=RIDGE,bg="white", width=15, height=1)
refresh.grid(row=3, column=4, padx=15, pady=5)


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
tabControl.add(tab2, text ='Rasvjeta')
tabControl.add(tab3, text= "Meteo")
#tabControl.g(expand = 1, fill ="both")





root.mainloop()