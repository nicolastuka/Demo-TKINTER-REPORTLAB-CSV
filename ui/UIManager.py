import tkinter as tk
from data.ControlData import SaveChangesData
from data.PDFExport import CreateReport

window = tk.Tk()
titleFrame = tk.Frame(window)
titleFrame.pack(expand=False, side="top")
mainFrame = tk.Frame(window)
mainFrame.pack(fill="both", expand=True, side="bottom")
headerFrame = tk.Frame(mainFrame)
headerFrame.pack(fill="both", expand=False)
dataFrame = tk.Frame(mainFrame)
dataFrame.pack(fill="both", expand=True)
buttonsFrame = tk.Frame(mainFrame)
buttonsFrame.pack(fill="both", expand=True)
data = None


def ShowSelection(select, row, col):
    print(
        f"\nIntervencion de datos de la lista: {row}, en columna {col}. Asigna {select}"
    )
    for d in data:
        if d[0] == row[0]:
            d[col] = select


def ExitApp():
    exit()


def ConfigWindow(widthWnd, heightWnd):
    window.title("Asistencia 7mo 3ra")
    widthScreen = window.winfo_screenwidth()
    heightScreen = window.winfo_screenheight()
    posX = (widthScreen // 2) - (widthWnd // 2)
    posY = (heightScreen // 2) - (heightWnd // 2)
    window.geometry("{}x{}+{}+{}".format(widthWnd, heightWnd, posX, posY))
    CreateTitleLabel()


def CreateTitleLabel():
    titleLabel = tk.Label(titleFrame, text="REGISTRO DE ASISTENCIApp", anchor="center")
    titleLabel.config(font=("Arial", 20, "bold"))
    titleLabel.pack(fill="both", expand=True, side="top", pady=25)


def CreateHeaders(headers):
    labelsHeader = []
    for title in headers:
        label = tk.Label(
            headerFrame,
            text=title.upper(),
            anchor="center",
            width=int(100 / (len(headers) + 1)),
        )
        label.config(font=("Arial", 12, "bold"))
        labelsHeader.append(label)
    for label in labelsHeader:
        label.pack(fill="both", expand=True, side="left", padx=5)


def CreateLabelsData(rowFrame, row, col):
    label = tk.Label(
        rowFrame,
        text=col,
        anchor="center",
        width=int(100 / (len(row) + 1)),
    )
    label.pack(fill="both", expand=True, side="left", padx=5)
    return label


def CreateButtonExit(caption, command):
    button = tk.Button(
        buttonsFrame,
        text=caption,
        command=command,
        width=int(100 / 4),
    )
    button.pack(fill="both", expand=True, side="left")


def CreateButtonSave(caption, command, pathToFile):
    button = tk.Button(
        buttonsFrame,
        text=caption,
        command=lambda: command(pathToFile, data),
        width=int(100 / 4),
    )
    button.pack(fill="both", expand=True, side="left")


def CreateButtonReport(caption, pathToFile):
    button = tk.Button(
        buttonsFrame,
        text=caption,
        command=lambda: CreateReport(pathToFile, data),
        width=int(100 / 4),
    )
    button.pack(fill="both", expand=True, side="left")


def CreateCheckboxData(rowFrame, row, col):
    select = tk.IntVar(value=0)
    if row[col] == "1":
        select = tk.IntVar(value=1)
    check = tk.Checkbutton(
        rowFrame,
        text="",
        variable=select,
        onvalue=1,
        offvalue=0,
        command=lambda: ShowSelection(select.get(), row, col),
    )
    check.pack(fill="both", expand=True, side="left", padx=5)
    return check


def CreateRowsData(data):
    rowLabelData = []
    counterRow = 0
    for row in data:
        rowLabel = []
        rowFrame = tk.Frame(dataFrame)
        rowFrame.pack(fill="x", expand=True)
        counterCols = 0
        counterRow += 1
        for col in row:
            if counterCols == 0:
                rowLabel.append(CreateLabelsData(rowFrame, row, col))
            else:
                rowLabel.append(CreateCheckboxData(rowFrame, row, counterCols))
            counterCols += 1
        rowLabelData.append(rowLabel)


def CreateList(headers, data):
    globals()["data"] = data
    CreateHeaders(headers)
    CreateRowsData(globals()["data"])


def CreateOptionButtons():
    CreateButtonSave("Guardar Cambios", SaveChangesData, "data/students.csv")
    CreateButtonReport("Crear Reporte", "reporte.pdf")
    CreateButtonExit("Salir", exit)
