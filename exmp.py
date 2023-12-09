import csv
import pandas as pd

filename = "data_sensor.csv"

df = pd.read_csv(filename)
datas = df.tail(120)

hour = datas["Hour"]
minute = datas["Minute"]

xList = []
for i in range(len(datas)):
    x = float(hour[i]) + (float(minute[i]) / 60.0)
    xList.append(x)

y1List = datas["pH"]
y2List = datas["TDS"]
y3List = datas["Humidity"]
y4List = datas["Heat Index"]
y5List = datas["Water Temp"]
y6List = datas["Air Temp"]
y7List = datas["Fert Level"]

print(y1List)