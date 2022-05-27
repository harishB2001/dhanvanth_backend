import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="harish",
  database="diseaseprediction"
)
mycursor = mydb.cursor()

def dbExecute(query:str)->list:
    mycursor.execute(query)
    return mycursor.fetchall()

def getQuery(symptom:set)->str:
    columns = " in (s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17)"
    query = ("""
    select * from dataset where
    """)
    for s in symptom:
        query = query+"\'"+s+"\'"+columns+" and "
    query = query.removesuffix("and ")
    return query

def getRelevantSymptoms(symptom):
    symptomsTermFrequency = {}
    diseaseSet = set()
    query = getQuery(symptom)

    result =  dbExecute(query)
    for tup in result:
        diseaseSet.add(tup[0])
        for i in range(1,len(tup)):
            if tup[i]!=None:
                tf = symptomsTermFrequency.setdefault(tup[i],0)
                symptomsTermFrequency[tup[i]] = tf+1
    for s in symptom:
        symptomsTermFrequency.pop(s)

    symptomsTermFrequency=dict(sorted(symptomsTermFrequency.items(), key=lambda item: item[1],reverse=True))
    stf = []

    for s in symptomsTermFrequency.keys():
        stf.append(s)
    return {"relevantsymptoms":stf,"diseaseSet":diseaseSet}

# usage of getRelevantSymptoms()
# symptoms = {"chills","nausea","high fever","vomiting",}
# getSet = getRelevantSymptoms(symptoms)
# print(getSet["relevantsymptoms"])
# print(getSet["diseaseSet"])