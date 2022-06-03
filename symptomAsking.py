import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="harish",
  database="diseaseprediction"
)
mycursor = mydb.cursor()

symptoms = set()

def getSymptoms(disease):
    # mycursor.execute("select * from dataset where disease="+disease)
    mycursor.execute("select  * from dataset where disease = '"+disease['exactWord']+"'")
    result = mycursor.fetchall()
    for tup in result:
        for i in range(1,len(tup)):
            if tup[i]!=None:
                symptoms.add(tup[i])
    return symptoms

