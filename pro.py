import tkinter as tk
import tkinter.ttk as ttk
import data
from tkinter import messagebox
from graph import *

window = tk.Tk()

#region window configuration
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

def fullscreen(state):
    global window
    global width
    global height

    if state:
        window.attributes('-fullscreen', True)
    else:
        width = 800
        height = 480
        window.configure(width=width, height=height)
        window.resizable(False, False)

fullscreen(True)

width2 = width/2
height2 = height/2
width4 = width/4
height4 = height/4

window.rowconfigure([0,1,2,3], minsize=height4, weight=1)
window.columnconfigure([0,1], minsize=width2, weight=1)
#endregion window configuration

#region variable component configuration
width_label = 6
width_on_off = 4
width_action = 5
#endregion variable component configuration

#region dialogue
def harvest():
    dlg_harvest = messagebox.askyesno(title='Harvest', message='Are you sure you want to reset data?', parent=window, icon='warning')
    if dlg_harvest:
        pass

def exit():
    dlg_exit = messagebox.askyesno(title='Exit', message='Are you sure you want to close GUI?', parent=window, icon='warning')
    if dlg_exit:
        window.destroy()
#endregion dialogue

#region sensors
frm_sensors = tk.Frame(window, bg='yellow', padx=5, pady=5)
frm_sensors.grid(row=0, rowspan=3, column=0, sticky='news')
frm_sensors.rowconfigure([0,1,2], weight=1)
frm_sensors.columnconfigure([0,1,2], weight=1)

#region sensor 1
frm_sensor1 = tk.Frame(frm_sensors, bg='white')
frm_sensor1.grid(row=0, column=0, sticky='news', padx=5, pady=5)

lbl_sensor1Title = tk.Label(frm_sensor1, fg='black', bg='white', text='Sensor 1', font=('Arial', 12))
lbl_sensor1Title.pack()

lbl_sensor1Value = tk.Label(frm_sensor1, fg='black', bg='white', text='0', font=('Arial', 36))
lbl_sensor1Value.pack()

lbl_sensor1Unit = tk.Label(frm_sensor1, fg='black', bg='white', text='%sC' % (chr(176)), font=('Arial', 12))
lbl_sensor1Unit.pack()
#endregion sensor 1

#region sensor 2
frm_sensor2 = tk.Frame(frm_sensors, bg='white')
frm_sensor2.grid(row=0, column=1, sticky='news', padx=5, pady=5)

lbl_sensor2Title = tk.Label(frm_sensor2, fg='black', bg='white', text='Sensor 2', font=('Arial', 12))
lbl_sensor2Title.pack()

lbl_sensor2Value = tk.Label(frm_sensor2, fg='black', bg='white', text='0', font=('Arial', 36))
lbl_sensor2Value.pack()

lbl_sensor2Unit = tk.Label(frm_sensor2, fg='black', bg='white', text='%sC' % (chr(176)), font=('Arial', 12))
lbl_sensor2Unit.pack()
#endregion sensor 2

#region sensor 3
frm_sensor3 = tk.Frame(frm_sensors, bg='white')
frm_sensor3.grid(row=1, column=0, sticky='news', padx=5, pady=5)

lbl_sensor3Title = tk.Label(frm_sensor3, fg='black', bg='white', text='Sensor 3', font=('Arial', 12))
lbl_sensor3Title.pack()

lbl_sensor3Value = tk.Label(frm_sensor3, fg='black', bg='white', text='0', font=('Arial', 36))
lbl_sensor3Value.pack()

lbl_sensor3Unit = tk.Label(frm_sensor3, fg='black', bg='white', text='%sC' % (chr(176)), font=('Arial', 12))
lbl_sensor3Unit.pack()
#endregion sensor 3

#region sensor 4
frm_sensor4 = tk.Frame(frm_sensors, bg='white')
frm_sensor4.grid(row=1, column=1, sticky='news', padx=5, pady=5)

lbl_sensor4Title = tk.Label(frm_sensor4, fg='black', bg='white', text='Sensor 4', font=('Arial', 12))
lbl_sensor4Title.pack()

lbl_sensor4Value = tk.Label(frm_sensor4, fg='black', bg='white', text='0', font=('Arial', 36))
lbl_sensor4Value.pack()

lbl_sensor4Unit = tk.Label(frm_sensor4, fg='black', bg='white', text='%sC' % (chr(176)), font=('Arial', 12))
lbl_sensor4Unit.pack()
#endregion sensor 4

#region sensor 5
frm_sensor5 = tk.Frame(frm_sensors, bg='white')
frm_sensor5.grid(row=2, column=0, sticky='news', padx=5, pady=5)

lbl_sensor5Title = tk.Label(frm_sensor5, fg='black', bg='white', text='Sensor 5', font=('Arial', 12))
lbl_sensor5Title.pack()

lbl_sensor5Value = tk.Label(frm_sensor5, fg='black', bg='white', text='0', font=('Arial', 36))
lbl_sensor5Value.pack()

lbl_sensor5Unit = tk.Label(frm_sensor5, fg='black', bg='white', text='%sC' % (chr(176)), font=('Arial', 12))
lbl_sensor5Unit.pack()
#endregion sensor 5

#region sensor 6
frm_sensor6 = tk.Frame(frm_sensors, bg='white')
frm_sensor6.grid(row=2, column=1, sticky='news', padx=5, pady=5)

lbl_sensor6Title = tk.Label(frm_sensor6, fg='black', bg='white', text='Sensor 6', font=('Arial', 12))
lbl_sensor6Title.pack()

lbl_sensor6Value = tk.Label(frm_sensor6, fg='black', bg='white', text='0', font=('Arial', 36))
lbl_sensor6Value.pack()

lbl_sensor6Unit = tk.Label(frm_sensor6, fg='black', bg='white', text='%sC' % (chr(176)), font=('Arial', 12))
lbl_sensor6Unit.pack()
#endregion sensor 6

#region sensor 7
frm_sensor7 = tk.Frame(frm_sensors, bg='white')
frm_sensor7.grid(row=0, rowspan=3, column=2, sticky='news', padx=5, pady=5)

lbl_sensor7Title = tk.Label(frm_sensor7, fg='black', bg='white', text='Sensor 7', font=('Arial', 12))
lbl_sensor7Title.pack()

lbl_sensor7Value = tk.Label(frm_sensor7, fg='black', bg='white', text='0', font=('Arial', 36))
lbl_sensor7Value.pack()

lbl_sensor7Unit = tk.Label(frm_sensor7, fg='black', bg='white', text='%sC' % (chr(176)), font=('Arial', 12))
lbl_sensor7Unit.pack()
#endregion sensor 7
#endregion sensors

#region graphs
frm_graphs = tk.Frame(window, bg='blue', padx=5, pady=5)
frm_graphs.grid(row=0, rowspan=3, column=1, sticky='news')
frm_graphs.rowconfigure([0,1,2,3], weight=1)
frm_graphs.columnconfigure(0, weight=1)

#region graph
frm_graph = tk.Frame(frm_graphs, bg='white')
frm_graph.grid(row=0, rowspan=3, column=0, sticky='news', padx=5, pady=5)

frm_plot = tk.Frame(frm_graph, bg='white')
frm_plot.pack(fill='both', expand=True)

stt_graph = 0
plot0(frm_plot)

def plotGraph(num):
    global frm_graph
    global frm_plot
    global stt_graph

    if num == stt_graph:
        frm_plot.destroy()
        frm_plot = tk.Frame(frm_graph, bg='white')
        frm_plot.pack(fill='both', expand=True)
        stt_graph = 0
        plot0(frm_plot)
    else:
        frm_plot.destroy()
        frm_plot = tk.Frame(frm_graph, bg='white')
        frm_plot.pack(fill='both', expand=True)
        stt_graph = num
        if num == 1: plot1(frm_plot)
        elif num == 2: plot2(frm_plot)
        elif num == 3: plot1(frm_plot)
        elif num == 4: plot2(frm_plot)

def plotGraph1():
    plotGraph(1)

def plotGraph2():
    plotGraph(2)

def plotGraph3():
    plotGraph(3)

def plotGraph4():
    plotGraph(4)
#endregion graph

#region tabs
frm_tabs = tk.Frame(frm_graphs, bg='blue')
frm_tabs.grid(row=3, column=0, sticky='news')
frm_tabs.rowconfigure([0,1], weight=1)
frm_tabs.columnconfigure([0,1], weight=1)

#region tab graph 1
frm_tab1 = tk.Frame(frm_tabs, bg='white')
frm_tab1.grid(row=0, column=0, sticky='news', padx=5, pady=5)

btn_tab1 = tk.Button(frm_tab1, text='Graph 1', fg='black', font=('Arial', 16), command=plotGraph1)
btn_tab1.pack(fill='both', expand=True)
#endregion tab graph 1

#region tab graph 2
frm_tab2 = tk.Frame(frm_tabs, bg='white')
frm_tab2.grid(row=0, column=1, sticky='news', padx=5, pady=5)

btn_tab2 = tk.Button(frm_tab2, text='Graph 2', fg='black', font=('Arial', 16), command=plotGraph2)
btn_tab2.pack(fill='both', expand=True)
#endregion tab graph 2

#region tab graph 3
frm_tab3 = tk.Frame(frm_tabs, bg='white')
frm_tab3.grid(row=1, column=0, sticky='news', padx=5, pady=5)

btn_tab3 = tk.Button(frm_tab3, text='Graph 3', fg='black', font=('Arial', 16), command=plotGraph3)
btn_tab3.pack(fill='both', expand=True)
#endregion tab graph 3

#region tab graph 4
frm_tab4 = tk.Frame(frm_tabs, bg='white')
frm_tab4.grid(row=1, column=1, sticky='news', padx=5, pady=5)

btn_tab4 = tk.Button(frm_tab4, text='Graph 4', fg='black', font=('Arial', 16), command=plotGraph4)
btn_tab4.pack(fill='both', expand=True)
#endregion tab graph 4
#endregion tabs
#endregion graphs

#region actuators
frm_actuators = tk.Frame(window, bg='red', padx=5, pady=5)
frm_actuators.grid(row=3, column=0, sticky='news')
frm_actuators.rowconfigure([0,1], weight=1)
frm_actuators.columnconfigure(0, weight=1)

#region actuator 1
stt_actuator1 = 'OFF'

def setActuator1():
    global stt_actuator1
    global btn_actuator1

    if stt_actuator1 == 'OFF':
        stt_actuator1 = 'ON'
    elif stt_actuator1 == 'ON':
        stt_actuator1 = 'OFF'
    
    btn_actuator1.configure(text=stt_actuator1)

frm_actuator1 = tk.Frame(frm_actuators, bg='red')
frm_actuator1.grid(row=0, column=0, sticky='news', pady=5)
frm_actuator1.rowconfigure(0, weight=1)
frm_actuator1.columnconfigure([0,1,2], weight=1)

frm_actuator1Label = tk.Frame(frm_actuator1, bg='white', width=width_label)
frm_actuator1Label.grid(row=0, column=0, columnspan=2, sticky='news', padx=5)

lbl_actuator1 = tk.Label(frm_actuator1Label, text='Aktuator 1', fg='black', bg='white', font=('Arial', 16))
lbl_actuator1.place(anchor='center', relwidth=1, relheight=1, relx=.5, rely=.5)

frm_actuator1Button = tk.Frame(frm_actuator1, bg='white')
frm_actuator1Button.grid(row=0, column=2, sticky='news', padx=5)

btn_actuator1 = tk.Button(frm_actuator1Button, text=stt_actuator1, fg='black', font=('Arial', 16), width=width_on_off, command=setActuator1)
btn_actuator1.pack(fill='both', expand=True)
#endregion actuator 1

#region actuator 2
stt_actuator2 = 'OFF'

def setActuator2():
    global stt_actuator2
    global btn_actuator2

    if stt_actuator2 == 'OFF':
        stt_actuator2 = 'ON'
    elif stt_actuator2 == 'ON':
        stt_actuator2 = 'OFF'
    
    btn_actuator2.configure(text=stt_actuator2)

frm_actuator2 = tk.Frame(frm_actuators, bg='red')
frm_actuator2.grid(row=1, column=0, sticky='news', pady=5)
frm_actuator2.rowconfigure(0, weight=1)
frm_actuator2.columnconfigure([0,1,2], weight=1)

frm_actuator2Label = tk.Frame(frm_actuator2, bg='white', width=width_label)
frm_actuator2Label.grid(row=0, column=0, columnspan=2, sticky='news', padx=5)

lbl_actuator2 = tk.Label(frm_actuator2Label, text='Aktuator 2', fg='black', bg='white', font=('Arial', 16))
lbl_actuator2.place(anchor='center', relwidth=1, relheight=1, relx=.5, rely=.5)

frm_actuator2Button = tk.Frame(frm_actuator2, bg='white')
frm_actuator2Button.grid(row=0, column=2, sticky='news', padx=5)

btn_actuator2 = tk.Button(frm_actuator2Button, text='OFF', fg='black', font=('Arial', 16), width=width_on_off, command=setActuator2)
btn_actuator2.pack(fill='both', expand=True)
#endregion actuator 2
#endregion actuators

#region actions
frm_actions = tk.Frame(window, bg='green', padx=5, pady=5)
frm_actions.grid(row=3, column=1, sticky='news')
frm_actions.rowconfigure([0,1], weight=1)
frm_actions.columnconfigure(0, weight=1)

#region action 1
stt_action1 = 'OFF'

def setAction1():
    global stt_action1
    global btn_action1

    if stt_action1 == 'OFF':
        stt_action1 = 'ON'
    elif stt_action1 == 'ON':
        stt_action1 = 'OFF'
    
    btn_action1.configure(text=stt_action1)

frm_action1 = tk.Frame(frm_actions, bg='green')
frm_action1.grid(row=0, column=0, sticky='news', pady=5)
frm_action1.rowconfigure(0, weight=1)
frm_action1.columnconfigure([0,1,2], weight=1)

frm_action1Label = tk.Frame(frm_action1, bg='white', width=width_label)
frm_action1Label.grid(row=0, column=0, columnspan=2, sticky='news', padx=5)

lbl_action1 = tk.Label(frm_action1Label, text='Aksi 1', fg='black', bg='white', font=('Arial', 16))
lbl_action1.place(anchor='center', relwidth=1, relheight=1, relx=.5, rely=.5)

frm_action1Button = tk.Frame(frm_action1, bg='white')
frm_action1Button.grid(row=0, column=2, sticky='news', padx=5)

btn_action1 = tk.Button(frm_action1Button, text='OFF', fg='black', font=('Arial', 16), width=width_on_off, command=setAction1)
btn_action1.pack(fill='both', expand=True)
#endregion action 1

#region action 2
frm_action2 = tk.Frame(frm_actions, bg='green')
frm_action2.grid(row=1, column=0, sticky='news', pady=5)
frm_action2.rowconfigure(0, weight=1)
frm_action2.columnconfigure([0,1], weight=1)

#region harvest button
frm_harvest = tk.Frame(frm_action2, bg='orange')
frm_harvest.grid(row=0, column=0, sticky='news', padx=5)

btn_harvest = tk.Button(frm_harvest, text='Harvest', font=('Arial', 16), width=width_action, command=harvest)
btn_harvest.pack(fill='both', expand=True)
#endregion harvest button

#region exit button
frm_exit = tk.Frame(frm_action2, bg='orange')
frm_exit.grid(row=0, column=1, sticky='news', padx=5)

btn_exit = tk.Button(frm_exit, text='Exit', font=('Arial', 16), width=width_action, command=exit)
btn_exit.pack(fill='both', expand=True)
#endregion exit button
#endregion action 2
#endregion actions

window.mainloop()