import csv

def getPrecaution(disease):
    file = open("asset\\diseasePrecaution.csv")
    csvreader = csv.reader(file)
    rows = []
    for record in csvreader:
        if record[0].casefold()==disease["exactWord"].casefold():
            rows.extend(record[1:])
    return rows
# print(getPrecaution({"exactWord":"Typhoid"}))

    
