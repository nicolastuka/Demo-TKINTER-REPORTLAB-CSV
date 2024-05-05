import csv


def LoadDataFromCSV(pathToFile):
    data = []
    with open(pathToFile, "r", newline="", encoding="utf-8") as file:
        reader_csv = csv.reader(file)
        headers = next(reader_csv)
        for row in reader_csv:
            data.append(row)
    return headers, data


def SaveChangesData(pathToFile, data):
    with open(pathToFile, "r", newline="", encoding="utf-8") as file:
        reader_csv = csv.reader(file)
        headers = next(reader_csv)
    data.insert(0, headers)
    with open(pathToFile, "w", newline="", encoding="utf-8") as file:
        writer_csv = csv.writer(file)
        for row in data:
            writer_csv.writerow(row)
