from GUI_Master import RootGUI, MasterGUI
from Serial_Master import SerialCtrl
from Data_Master import DataCtrl

MyData = DataCtrl()
MySerial = SerialCtrl()

GUI_ROOT = RootGUI()
GUI_MASTER = MasterGUI(GUI_ROOT.root, MySerial, MyData)

GUI_ROOT.root.mainloop()