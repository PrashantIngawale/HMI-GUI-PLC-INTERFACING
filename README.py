from tkinter import *  # importing libraries
from tkinter import messagebox
from tkinter.ttk import Treeview

# from tkinter import ttk
from PIL import ImageTk
from time import strftime
from pylogix import PLC
import time
import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import xlsxwriter
# connecting with database>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", passwd="3603", database="plc_database")

comm = PLC()
comm.IPAddress = '192.168.10.10'


def main():
    # username = entry1.get()                                  # getting data from user(username & password)
    # password = entry2.get()
    #
    # if(username == "admin" and password == "admin"):
    # messagebox.showinfo("python message", "login sucessfull")

    global main_frame
    main_frame = Frame(root, width=1280, height=800, bg="white")
    main_frame.place(x=0, y=0)

    global frame_top
    global frame_left
    frame_top = Frame(main_frame, width=1280, height=80, bg="grey78")  # TOP FRAME of HMI
    frame_top.place(x=0, y=0)
    frame_bottom = Frame(main_frame, width=1280, height=80, bg="grey78")  # BOTTOM FRAME of HMI
    frame_bottom.place(x=0, y=720)

    # Home_Win()               # calling home window to show home screen directly after login
    # Displaying logo image
    global logo, photo
    logo = ImageTk.PhotoImage(
        file=r"C:\Users\prash\PycharmProjects\HMI_CTPL\ctpl1.png")  # Displaying Company LOGO on upper left corner
    # label = Label(root, image=icon).place(x=450, y=100)
    label = Label(root, image=logo)
    label.place(x=3, y=3)

    # photo = ImageTk.PhotoImage(
    # file=r"C:\Users\prash\PycharmProjects\HMI_CTPL\roboticarm.png")
    # labelp = Label(root, image=photo,height=640,width=1280)
    # labelp.place(x=0, y=80)

    # Displaying realtime Day, Time & Date
    def my_time():
        global time_string
        time_string = strftime(
            '%x  \n%H:%M:%S %p')  # time format:- %A=Day, %x=Date, %H=hours %M= minutes, %S= Sec., %p= AM/PM
        l1.config(text=time_string)
        l1.after(1000, my_time)  # time delay of 1000 milliseconds

    my_font = ('times', 12, 'bold')  # display size and style

    l1 = Label(main_frame, font=my_font, bg='gray78')
    l1.place(x=1130, y=20)

    my_time()  # Calling time function

    global main_label
    main_label = Label(frame_top, text="MAIN WINDOW", font="Lora 20 bold", bg="gray78")  # Displaying label on TOP frame
    main_label.place(x=560, y=30)

    # Importing File path to display images over buttons
    global home, mode, sett, manual, alarm, seq, legend
    home = ImageTk.PhotoImage(file=r"C:\Users\prash\PycharmProjects\HMI_CTPL\home3.png")
    mode = ImageTk.PhotoImage(file=r"C:\Users\prash\PycharmProjects\HMI_CTPL\mode.png")
    sett = ImageTk.PhotoImage(file=r"C:\Users\prash\PycharmProjects\HMI_CTPL\settings.png")
    manual = ImageTk.PhotoImage(file=r"C:\Users\prash\PycharmProjects\HMI_CTPL\man.png")
    alarm = ImageTk.PhotoImage(file=r"C:\Users\prash\PycharmProjects\HMI_CTPL\alarm.png")
    seq = ImageTk.PhotoImage(file=r"C:\Users\prash\PycharmProjects\HMI_CTPL\sequence.png")
    legend = ImageTk.PhotoImage(file=r"C:\Users\prash\PycharmProjects\HMI_CTPL\legends.png")

    def hide_indicator():
        HomeButton_indicate.config(bg="gray78")
        ModeSelect_indicate.config(bg="gray78")
        Settings_indicate.config(bg="gray78")
        ManualOperatin_indicate.config(bg="gray78")
        Alarm_indicate.config(bg="gray78")
        Sequence_indicate.config(bg="gray78")
        Legends_indicate.config(bg="gray78")

    # highlight indicator for buttons----------------------------
    def indicate(lb, page):
        hide_indicator()
        lb.config(bg="orange")

    # creating buttons on main_frame

    HomeButton = Button(main_frame, text="Home", image=home, command=lambda: indicate(HomeButton_indicate, Home_Win()),
                        font="Lora 10 bold", bg="gray78", activeforeground="orange", activebackground="orange", bd=4)
    HomeButton_indicate = Label(main_frame, text=" ", bg="gray78")  # creating indicating label
    ModeSelect = Button(main_frame, text="Mode \nSelection", image=mode,
                        command=lambda: indicate(ModeSelect_indicate, ModeSelect_Win()), font="Lora 10 bold",
                        bg="gray78", activebackground="orange", fg="#FEA95E", bd=4)
    ModeSelect_indicate = Label(main_frame, text=" ", bg="gray78")
    Settings = Button(main_frame, text="Settings", image=sett,
                      command=lambda: indicate(Settings_indicate, Settings_Win()), font="Lora 10 bold", bg="gray78",
                      fg="#FEA95E", activebackground="orange", bd=4)
    Settings_indicate = Label(main_frame, text=" ", bg="gray78")
    ManualOperatin = Button(main_frame, text="Manual \nOperation ", image=manual,
                            command=lambda: indicate(ManualOperatin_indicate, ManualOperetion_win()),
                            font="Lora 10 bold", bg="gray78", activebackground="orange", fg="#FEA95E", bd=4)
    ManualOperatin_indicate = Label(main_frame, text=" ", bg="gray78")
    Alarm = Button(main_frame, text="Alarms", image=alarm, command=lambda: indicate(Alarm_indicate, Alarm_win()),
                   font="Lora 10 bold", bg="gray78", fg="#FEA95E", activebackground="orange", bd=4)
    Alarm_indicate = Label(main_frame, text=" ", bg="gray78")
    Sequence = Button(main_frame, text="Sequence", image=seq,
                      command=lambda: indicate(Sequence_indicate, Sequence_win()), font="Lora 10 bold", bg="gray78",
                      fg="#FEA95E", activebackground="orange", bd=4)
    Sequence_indicate = Label(main_frame, text=" ", bg="gray78")
    Legends = Button(main_frame, text="Legends", image=legend,
                     command=lambda: indicate(Legends_indicate, Legends_win()), font="Lora 10 bold", bg="gray78",
                     fg="#FEA95E", activebackground="orange", bd=4)
    Legends_indicate = Label(main_frame, text=" ", bg="gray78")
    LogOut = Button(main_frame, text="Log Out", command=log_out, font="Lora 10 bold", height=3, width=8, bg="gray78",
                    fg="Black", activebackground="orange", bd=4)
    # SafetyChain = Button(main_frame, text="Safety\nChain",command=SafetyChain_win, font="Lora 10 bold", height=3, width=8,bg="#FEA95E",fg="Black", bd=4)

    # placing buttons and its indicator
    HomeButton.place(x=20, y=725)
    HomeButton_indicate.place(x=20, y=794, width=70, height=4)
    ModeSelect.place(x=140, y=725)
    ModeSelect_indicate.place(x=140, y=795, width=70, height=4)
    Settings.place(x=260, y=725)
    Settings_indicate.place(x=260, y=795, width=70, height=4)
    ManualOperatin.place(x=380, y=725)
    ManualOperatin_indicate.place(x=380, y=795, width=70, height=4)
    Alarm.place(x=500, y=725)
    Alarm_indicate.place(x=500, y=795, width=70, height=6)
    Sequence.place(x=620, y=725)
    Sequence_indicate.place(x=620, y=795, width=70, height=6)
    Legends.place(x=740, y=725)
    Legends_indicate.place(x=740, y=795, width=70, height=6)
    # SafetyChain.place(x=860, y=725)
    LogOut.place(x=1160, y=725)

    # combo = ttk.Combobox(root)
    # combo['values'] = (1, 2, 3, 4, 5, "USER")
    # combo.current(5)
    # combo.place(x=960, y=730)


# else:
#
#     messagebox.showerror('Python Error', 'Error: Invalid Username and Password !')          # Display error message for invalid USERNAME & PASSWORD
# ------------------------------------------------------------------------------
def root_win():
    global root
    root = Tk()  # creating LOGIN  window
    root.title("Cybernetik")
    root.geometry('1280x800')  # size of window
    root.resizable(0, 0)  # cant resize window

    global icon
    icon = ImageTk.PhotoImage(file=r"C:\Users\prash\PycharmProjects\HMI_CTPL\login_page.png")
    # label = Label(root, image=icon).place(x=450, y=100)
    label = Label(root, image=icon)
    label.place(x=0, y=0)
    Label(root, text="Username :", font="Lora 20 bold", bg="white").place(x=350, y=300)
    global entry1
    entry1 = Entry(root, font="Lora 20 bold", width=15, bg="white", highlightbackground="black",
                   highlightthickness=1)  # entry for Username
    entry1.place(x=530, y=300)

    Label(root, text="Password :", font="Lora 20 bold", bg="white").place(x=350, y=350)
    global entry2
    entry2 = Entry(root, show="*", font="Lora 20 bold", width=15, bg="white", highlightbackground="black",
                   highlightthickness=1)  # entry for Password
    entry2.place(x=530, y=350)

    login_bt = Button(root, text="LOG IN", command=main, font="Lora 9 bold", height=3, width=15, bg="orange",
                      fg="Black", bd=6)  # Creating Login button
    login_bt.place(x=580, y=430)


root_win()  # calling root_win() function


# -------------------------------------------------------creating multiple screens for each button-----------------

def Home_Win():
    global home_frame
    home_frame = Frame(root, width=1280, height=640, bg="white", highlightbackground="black", highlightthickness=1)
    home_frame.place(x=0, y=80)

    frame_left = Frame(home_frame, width=150, height=638, bg="grey78", highlightbackground="black",
                       highlightthickness=0.9)
    frame_left.place(x=0, y=0)

    # main_label.destroy()
    # (settings_label or modeSel_label).destroy()
    global home_label
    home_label = Label(frame_top, text="HOME", font="Lora 20 bold", bg="gray78", width=20)
    home_label.place(x=480, y=30)

    #   creating buttons on home screen
    global production_indicate, runtime_indicate, cycletime_indicate, downtime_indicate

    production_button = Button(home_frame, text="PRODUCTION",
                               command=lambda: indicateBt(production_indicate, productin_win()), font="Lora 10 bold",
                               height=2, width=13, bg="gray78", fg="Black", activebackground="orange", bd=3)
    production_indicate = Label(home_frame, text=" ", bg="gray78")  # creating indicating label
    runtime_button = Button(home_frame, text="RUN TIME", command=lambda: indicateBt(runtime_indicate, runtime_win()),
                            font="Lora 10 bold", height=2, width=13, bg="gray78", activebackground="orange",
                            fg="Black", bd=3)
    runtime_indicate = Label(home_frame, text=" ", bg="gray78")  # creating indicating label

    cycletime_button = Button(home_frame, text="CYCLE TIME",
                              command=lambda: indicateBt(cycletime_indicate, cycletime()), font="Lora 10 bold",
                              height=2, width=13, bg="gray78", activebackground="orange",
                              fg="Black", bd=3)
    cycletime_indicate = Label(home_frame, text=" ", bg="gray78")  # creating indicating label

    downtime_button = Button(home_frame, text="DOWN TIME", command=lambda: indicateBt(downtime_indicate, downtime()),
                             font="Lora 10 bold", height=2, width=13, bg="gray78", activebackground="orange",
                             fg="Black", bd=3)
    downtime_indicate = Label(home_frame, text=" ", bg="gray78")  # creating indicating label
    # placing buttons on home screen
    production_button.place(x=20, y=50)
    production_indicate.place(x=15, y=51, width=5, height=45)
    runtime_button.place(x=20, y=120)
    runtime_indicate.place(x=15, y=121, width=5, height=45)
    cycletime_button.place(x=20, y=190)
    cycletime_indicate.place(x=15, y=191, width=5, height=45)
    downtime_button.place(x=20, y=260)
    downtime_indicate.place(x=15, y=261, width=5, height=45)


def ModeSelect_Win():
    global modeSel_frame
    modeSel_frame = Frame(root, width=1280, height=640, bg="white", highlightbackground="black",
                          highlightthickness=1)
    modeSel_frame.place(x=0, y=80)

    frame_left = Frame(modeSel_frame, width=150, height=638, bg="grey78", highlightbackground="black",
                       highlightthickness=0.9)
    frame_left.place(x=0, y=0)

    global modesel_label
    modesel_label = Label(frame_top, text="MODE SELECT", font="Lora 20 bold", bg="gray78")
    modesel_label.place(x=540, y=30)
    global preset_indicate, safety_indicate, faultclear_indicate
    preaset_button = Button(modeSel_frame, text="PRESTART", command=lambda: indicateMS(preset_indicate, prestart_win()),
                            font="Lora 10 bold", height=2,
                            width=13, bg="gray78", fg="Black", activebackground="orange", bd=3)
    preset_indicate = Label(modeSel_frame, text=" ", bg="gray78")  # creating indicating label
    safety_button = Button(modeSel_frame, text="SAFETY", command=lambda: indicateMS(safety_indicate, safety_win()),
                           font="Lora 10 bold", height=2, width=13,
                           bg="gray78", fg="Black", activebackground="orange", bd=3)
    safety_indicate = Label(modeSel_frame, text=" ", bg="gray78")  # creating indicating label
    faultclear_button = Button(modeSel_frame, text="FAULT CLEAR",
                               command=lambda: indicateMS(faultclear_indicate, faultclear_win()), font="Lora 10 bold",
                               height=2,
                               width=13, bg="gray78", activebackground="orange",
                               fg="Black", bd=3)
    faultclear_indicate = Label(modeSel_frame, text=" ", bg="gray78")  # creating indicating label

    preaset_button.place(x=20, y=50)
    preset_indicate.place(x=15, y=51, width=5, height=45)
    safety_button.place(x=20, y=120)
    safety_indicate.place(x=15, y=121, width=5, height=45)
    faultclear_button.place(x=20, y=190)
    faultclear_indicate.place(x=15, y=191, width=5, height=45)


def Settings_Win():
    settings_frame = Frame(root, width=1280, height=640, bg="white", highlightbackground="black",
                           highlightthickness=1)
    settings_frame.place(x=0, y=80)

    frame_left = Frame(settings_frame, width=150, height=638, bg="grey78", highlightbackground="black",
                       highlightthickness=0.9)
    frame_left.place(x=0, y=0)

    global settings_label
    settings_label = Label(frame_top, text="SETTINGS", font="Lora 20 bold", bg="gray78", width=20)
    settings_label.place(x=480, y=30)


def ManualOperetion_win():
    manualOp_frame = Frame(root, width=1280, height=640, bg="white", highlightbackground="black",
                           highlightthickness=1)
    manualOp_frame.place(x=0, y=80)

    frame_left = Frame(manualOp_frame, width=150, height=638, bg="grey78", highlightbackground="black",
                       highlightthickness=0.9)
    frame_left.place(x=0, y=0)

    global manualOp_label
    manualOp_label = Label(frame_top, text="MANUAL OPERATION", font="Lora 20 bold", bg="gray78")
    manualOp_label.place(x=530, y=30)

    # creating buttons on manual operation window
    global inputList_indicate, outputList_indicate, network_indicate
    inputList_button = Button(manualOp_frame, text="INPUT LIST",
                              command=lambda: indicateMO(inputList_indicate, inputList_win()), font="Lora 10 bold",
                              height=2,
                              width=13, bg="gray78", fg="Black", activebackground="orange", bd=3)
    inputList_indicate = Label(manualOp_frame, text=" ", bg="gray78")  # creating indicating label
    outputList_button = Button(manualOp_frame, text="OUTPUT LIST",
                               command=lambda: indicateMO(outputList_indicate, outputList_win()), font="Lora 10 bold",
                               height=2, width=13, bg="gray78", activebackground="orange",
                               fg="Black", bd=3)
    outputList_indicate = Label(manualOp_frame, text=" ", bg="gray78")  # creating indicating label
    network_button = Button(manualOp_frame, text="NETWORK", command=lambda: indicateMO(network_indicate, network_win()),
                            font="Lora 10 bold", height=2,
                            width=13, bg="gray78", activebackground="orange",
                            fg="Black", bd=3)
    network_indicate = Label(manualOp_frame, text=" ", bg="gray78")  # creating indicating label
    inputList_button.place(x=20, y=50)
    inputList_indicate.place(x=15, y=51, width=5, height=45)
    outputList_button.place(x=20, y=120)
    outputList_indicate.place(x=15, y=121, width=5, height=45)
    network_button.place(x=20, y=190)
    network_indicate.place(x=15, y=191, width=5, height=45)


def Alarm_win():
    alarm_frame = Frame(root, width=1280, height=640, bg="white", highlightbackground="black",
                        highlightthickness=1)
    alarm_frame.place(x=0, y=80)

    frame_left = Frame(alarm_frame, width=150, height=638, bg="grey78", highlightbackground="black",
                       highlightthickness=0.9)
    frame_left.place(x=0, y=0)

    global alarm_label
    alarm_label = Label(frame_top, text="ALARM", font="Lora 20 bold", bg="gray78", width=20)
    alarm_label.place(x=480, y=30)
    global activealarm_indicate, alarmhistory_indicate
    activeAlarm = Button(alarm_frame, text=" ACTIVE ALARMS",
                         command=lambda: indicateA(activealarm_indicate, activeAlarms_win()), font="Lora 10 bold",
                         height=2,
                         width=13, bg="gray78", activebackground="orange",
                         fg="Black", bd=3)
    activealarm_indicate = Label(alarm_frame, text=" ", bg="gray78")  # creating indicating label
    alarmHistory_button = Button(alarm_frame, text="ALARM HISTORY",
                                 command=lambda: indicateA(alarmhistory_indicate, alarmHistory_win()),
                                 font="Lora 10 bold",
                                 height=2, width=13, bg="gray78", activebackground="orange",
                                 fg="Black", bd=3)
    alarmhistory_indicate = Label(alarm_frame, text=" ", bg="gray78")  # creating indicating label
    activeAlarm.place(x=20, y=50)
    activealarm_indicate.place(x=15, y=51, width=5, height=45)
    alarmHistory_button.place(x=20, y=120)
    alarmhistory_indicate.place(x=15, y=121, width=5, height=45)


def Sequence_win():
    sequence_frame = Frame(root, width=1280, height=640, bg="white", highlightbackground="black",
                           highlightthickness=1)
    sequence_frame.place(x=0, y=80)

    frame_left = Frame(sequence_frame, width=150, height=638, bg="grey78", highlightbackground="black",
                       highlightthickness=0.9)
    frame_left.place(x=0, y=0)

    global sequence_label
    sequence_label = Label(frame_top, text="SEQUENCE", font="Lora 20 bold", bg="gray78", width=20)
    sequence_label.place(x=480, y=30)


def Legends_win():
    legends_frame = Frame(root, width=1280, height=640, bg="white", highlightbackground="black",
                          highlightthickness=1)
    legends_frame.place(x=0, y=80)

    frame_left = Frame(legends_frame, width=150, height=638, bg="grey78", highlightbackground="black",
                       highlightthickness=0.9)
    frame_left.place(x=0, y=0)

    global legends_label
    legends_label = Label(frame_top, text="LEGENDS", font="Lora 20 bold", bg="gray78", width=20)
    legends_label.place(x=480, y=30)
    def get_mysql_data():
        try:
            # displaying plc tag values on legends window
            query = "SELECT * FROM plc_tags"            # SQL Query
            cursor = con.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            return data

        except mysql.Error as e:
            print("Error connecting to MySQL:", e)
            return None
    def display_data():
        data = get_mysql_data()
        if data:
            for item in data:
                tree.insert('', END, values=item)

    if __name__ == "__main__":

        tree = Treeview(root, columns=('date_time', 'tag_name', 'tag_value'), show='headings', height = 15)
        tree.heading('date_time', text="Date_Time")
        tree.heading('tag_name', text='tag_name')
        tree.heading('tag_value', text='tag_Value')
        tree.place(x=200,y=150)

        display_data() # calling display_data() function to display database values on legends window



# def SafetyChain_win():
#     safetyChain_frame = Frame(root, width=1280, height=640, bg="white", highlightbackground="black",
#                        highlightthickness=1)
#     safetyChain_frame.place(x=0, y=80)
#
#     frame_left = Frame(safetyChain_frame, width=150, height=638, bg="grey78",highlightbackground="black",highlightthickness=0.9)
#     frame_left.place(x=0, y=0)
#
#     global safetyChain_label
#     safetyChain_label = Label(frame_top, text="SAFETY CHAIN", font="Lora 20 bold", bg="gray78",width=20)
#     safetyChain_label.place(x=500,y=30)

def log_out():
    main_frame.destroy()
    root.destroy()
    root_win()

# creating sub-screens on Home Screen   :>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def productin_win():
    global production_frame
    production_frame = Frame(root, width=1130, height=640, bg="white", highlightbackground="black",
                             highlightthickness=1)
    production_frame.place(x=150, y=80)


    global production_label
    production_label = Label(production_frame, text="PRODUCTION", font="Lora 15 bold", bg="white", width=20)
    production_label.place(x=380, y=0)

    # creating toggle button on production frame
    global toggle_buttonp
    toggle_buttonp = Button(production_frame, text="OFF", font=" Lora 10 bold", width=10, height=2, command=simpletoggle,
                           highlightthickness=3, highlightbackground="black", bg="gray78")
    toggle_buttonp.place(x=100, y=200)

    # creating LED indicator for toggle button
    global ledButtonp
    ledButtonp = Button(production_frame, text="   ", state=DISABLED, bg="red", height=1, width=2)
    ledButtonp.place(x=200, y=210)
    if toggle_state1:
        toggle_buttonp.config(text="ON")
        ledButtonp.config(bg="green")
    else:
        toggle_buttonp.config(text="OFF")
        ledButtonp.config(bg="red")

    # creating push button and LED Indicator
    def button_pressed():
        led.config(bg="green")

    def button_released():
        led.config(bg="red")

    # Create the LED
    led = Label(production_frame, bg="red", width=5, height=1)
    led.place(x=450, y=170)

    # Create the push button
    button = Button(production_frame, text="PUSH BT", font=" Lora 10 bold", width=10, height=2, highlightthickness=3,
                    highlightbackground="black", bg="gray78")
    button.place(x=400, y=200)


    # Configure push button events
    button.bind("<ButtonPress>", lambda event: button_pressed())
    button.bind("<ButtonRelease>", lambda event: button_released())
    update_values_production()

def runtime_win():
    global runtime_frame
    runtime_frame = Frame(root, width=1130, height=640, bg="WHITE", highlightbackground="black",
                          highlightthickness=1)
    runtime_frame.place(x=150, y=80)

    global runtime_label
    runtime_label = Label(runtime_frame, text="RUN TIME", font="Lora 15 bold", bg="white", width=20)
    runtime_label.place(x=380, y=0)

    global toggle_button
    toggle_button = Button(runtime_frame, text="OFF", font=" Lora 10 bold", width=10, height=2, command=Simpletoggle,
                           highlightthickness=3, highlightbackground="black", bg="gray78")

    toggle_button.place(x=800, y=100)

    # creating LED indicator
    global ledButton
    ledButton = Button(runtime_frame, text="   ", height=1, width=2)
    ledButton.place(x=900, y=100)

    def insert_data():


        # Convert the toggle_state to an integer (0 for OFF, 1 for ON) for the database
        state_value = PY_real01
        if state_value == 1:
            Additional_Info = ' PY_StartBit1 turned ON'
        else:
            Additional_Info = ' PY_StartBit1 turned OFF'



        cursor = con.cursor()
        cursor.execute("INSERT INTO alarm_history (Time_Date,Tag_name,Discription ) VALUES (%s,%s,%s)", (time_string,'PY_real01',Additional_Info))
        con.commit()

    if toggle_state:
        toggle_button.config(text="ON")
        ledButton.config(bg="green")
    else:
        toggle_button.config(text="OFF")
        ledButton.config(bg="red")

    # Create a Matplotlib figure and subplot
    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Create empty lists to store x and y data
    x_data = []
    y_data = []

    def write_plc_value():                      #defining a function to write alue in plc tag
        global value_present
        value_present = entry_value.get()
        if value_present:
            with PLC() as comm:
                comm.IPAddress = '192.168.10.10'
                value_to_write = entry_value.get()
                comm.Write('PY_real01', value_to_write)
            update_graph()  # Call update_graph immediately after writing the value
        else:
            messagebox.showwarning("Warning", "Invalid value")

    def write_plc_value2():             #defining a function to write alue in plc tag
        global value_present2
        value_present2 = entry_value2.get()
        if value_present2:
            with PLC() as comm:
                comm.IPAddress = '192.168.10.10'
                value_to_write = entry_value2.get()
                comm.Write('PY_real03', value_to_write)

            update_graph()  # Call update_graph immediately after writing the value
        else:
            messagebox.showwarning("Warning", "Invalid value")

    def update_graph():                 # defining the function to updating the trends(graph)
        with PLC() as comm:
            comm.IPAddress = '192.168.10.10'
            value1 = comm.Read('PY_real01')
            value2 = comm.Read('PY_real03')
            label_Int.set(value1.Value)
            Label_Int.set(value2.Value)

            # Append current time and value to the data lists
            x_data.append(datetime.datetime.now())
            y_data.append(value1.Value)
            y_data2.append(value2.Value)

            # Clear the previous graph
            ax.clear()

            # Plot the data points
            ax.plot(x_data, y_data, label='PLC Value 1')
            ax.plot(x_data, y_data2, label='PLC Value 2')
            ax.legend(["PLC Value 1", "PLC Value 2"],loc = "upper right")

            # Plot the given value as a red star marker
            ax.plot(x_data[-1], y_data[-1], )
            # Format the x-axis tick labels as hours:minutes:seconds
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            # Tell matplotlib to interpret the x-axis values as dates
            ax.xaxis_date()
            # Make space for and rotate the x-axis tick labels
            fig.autofmt_xdate()

            # Set the x-axis label
            ax.set_xlabel('Time')

            # Set the y-axis label
            ax.set_ylabel('Value')

            # Redraw the canvas
            canvas.draw()

            # Schedule the next update after a delay (e.g., 1 second)
            runtime_frame.after(1500, update_graph)


    # def on_configure(event):
    #     # Update the scroll region to match the size of the graph
    #     canvas.configure(scrollregion=canvas.bbox("all"))
    y_data2 = []
    # Create a label to display the PLC value
    label_text1 = Label(runtime_frame, text='PLC Value 1 :', font='arial 15', width="13", bg="white")
    label_text1.place(x=650, y=200)

    label_Int = IntVar()
    label_value1 = Label(runtime_frame, textvariable=label_Int, text='', font='arial 15', bg="white")
    label_value1.place(x=790, y=200)

    label_text2 = Label(runtime_frame, text='PLC Value 2 :', font='arial 15', width="13", bg="white")
    label_text2.place(x=650, y=240)

    Label_Int = IntVar()
    label_value2 = Label(runtime_frame, textvariable=Label_Int, text='', font='arial 15', bg="white")
    label_value2.place(x=790, y=240)

    # Create an entry widget for entering the value to write
    entry_Int = IntVar()
    entry_value = Entry(runtime_frame, textvariable=entry_Int, font='arial 15', highlightthickness=2)
    entry_value.place(x=660, y=290)

    Entry_Int = IntVar()
    entry_value2 = Entry(runtime_frame, textvariable=Entry_Int, font='arial 15', highlightthickness=2)
    entry_value2.place(x=890, y=290)

    # Create a button to write the value to the PLC
    button_write = Button(runtime_frame, text='Write PLC Value 1', command=lambda: [update_DataBase1(entry_Int),write_plc_value()], font='arial 15')
    button_write.place(x=660, y=340)
    # creating button to assigning
    button_write2 = Button(runtime_frame, text='Write PLC Value 2', command=lambda: [update_DataBase2(Entry_Int),write_plc_value2()], font='arial 15')
    button_write2.place(x=890, y=340)

    # Create a canvas to hold the graph and display on the runtime frame
    canvas = FigureCanvasTkAgg(fig, master=runtime_frame)
    canvas.draw()
    canvas.get_tk_widget().place(x=50, y=100)


    # Call the update_graph function to initially display the graph
    update_graph()

    def update_values():            # updating the values of the tag in the label on runtime frame ( updating value entered in entry box)

        with PLC() as comm:
            comm.IPAddress = '192.168.10.10'
            value = comm.Read('PY_real01')
            label_Int.set(value.Value)
        # Schedule the next update after a certain time interval (in milliseconds)
        runtime_frame.after(1500, update_values)  # Update every 0.1 second

    update_values_runtime()
    update_values()

    def update_values2():  # updating the values of the tag in the label on runtime frame ( updating value entered in entry box)

        with PLC() as comm:
            comm.IPAddress = '192.168.10.10'
            value = comm.Read('PY_real03')
            Label_Int.set(value.Value)

        # Schedule the next update after a certain time interval (in milliseconds)
        runtime_frame.after(1500, update_values2)  # Update every 0.1 second

    update_values_runtime()
    update_values2()



def cycletime():
    cycletime_frame = Frame(root, width=1130, height=640, bg="WHITE", highlightbackground="black",
                            highlightthickness=1)
    cycletime_frame.place(x=150, y=80)
    global cycletime_label
    cycletime_label = Label(cycletime_frame, text="CYCLE TIME", font="Lora 15 bold", bg="white", width=20)
    cycletime_label.place(x=380, y=0)


def downtime():                 # creating downtime window
    downtime_frame = Frame(root, width=1130, height=640, bg="WHITE", highlightbackground="black",
                           highlightthickness=1)
    downtime_frame.place(x=150, y=80)

    global downtime_label
    downtime_label = Label(downtime_frame, text="DOWN TIME", font="Lora 15 bold", bg="white", width=20)
    downtime_label.place(x=380, y=0)


# creating sub-screens on  Mode Selection   :>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def prestart_win():
    prestart_frame = Frame(root, width=1130, height=640, bg="WHITE", highlightbackground="black",
                           highlightthickness=1)
    prestart_frame.place(x=150, y=80)

    global prestart_label
    prestart_label = Label(prestart_frame, text="PRESTART", font="Lora 15 bold", bg="white", width=20)
    prestart_label.place(x=380, y=0)


def safety_win():
    safety_frame = Frame(root, width=1130, height=640, bg="WHITE", highlightbackground="black",
                         highlightthickness=1)
    safety_frame.place(x=150, y=80)

    global safety_label
    safety_label = Label(safety_frame, text="SAFETY", font="Lora 15 bold", bg="white", width=20)
    safety_label.place(x=380, y=0)


def faultclear_win():
    faultclear_frame = Frame(root, width=1130, height=640, bg="WHITE", highlightbackground="black",
                             highlightthickness=1)
    faultclear_frame.place(x=150, y=80)

    global faultclear_label
    faultclear_label = Label(faultclear_frame, text="FAULT CLEAR", font="Lora 15 bold", bg="white", width=20)
    faultclear_label.place(x=380, y=0)


# creating sub-screens on Manual Operations   :>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def inputList_win():
    inputlist_frame = Frame(root, width=1130, height=640, bg="WHITE", highlightbackground="black",
                            highlightthickness=1)
    inputlist_frame.place(x=150, y=80)

    global inputlist_label
    inputlist_label = Label(inputlist_frame, text="INPUT LIST", font="Lora 15 bold", bg="white", width=20)
    inputlist_label.place(x=380, y=0)


def outputList_win():
    outputlist_frame = Frame(root, width=1130, height=640, bg="WHITE", highlightbackground="black",
                             highlightthickness=1)
    outputlist_frame.place(x=150, y=80)

    global outputlist_label
    outputlist_label = Label(outputlist_frame, text="OUTPUT LIST", font="Lora 15 bold", bg="white", width=20)
    outputlist_label.place(x=380, y=0)


def network_win():
    network_frame = Frame(root, width=1130, height=640, bg="WHITE", highlightbackground="black",
                          highlightthickness=1)
    network_frame.place(x=150, y=80)

    global network_label
    network_label = Label(network_frame, text="NETWORK", font="Lora 15 bold", bg="white", width=20)
    network_label.place(x=380, y=0)


# creating sub-screens on ALARMS screen   :>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def activeAlarms_win():
    activeAlarms_frame = Frame(root, width=1130, height=640, bg="WHITE", highlightbackground="black",
                               highlightthickness=1)
    activeAlarms_frame.place(x=150, y=80)
    global activeAlarms_label
    activeAlarms_label = Label(activeAlarms_frame, text="ACTIVE ALARMS", font="Lora 15 bold", bg="white", width=20)
    activeAlarms_label.place(x=380, y=0)

    def get_mysql_data():
        try:
            # displaying Alarm History
            query = "SELECT * FROM active_alarm"            # SQL Query
            cursor = con.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            return data

        except mysql.Error as e:
            print("Error connecting to MySQL:", e)
            return None
    def display_data():
        data = get_mysql_data()
        if data:
            for item in data:
                tree.insert('', END, values=item)

    if __name__ == "__main__":

        tree = Treeview(root, columns=('Date_Time', 'Tag_name', 'Discription'), show='headings', height = 15)
        tree.heading('date_time', text="Date_Time")
        tree.heading('tag_name', text='Tag_Name')
        tree.heading('Discription', text='Tag_Value')
        tree.place(x=200,y=150)

        display_data() # calling display_data() function to display database values on legends window







def alarmHistory_win():
    alarmHistory_frame = Frame(root, width=1130, height=640, bg="WHITE", highlightbackground="black",
                               highlightthickness=1)
    alarmHistory_frame.place(x=150, y=80)
    global alarmHistory_label
    alarmHistory_label = Label(alarmHistory_frame, text="ALARM HISTORY", font="Lora 15 bold", bg="white", width=20)
    alarmHistory_label.place(x=380, y=0)


# creating indicators for all Sub-Screen buttons>>>>>>>>>>>>>>>>>>>>>>>>>>
def hide_indicatorLBt():
    # hide indicatoes for home screen
    production_indicate.config(bg="gray78")
    runtime_indicate.config(bg="gray78")
    cycletime_indicate.config(bg="gray78")
    downtime_indicate.config(bg="gray78")


# creating highlight indicator for buttons ----------------------------
def indicateBt(lb, page):
    hide_indicatorLBt()
    lb.config(bg="orange")


def hide_indicatorMS():
    preset_indicate.config(bg="gray78")
    safety_indicate.config(bg="gray78")
    faultclear_indicate.config(bg="gray78")


def indicateMS(lb, page):
    hide_indicatorMS()
    lb.config(bg="orange")


def hide_indicateMO():
    inputList_indicate.config(bg="gray78")
    outputList_indicate.config(bg="gray78")
    network_indicate.config(bg="gray78")


def indicateMO(lb, page):
    hide_indicateMO()
    lb.config(bg="orange")


def hide_indicateA():
    activealarm_indicate.config(bg="gray78")
    alarmhistory_indicate.config(bg="gray78")


def indicateA(lb, page):
    hide_indicateA()
    lb.config(bg="orange")

def update_values_runtime():
    # Update the button state here for runtime
    with PLC() as comm:
        comm.IPAddress = '192.168.10.10'
        value = comm.Read('PY_StartBit1')
        bt_value = value.Value
        if bt_value == 1:
            toggle_button.config(text="ON", bg="green")
            ledButton.config(bg="green")

        else:
            toggle_button.config(text="OFF", bg="gray78")

            ledButton.config(bg="red")
    runtime_frame.after(1000, update_values_runtime)

def update_values_production():
    # Update the button state here for runtime
    with PLC() as comm:
        comm.IPAddress = '192.168.10.10'
        value = comm.Read('AlwaysOn')
        bt_value = value.Value
        if bt_value == 1:
            toggle_buttonp.config(text="ON", bg="green")
            ledButtonp.config(bg="green")

        else:
            toggle_buttonp.config(text="OFF", bg="gray78")

            ledButtonp.config(bg="red")
    # production_frame.after(1000, update_values_production)


toggle_state = False

def Simpletoggle():  # defining function to change the state of the button on runtime window
    global toggle_state, tag_value
    toggle_state = not toggle_state
    if toggle_state:
        toggle_button.config(text="ON", bg="green")
        ledButton.config(bg="green")
        tag_value = 1
    else:
        toggle_button.config(text="OFF", bg="gray78")
        ledButton.config(bg="red")
        tag_value = 0
    comm.Write('PY_StartBit1', tag_value)
    result = comm.Read('PY_StartBit1')
    if result == " ":
        print("error", tag_value)
    else:
        print("sucess", tag_value)


toggle_state1 = False

def simpletoggle():  # defining function to change the state of the button on production window

    global toggle_state1,tag_value_p
    toggle_state1 = not toggle_state1
    if toggle_state1:
        toggle_buttonp.config(text="ON", bg="green")
        ledButtonp.config(bg="green")
        tag_value_p = 1
    else:
        toggle_buttonp.config(text="OFF", bg="gray78")
        ledButtonp.config(bg="red")
        tag_value_p = 0
    comm.Write('AlwaysOn', tag_value_p)
    result = comm.Read('AlwaysOn')
    if result == " ":
        print("error", tag_value_p)
    else:
        print("sucess", tag_value_p)

def update_DataBase1(entry_Int):                   # creating excel sheet of the tag values
        tag_01 = entry_Int.get()
#         # create sql Database connection
#         conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',
#                               host='LAPTOP-9PH17G3B\SQLEXPRESS',
#                               database='plc_tags', trusted_connection='yes')
#         cursor = conn.cursor()
#         # cursor.execute("insert into Table_01(date_time,tag_name,tag_value) values(?,?,?);", (time_string,'PY_real01',tag_01))
#         cursor.execute("insert into Table_1(tag_name,tag_value) values(?,?);", ('PY_real01', tag_01))
#         conn.commit()
        cursor = con.cursor()
        cursor.execute("INSERT INTO plc_tags (time_date,tag_name,tag_value ) VALUES (%s,%s,%s)", (time_string,'PY_real01',tag_01))
        con.commit()

#
def update_DataBase2(Entry_Int ):
        tag_02 = Entry_Int.get()
#         # create sql Database connection
#         conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',
#                               host='LAPTOP-9PH17G3B\SQLEXPRESS',
#                               database='plc_tag', trusted_connection='yes')
#         cursor = conn.cursor()
#         cursor.execute("insert into Table_1(tag_name,tag_value) values(?,?);", ('PY_real03',tag_02))
#         conn.commit()
        cursor = con.cursor()
        cursor.execute("INSERT INTO plc_tags (time_date,tag_name,tag_value ) VALUES (%s,%s,%s)", (time_string,'PY_real03',tag_02))
        con.commit()


comm.Close()
root.mainloop()
con.close()
