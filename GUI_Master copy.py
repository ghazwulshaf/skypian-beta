from tkinter import *
from tkinter import messagebox
import threading

fontSize = 18

class RootGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Skypian Beta")
        self.root.geometry("%dx%d" % (800, 480))
        self.root.config(bg="white")
        self.root.resizable(False, False)

class MasterGUI():
    def __init__(self, root, serial, data, sensor):
        self.root = root
        self.serial = serial
        self.data = data
        self.sensor = sensor

        self.padX = 20

        self.ComGUI()

        self.publish()
    
    def ComGUI(self):
        self.frm_com = LabelFrame(self.root, text="Com Manager", bg="white", padx=2, pady=2)

        self.lbl_com = Label(self.frm_com, text="Available Port(s): ", bg="white", anchor="w")
        self.lbl_bd = Label(self.frm_com, text="Baud Rate: ", bg="white", anchor="w")

        self.ComOptionMenu()
        self.BaudOptionMenu()

        self.btn_refresh = Button(self.frm_com, text="Refresh", width=10, command=self.refresh)
        self.btn_connect = Button(self.frm_com, text="Connect", width=10, command=self.connect, state="disabled")

    def ComOptionMenu(self):
        coms = ["-"]
        self.clicked_com = StringVar()
        self.clicked_com.set(coms[0])
        self.drop_com = OptionMenu(self.frm_com, self.clicked_com, *coms, command=self.connect_ctrl)
        self.drop_com.config(width=10)
    
    def BaudOptionMenu(self):
        bds = ["-",
               "300",
               "600",
               "1200",
               "2400",
               "4800",
               "9600",
               "14400",
               "19200",
               "28800",
               "38400",
               "56000",
               "57600",
               "115200",
               "128000",
               "256000"]
        self.clicked_bd = StringVar()
        self.clicked_bd.set(bds[0])
        self.drop_baud = OptionMenu(self.frm_com, self.clicked_bd, *bds, command=self.connect_ctrl)
        self.drop_baud.config(width=10)
        
    def connect_ctrl(self, widget):
        """Method to control connect button and get com and baudrate"""
        print()
        print("COM: " + self.clicked_com.get())
        print("Baud: " + self.clicked_bd.get())

        if "-" in self.clicked_com.get() or "-" in self.clicked_bd.get():
            self.btn_connect["state"] = "disable"
        else:
            self.btn_connect["state"] = "active"
    
    def refresh(self):
        self.serial.getCOMList()
        coms = self.serial.com_list

        print()
        print(self.serial.com_list)

        self.clicked_com.set(coms[0])
        self.drop_com.destroy()
        self.drop_com = OptionMenu(self.frm_com, self.clicked_com, *coms, command=self.connect_ctrl)
        self.drop_com.config(width=10)
        self.drop_com.grid(column=2, row=0, padx=self.padX)

    def connect(self):
        if self.btn_connect["text"] in "Connect":
            self.serial.SerialOpen(self)
            if self.serial.ser.status:
                self.btn_connect["text"] = "Disconnect"
                self.btn_refresh["state"] = "disable"
                self.drop_com["state"] = "disable"
                self.drop_baud["state"] = "disable"
                InfoMsg = f"Successful UART connection using {self.clicked_com.get()}"
                messagebox.showinfo("showinfo", InfoMsg)

                self.frm_com.destroy()

                self.start_stream()
            else:
                ErrorMsg = f"Failure to estabish UART connection using {self.clicked_com.get()}"
                messagebox.showerror("showerror", ErrorMsg)
        else:
            self.serial.SerialClose()
            self.stop_stream()
            InfoMsg = f"UART connection using {self.clicked_com.get()} is now closed"
            messagebox.showwarning("showinfo", InfoMsg)
            self.btn_connect["text"] = "Connect"
            self.btn_refresh["state"] = "active"
            self.drop_com["state"] = "active"
            self.drop_baud["state"] = "active"

    def start_stream(self):
        self.serial.t1 = threading.Thread(target=self.serial.SerialDataStream, args=(self,), daemon=True)
        self.serial.t1.start()

        self.sensor.t2 = threading.Thread(target=self.sensor.UpdateText, args=(self.data,), daemon=True)
        self.sensor.t2.start()
    
    def stop_stream(self):
        self.serial.t1.stop()
    
    def DataGUI(self):
        self.frm_data = Frame(self.root, bg="white")

        self.height_data = self.frm_data.winfo_height()
        self.width_data = self.frm_data.winfo_width()

        self.frm_data.rowconfigure([0,1,2,3,4,5], minsize=self.height_data/6, weight=1)
        self.frm_data.columnconfigure([0,1], minsize=self.width_data/2, weight=1)

    def SensorGUI(self):
        frm_s = LabelFrame(self.frm_data, text="Sensors", labelanchor="n", bg="white", padx=2, pady=2)

        self.height = frm_s.winfo_height()
        self.width = frm_s.winfo_width()

        frm_s.rowconfigure([0,1,2], minsize=self.height/3, weight=1)
        frm_s.columnconfigure([0,1,2], minsize=self.width/3, weight=1)

        self.frm_s1 = LabelFrame(frm_s, text=self.data.nm_s1, labelanchor="n", bg="white", padx=2, pady=2)
        self.frm_s2 = LabelFrame(frm_s, text=self.data.nm_s2, labelanchor="n", bg="white", padx=2, pady=2)
        self.frm_s3 = LabelFrame(frm_s, text=self.data.nm_s3, labelanchor="n", bg="white", padx=2, pady=2)
        self.frm_s4 = LabelFrame(frm_s, text=self.data.nm_s4, labelanchor="n", bg="white", padx=2, pady=2)
        self.frm_s5 = LabelFrame(frm_s, text=self.data.nm_s5, labelanchor="n", bg="white", padx=2, pady=2)
        self.frm_s6 = LabelFrame(frm_s, text=self.data.nm_s6, labelanchor="n", bg="white", padx=2, pady=2)
        self.frm_s7 = LabelFrame(frm_s, text=self.data.nm_s7, labelanchor="n", bg="white", padx=2, pady=2)

        self.lbl_s1 = Label(self.frm_s1, text=self.data.DataSensor[1], font=("Arial", fontSize), bg="white", anchor="center")
        self.lbl_s2 = Label(self.frm_s2, text=self.data.DataSensor[2], font=("Arial", fontSize), bg="white", anchor="center")
        self.lbl_s3 = Label(self.frm_s3, text=self.data.DataSensor[2], font=("Arial", fontSize), bg="white", anchor="center")
        self.lbl_s4 = Label(self.frm_s4, text=self.data.DataSensor[2], font=("Arial", fontSize), bg="white", anchor="center")
        self.lbl_s5 = Label(self.frm_s5, text=self.data.DataSensor[2], font=("Arial", fontSize), bg="white", anchor="center")
        self.lbl_s6 = Label(self.frm_s6, text=self.data.DataSensor[2], font=("Arial", fontSize), bg="white", anchor="center")
        self.lbl_s7 = Label(self.frm_s7, text=self.data.DataSensor[2], font=("Arial", fontSize), bg="white", anchor="center")
    
    def publish(self):
        #region Com GUI
        self.frm_com.pack(anchor="w", padx=5, pady=5)

        self.lbl_com.grid(column=1, row=0)
        self.drop_com.grid(column=2, row=0, padx=self.padX)

        self.lbl_bd.grid(column=3, row=0)
        self.drop_baud.grid(column=4, row=0, padx=self.padX)

        self.btn_refresh.grid(column=5, row=0, padx=2)
        self.btn_connect.grid(column=6, row=0, padx=2)
        #endregion Com GUI

        #region Data GUI
        self.frm_data.pack(fill="both", expand=True, padx=5, pady=5)

        #region Sensor GUI
        self.frm_s.grid(row=0, column=0, rowspan=5, sticky="news", padx=2, pady=2)

        self.frm_s1.grid(row=0, column=0, sticky="news", padx=2, pady=2)
        self.frm_s2.grid(row=0, column=1, sticky="news", padx=2, pady=2)
        self.frm_s3.grid(row=1, column=0, sticky="news", padx=2, pady=2)
        self.frm_s4.grid(row=1, column=1, sticky="news", padx=2, pady=2)
        self.frm_s5.grid(row=2, column=0, sticky="news", padx=2, pady=2)
        self.frm_s6.grid(row=2, column=1, sticky="news", padx=2, pady=2)
        self.frm_s7.grid(row=0, column=2, rowspan=2, sticky="news", padx=2, pady=2)

        self.lbl_s1.pack(fill="both", expand="true")
        self.lbl_s2.pack(fill="both", expand="true")
        self.lbl_s3.pack(fill="both", expand="true")
        self.lbl_s4.pack(fill="both", expand="true")
        self.lbl_s5.pack(fill="both", expand="true")
        self.lbl_s6.pack(fill="both", expand="true")
        self.lbl_s7.pack(fill="both", expand="true")
        #endregion Sensor GUI
        #endregion Data GUI
    
    def UpdateSensorText(self, data):
        self.lbl_s1["text"] = data.DataSensor[1]
        self.lbl_s2["text"] = data.DataSensor[2]
        self.lbl_s3["text"] = data.DataSensor[3]
        self.lbl_s4["text"] = data.DataSensor[4]
        self.lbl_s5["text"] = data.DataSensor[5]
        self.lbl_s6["text"] = data.DataSensor[6]
        self.lbl_s7["text"] = data.DataSensor[7]

# class DataGUI():
#     def __init__(self, root):
#         self.root = root
#         self.frame = Frame(root, bg="white")

#         self.height = self.frame.winfo_height()
#         self.width = self.frame.winfo_width()

#         self.frame.rowconfigure([0,1,2,3,4,5], minsize=self.height/6, weight=1)
#         self.frame.columnconfigure([0,1], minsize=self.width/2, weight=1)

#         self.publish()
    
#     def publish(self):
#         self.frame.pack(fill="both", expand=True, padx=5, pady=5)

class SensorGUI():
    def __init__(self, root, data):
        frm_s = LabelFrame(frm_data, text="Sensors", labelanchor="n", bg="white", padx=2, pady=2)

        self.height = frm_s.winfo_height()
        self.width = frm_s.winfo_width()

        frm_s.rowconfigure([0,1,2], minsize=self.height/3, weight=1)
        frm_s.columnconfigure([0,1,2], minsize=self.width/3, weight=1)

        self.frm_s1 = LabelFrame(frm_s, text=data.nm_s1, labelanchor="n", bg="white", padx=2, pady=2)
        self.frm_s2 = LabelFrame(frm_s, text=data.nm_s2, labelanchor="n", bg="white", padx=2, pady=2)
        self.frm_s3 = LabelFrame(frm_s, text=data.nm_s3, labelanchor="n", bg="white", padx=2, pady=2)
        self.frm_s4 = LabelFrame(frm_s, text=data.nm_s4, labelanchor="n", bg="white", padx=2, pady=2)
        self.frm_s5 = LabelFrame(frm_s, text=data.nm_s5, labelanchor="n", bg="white", padx=2, pady=2)
        self.frm_s6 = LabelFrame(frm_s, text=data.nm_s6, labelanchor="n", bg="white", padx=2, pady=2)
        self.frm_s7 = LabelFrame(frm_s, text=data.nm_s7, labelanchor="n", bg="white", padx=2, pady=2)

        self.lbl_s1 = Label(self.frm_s1, text=self.data.DataSensor[1], font=("Arial", fontSize), bg="white", anchor="center")
        self.lbl_s2 = Label(self.frm_s2, text=self.data.DataSensor[2], font=("Arial", fontSize), bg="white", anchor="center")
        self.lbl_s3 = Label(self.frm_s3, text=self.data.DataSensor[2], font=("Arial", fontSize), bg="white", anchor="center")
        self.lbl_s4 = Label(self.frm_s4, text=self.data.DataSensor[2], font=("Arial", fontSize), bg="white", anchor="center")
        self.lbl_s5 = Label(self.frm_s5, text=self.data.DataSensor[2], font=("Arial", fontSize), bg="white", anchor="center")
        self.lbl_s6 = Label(self.frm_s6, text=self.data.DataSensor[2], font=("Arial", fontSize), bg="white", anchor="center")
        self.lbl_s7 = Label(self.frm_s7, text=self.data.DataSensor[2], font=("Arial", fontSize), bg="white", anchor="center")

        self.publish()

    def publish(self):
        self.frm_s.grid(row=0, column=0, rowspan=5, sticky="news", padx=2, pady=2)

        self.frm_s1.grid(row=0, column=0, sticky="news", padx=2, pady=2)
        self.frm_s2.grid(row=0, column=1, sticky="news", padx=2, pady=2)
        self.frm_s3.grid(row=1, column=0, sticky="news", padx=2, pady=2)
        self.frm_s4.grid(row=1, column=1, sticky="news", padx=2, pady=2)
        self.frm_s5.grid(row=2, column=0, sticky="news", padx=2, pady=2)
        self.frm_s6.grid(row=2, column=1, sticky="news", padx=2, pady=2)
        self.frm_s7.grid(row=0, column=2, rowspan=2, sticky="news", padx=2, pady=2)

        self.lbl_s1.pack(fill="both", expand="true")
        self.lbl_s2.pack(fill="both", expand="true")
        self.lbl_s3.pack(fill="both", expand="true")
        self.lbl_s4.pack(fill="both", expand="true")
        self.lbl_s5.pack(fill="both", expand="true")
        self.lbl_s6.pack(fill="both", expand="true")
        self.lbl_s7.pack(fill="both", expand="true")
    
    def UpdateText(self, data):
        self.lbl_s1["text"] = data.DataSensor[1]
        self.lbl_s2["text"] = data.DataSensor[2]
        self.lbl_s3["text"] = data.DataSensor[3]
        self.lbl_s4["text"] = data.DataSensor[4]
        self.lbl_s5["text"] = data.DataSensor[5]
        self.lbl_s6["text"] = data.DataSensor[6]
        self.lbl_s7["text"] = data.DataSensor[7]

class GraphGUI():
    def __init__(self, root, data):
        self.root = root
        self.data = data

        self.frame = LabelFrame(root, text="Graph", labelanchor="n", bg="white", padx=2, pady=2)

        self.height = self.frame.winfo_height()
        self.width = self.frame.winfo_width()

        self.frame.rowconfigure([0,1,2,3,4], minsize=self.height/5, weight=1)
        self.frame.columnconfigure(0, weight=1)

        self.frm_gp = Frame(self.frame, bg="white", highlightbackground="grey", highlightthickness=1)
        self.frm_btn = Frame(self.frame, bg="white")

        self.frm_btn_height = self.frm_btn.winfo_height()
        self.frm_btn_width = self.frm_btn.winfo_width()

        self.frm_btn.rowconfigure([0,1], minsize=self.frm_btn_height/2, weight=1)
        self.frm_btn.columnconfigure([0,1], minsize=self.frm_btn_width/2, weight=1)
        
        self.btn_gp1 = Button(self.frm_btn, text=self.data.nm_gp1)
        self.btn_gp2 = Button(self.frm_btn, text=self.data.nm_gp2)
        self.btn_gp3 = Button(self.frm_btn, text=self.data.nm_gp3)
        self.btn_gp4 = Button(self.frm_btn, text=self.data.nm_gp4)

        self.publish()

    def publish(self):
        self.frame.grid(row=0, column=1, rowspan=5, sticky="news", padx=2, pady=2)

        self.frm_gp.grid(row=0, column=0, rowspan=4, sticky="news", padx=2, pady=2)
        self.frm_btn.grid(row=4, column=0, sticky="news")

        self.btn_gp1.grid(row=0, column=0, sticky="news", padx=2, pady=2)
        self.btn_gp2.grid(row=0, column=1, sticky="news", padx=2, pady=2)
        self.btn_gp3.grid(row=1, column=0, sticky="news", padx=2, pady=2)
        self.btn_gp4.grid(row=1, column=1, sticky="news", padx=2, pady=2)

class ActuatorGUI():
    def __init__(self, root, data):
        self.root = root
        self.data = data

        self.frame = LabelFrame(root, text="Actuators", labelanchor="n", bg="white", padx=2, pady=2)

        self.height = self.frame.winfo_height()
        self.width = self.frame.winfo_width()

        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure([0,1], minsize=self.width/2, weight=1)

        self.btn_ac1 = Button(self.frame, text=(self.data.nm_ac1 + ": " + self.data.st_ac1))
        self.btn_ac2 = Button(self.frame, text=(self.data.nm_ac2 + ": " + self.data.st_ac2))

        self.publish()

    def publish(self):
        self.frame.grid(row=5, column=0, sticky="news", padx=2, pady=2)

        self.btn_ac1.grid(row=0, column=0, sticky="news", padx=2, pady=2)
        self.btn_ac2.grid(row=0, column=1, sticky="news", padx=2, pady=2)

class ActionGUI():
    def __init__(self, root, data):
        self.root = root
        self.data = data

        self.frame = LabelFrame(root, text="Actions", labelanchor="n", bg="white", padx=2, pady=2)

        self.height = self.frame.winfo_height()
        self.width = self.frame.winfo_width()

        self.frame.rowconfigure([0,1], minsize=self.height/2, weight=1)
        self.frame.columnconfigure([0,1], minsize=self.width/2, weight=1)

        self.btn_act1 = Button(self.frame, text=(self.data.nm_act1 + ": " + self.data.st_act1))
        self.btn_act2 = Button(self.frame, text=self.data.nm_act2)
        self.btn_act3 = Button(self.frame, text=self.data.nm_act3)

        self.publish()

    def publish(self):
        self.frame.grid(row=5, column=1, sticky="news", padx=2, pady=2)

        self.btn_act1.grid(row=0, column=0, rowspan=2, sticky="news", padx=2, pady=2)
        self.btn_act2.grid(row=0, column=1, sticky="news", padx=2, pady=2)
        self.btn_act3.grid(row=1, column=1, sticky="news", padx=2, pady=2)

if __name__ == "__main__":
    RootGUI()
    ComGUI()
    DataGUI()
    SensorGUI()
    GraphGUI()
    ActuatorGUI()
    ActionGUI()