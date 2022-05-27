from sentence_transformers import SentenceTransformer,util
import joblib

_bert_load = joblib.load('asset\\sbert_model')


symptomPositiveStatements = [
    "yes i have the symptoms ",
    "i have the symptom"
    "yes",
    "yes ofcourse",
    "yes im suffering with that",
    "i have it too",
    "i feel the symptoms",
    "yes i have",
    "hi i have the symptom "
    "hello i have the symptom "
    ]


symptomNegativeStatements = [
    "i dont have",
    "no",
    "no i do not have the symptom"
    "ofcourse not",
    "im not suffering with that",
    "i do not have the symptom",
    "i have no idea on it",
    "no symptom of"
    "nope i dont feel"
    "i dont feel"
    "no sense of it"
    "not right now"
]

symptomAsking = [
    "what are the symptoms of",
    "important sign of",
    "what are the main signs of",
    "symptoms of",
    "indications of ",
    "indications",
    "symptoms",
    "common symptoms of"
]

precautionAsking = [
    "how to safeguard from",
    "precaution of",
    "what are the measures to prevent",
    "how to protect ourself from",
    "how to avoid risk of",
    "take precautions on",
    "prevantive measures of",
]

treatmentAsking = [
    "how to treat",
    "what is the medication for",
    "how to cure",
    "cure",
    "therapy for",
    "deal with ",
    "what to do for",
]

hi = [
    "hi there",
    "hello dhanvanth",
    "What can you do",
    "how will you help me",
    "greetings",
    "can you help me",

]

thanks =  [
      "thank you soo much",
      "i appreciate it",
      "thanks for your work",
      "much appreciated",
      "thanks for the treatment",
      ]


def getIntent(sentennce):
        positiveScore = 0   # when user gives a positve reply for a symptom
        negativeScore = 0   # when user gives a negative reply for a symptom
        symptomScore = 0    # when user asking about symptom of a  disease
        precautonScore = 0  # when user asking about precaution
        treatmentScore = 0  # when user asking about the tretament
        hiScore = 0         # when user says hi
        thanksScore = 0     # when user say thanks 
        
        scores = []
        intent = ["POSITIVE","NEGATIVE","SYMPTOM","PRECAUTION","TREATMENT","HI","THANKS"]
        #symptom positive statement
        for record in symptomPositiveStatements:
            input1 = _bert_load.encode(record)
            input2 = _bert_load.encode(sentennce)
            tempScore = util.cos_sim(input1,input2)[0][0].item()
            positiveScore+=tempScore
        
        #symptom negative statement
        for record in symptomNegativeStatements:
            input1 = _bert_load.encode(record)
            input2 = _bert_load.encode(sentennce)
            tempScore = util.cos_sim(input1,input2)[0][0].item()
            negativeScore+=tempScore

        #asking symptom statement    
        for record in symptomAsking:
            input1 = _bert_load.encode(record)
            input2 = _bert_load.encode(sentennce)
            tempScore = util.cos_sim(input1,input2)[0][0].item()
            symptomScore+=tempScore


        #asking precaution
        for record in precautionAsking:
            input1 = _bert_load.encode(record)
            input2 = _bert_load.encode(sentennce)
            tempScore = util.cos_sim(input1,input2)[0][0].item()
            precautonScore+=tempScore


        #asking about treatment
        for record in treatmentAsking:
            input1 = _bert_load.encode(record)
            input2 = _bert_load.encode(sentennce)
            tempScore = util.cos_sim(input1,input2)[0][0].item()
            treatmentScore+=tempScore

        #greeting
        for record in hi:
            input1 = _bert_load.encode(record)
            input2 = _bert_load.encode(sentennce)
            tempScore = util.cos_sim(input1,input2)[0][0].item()
            hiScore+=tempScore


        #thanks 
        for record in thanks:
            input1 = _bert_load.encode(record)
            input2 = _bert_load.encode(sentennce)
            tempScore = util.cos_sim(input1,input2)[0][0].item()
            thanksScore+=tempScore

        scores.append(positiveScore/len(symptomPositiveStatements))
        scores.append(negativeScore/len(symptomNegativeStatements))
        scores.append(symptomScore/len(symptomAsking))
        scores.append(precautonScore/len(precautionAsking))
        scores.append(treatmentScore/len(treatmentAsking))
        scores.append(hiScore/len(hi))
        scores.append(thanksScore/len(thanks))
        return {"intent":intent[scores.index(max(scores))],"score":max(scores)}     


# # print("can start") ##must be removed while production

# while(True): ##must be removed while production
#     s =  input("Enter a statement: ")
#     if s=="exit":
#         break
#     print(cosineSimilarities(s)) ##must be removed while production
    