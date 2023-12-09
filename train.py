import tkinter as tk

window = tk.Tk()

# width = window.winfo_screenwidth()
# height = window.winfo_screenheight()

width = 800
height = 480
width2 = 800/2
height2 = 480/2

# w = 121.0
# h = 76.0
# width = '%fm' % (w)
# height = '%fm' % (h)
# width2 = '%fm' % (w/2.0)
# height2 = '%fm' % (h/2.0)

# window.attributes('-fullscreen', True)
# window.geometry('%dx%d' % (width, height))
window.configure(width=width, height=height)
window.resizable(False, False)


window.rowconfigure([0, 1], minsize=height2, weight=1)
window.columnconfigure([0, 1], minsize=width2, weight=1)

# region sensors
frm_sensors = tk.Frame(window, bg='yellow', padx=5, pady=5)
frm_sensors.grid(row=0, column=0, sticky='news')
frm_sensors.rowconfigure([0,1], weight=1)
frm_sensors.columnconfigure([0,1,2], weight=1)

frm_sensor1 = tk.Frame(frm_sensors, bg='white')
frm_sensor1.grid(row=0, column=0, sticky='news', padx=5, pady=5)

frm_sensor2 = tk.Frame(frm_sensors, bg='white')
frm_sensor2.grid(row=0, column=1, sticky='news', padx=5, pady=5)

frm_sensor3 = tk.Frame(frm_sensors, bg='white')
frm_sensor3.grid(row=0, column=2, sticky='news', padx=5, pady=5)

frm_sensor4 = tk.Frame(frm_sensors, bg='white')
frm_sensor4.grid(row=1, column=0, sticky='news', padx=5, pady=5)

frm_sensor5 = tk.Frame(frm_sensors, bg='white')
frm_sensor5.grid(row=1, column=1, sticky='news', padx=5, pady=5)

frm_sensor6 = tk.Frame(frm_sensors, bg='white')
frm_sensor6.grid(row=1, column=2, sticky='news', padx=5, pady=5)
# endregion sensors

# region graphs
frm_graphs = tk.Frame(window, bg='blue', padx=5, pady=5)
frm_graphs.grid(row=0, column=1, sticky='news')
frm_graphs.rowconfigure(0, weight=1)
frm_graphs.columnconfigure([0,1,2], weight=1)

frm_graph = tk.Frame(frm_graphs, bg='white')
frm_graph.grid(row=0, column=0, columnspan=2, sticky='news', padx=5, pady=5)

frm_tabs = tk.Frame(frm_graphs, bg='blue')
frm_tabs.grid(row=0, column=2, sticky='news', padx=5)
frm_tabs.rowconfigure([0,1,2,3], weight=1)
frm_tabs.columnconfigure(0, weight=1)

frm_tab1 = tk.Frame(frm_tabs, bg='white')
frm_tab1.grid(row=0, column=0, sticky='news', pady=5)

frm_tab2 = tk.Frame(frm_tabs, bg='white')
frm_tab2.grid(row=1, column=0, sticky='news', pady=5)

frm_tab3 = tk.Frame(frm_tabs, bg='white')
frm_tab3.grid(row=2, column=0, sticky='news', pady=5)

frm_tab4 = tk.Frame(frm_tabs, bg='white')
frm_tab4.grid(row=3, column=0, sticky='news', pady=5)
# endregion graphs

# region actuators
frm_actuators = tk.Frame(window, bg='red', padx=5, pady=5)
frm_actuators.grid(row=1, column=0, sticky='news')
frm_actuators.rowconfigure([0,1,2,3], weight=1)
frm_actuators.columnconfigure(0, weight=1)

# region actuator 1
frm_actuator1 = tk.Frame(frm_actuators, bg='orange')
frm_actuator1.grid(row=0, column=0, sticky='news', pady=5)
frm_actuator1.rowconfigure(0, weight=1)
frm_actuator1.columnconfigure([0,1,2], weight=1)

frm_actuator1Label = tk.Frame(frm_actuator1, bg='white')
frm_actuator1Label.grid(row=0, column=0, columnspan=2, sticky='news', padx=5)

frm_actuator1Button = tk.Frame(frm_actuator1, bg='white')
frm_actuator1Button.grid(row=0, column=2, sticky='news', padx=5)
# endregion actuator 1

# region actuator 2
frm_actuator2 = tk.Frame(frm_actuators, bg='orange')
frm_actuator2.grid(row=1, column=0, sticky='news', pady=5)
frm_actuator2.rowconfigure(0, weight=1)
frm_actuator2.columnconfigure([0,1,2], weight=1)

frm_actuator2Label = tk.Frame(frm_actuator2, bg='white')
frm_actuator2Label.grid(row=0, column=0, columnspan=2, sticky='news', padx=5)

frm_actuator2Button = tk.Frame(frm_actuator2, bg='white')
frm_actuator2Button.grid(row=0, column=2, sticky='news', padx=5)
# endregion actuator 2

# region actuator 3
frm_actuator3 = tk.Frame(frm_actuators, bg='orange')
frm_actuator3.grid(row=2, column=0, sticky='news', pady=5)
frm_actuator3.rowconfigure(0, weight=1)
frm_actuator3.columnconfigure([0,1,2], weight=1)

frm_actuator3Label = tk.Frame(frm_actuator3, bg='white')
frm_actuator3Label.grid(row=0, column=0, columnspan=2, sticky='news', padx=5)

frm_actuator3Button = tk.Frame(frm_actuator3, bg='white')
frm_actuator3Button.grid(row=0, column=2, sticky='news', padx=5)
# endregion actuator 3

# region actuator 4
frm_actuator4 = tk.Frame(frm_actuators, bg='orange')
frm_actuator4.grid(row=3, column=0, sticky='news', pady=5)
frm_actuator4.rowconfigure(0, weight=1)
frm_actuator4.columnconfigure([0,1,2], weight=1)

frm_actuator4Label = tk.Frame(frm_actuator4, bg='white')
frm_actuator4Label.grid(row=0, column=0, columnspan=2, sticky='news', padx=5)

frm_actuator4Button = tk.Frame(frm_actuator4, bg='white')
frm_actuator4Button.grid(row=0, column=2, sticky='news', padx=5)
# endregion actuator 4
# endregion actuators

# region actions
frm_actions = tk.Frame(window, bg='green', padx=5, pady=5)
frm_actions.grid(row=1, column=1, sticky='news')
frm_actions.rowconfigure([0,1,2,3], weight=1)
frm_actions.columnconfigure(0, weight=1)

# region action 1
frm_action1 = tk.Frame(frm_actions, bg='orange')
frm_action1.grid(row=0, column=0, sticky='news', pady=5)
frm_action1.rowconfigure(0, weight=1)
frm_action1.columnconfigure([0,1,2], weight=1)

frm_action1Label = tk.Frame(frm_action1, bg='white')
frm_action1Label.grid(row=0, column=0, columnspan=2, sticky='news', padx=5)

frm_action1Button = tk.Frame(frm_action1, bg='white')
frm_action1Button.grid(row=0, column=2, sticky='news', padx=5)
# endregion action 1

# region action 2
frm_action2 = tk.Frame(frm_actions, bg='orange')
frm_action2.grid(row=1, column=0, sticky='news', pady=5)
frm_action2.rowconfigure(0, weight=1)
frm_action2.columnconfigure([0,1,2], weight=1)

frm_action2Label = tk.Frame(frm_action2, bg='white')
frm_action2Label.grid(row=0, column=0, columnspan=2, sticky='news', padx=5)

frm_action2Button = tk.Frame(frm_action2, bg='white')
frm_action2Button.grid(row=0, column=2, sticky='news', padx=5)
# endregion action 2

# region action 3
frm_action3 = tk.Frame(frm_actions, bg='orange')
frm_action3.grid(row=2, column=0, sticky='news', pady=5)
frm_action3.rowconfigure(0, weight=1)
frm_action3.columnconfigure([0,1,2], weight=1)

frm_action3Label = tk.Frame(frm_action3, bg='white')
frm_action3Label.grid(row=0, column=0, columnspan=2, sticky='news', padx=5)

frm_action3Button = tk.Frame(frm_action3, bg='white')
frm_action3Button.grid(row=0, column=2, sticky='news', padx=5)
# endregion action 3

# region exit button
# frm_exit = tk.Frame(frm_actions, bg='orange')
# frm_exit.grid(row=3, column=0, sticky='news', pady=5)

# btn_exit = tk.Button(frm_exit, text='Exit', command=window.destroy)
# btn_exit.pack(fill='both', expand=True, padx=5)

btn_exit = tk.Button(frm_actions, text='Exit', command=window.destroy)
btn_exit.grid(row=3, column=0, sticky='ews', padx=5, pady=5)
# endregion exit button
# endregion actions

window.mainloop()