import csv

file = open("asset\\diseasePrecaution.csv")
csvreader = csv.reader(file)
def precautionAsking(disease):
    rows = []
    for record in csvreader:
        if record[0]==disease:
            rows.extend(record[1:])
    return rows
        

    
