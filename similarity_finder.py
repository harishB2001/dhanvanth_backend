import csv
from sentence_transformers import SentenceTransformer,util
import joblib

_bert_load = joblib.load('asset\\sbert_model')

def cosineSimilarities(sentennce,path)->dict:
    file = open(path)
    csvreader = csv.reader(file)

    rows = []
    for record in csvreader:
        rows.append(record[0])
    while(True):
        score = 0
        exactWord = ""
        for record in rows:
            input1 = _bert_load.encode(record)
            input2 = _bert_load.encode(sentennce)
            tempScore = util.cos_sim(input1,input2)[0][0].item()
            if score<tempScore:
                score = tempScore
                exactWord = record
        # print(score,previousScore,end="\t\t") ##must be removed while production
        return {"exactWord":exactWord,"score":score}
# print("can start") ##must be removed while production

# #while(True): ##must be removed while production
# print(cosineSimilarities(input(),'asset\\symptoms.csv')) ##must be removed while production