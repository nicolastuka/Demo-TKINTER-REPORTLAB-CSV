from ui.UIManager import window, ConfigWindow, CreateList, CreateOptionButtons
from data.ControlData import LoadDataFromCSV

ConfigWindow(800, 600)

headers, data = LoadDataFromCSV("data/students.csv")

CreateList(headers, data)

CreateOptionButtons()

window.mainloop()
