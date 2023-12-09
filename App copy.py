from GUI_Master import *

RootMaster = RootGUI()

SensorMaster = SensorGUI(RootMaster.root)
GraphMaster = GraphGUI(RootMaster.root)
ActuatorMaster = ActuatorGUI(RootMaster.root)
ActionMaster = ActionGUI(RootMaster.root)

RootMaster.root.mainloop()