import application_util
import handler

possibleDiseases = set()
allSymptoms = set()
message = ""
relatedSymptoms = []
shouldNotAskAgain =[]

while(True):
    sentence = input("\nEnter the statement: ")
    
    if sentence == "exit":
        break
    ner_dict = application_util.nerOperations(sentence.lower())

    intent = application_util.getIntent(ner_dict["statement"])["intent"]
    
    symptom = ""
    disease = ""
    if ner_dict["disease"] =="":
        symptom = ner_dict["symptoms"]
    elif ner_dict["symptoms"]=="":
         disease = ner_dict["disease"]

    if intent == "POSITIVE":
        # get the symptoms..
        if symptom =="":
            symptom = relatedSymptoms[0]
        else:
            symptom = application_util.getExactSymptom(symptom)["exactWord"]
        allSymptoms = handler.acceptSymptoms(allSymptoms, symptom)
        relatedSymptomsTF = application_util.lookup_operations.getRelevantSymptoms(allSymptoms)
        possibleDiseases = relatedSymptomsTF["diseaseSet"]
        relatedSymptoms = relatedSymptomsTF["relevantsymptoms"]
        for s in shouldNotAskAgain:
            try:
                relatedSymptoms.remove(s)
            except:
                pass
        if len(possibleDiseases) == 1 or len(relatedSymptoms) == 0:
            handler.printDisease(possibleDiseases)
            possibleDiseases = set()
            allSymptoms = set()
            message = ""
            relatedSymptoms = []
            shouldNotAskAgain =[]
            continue
        print("\n\t Do you have any symptoms of "+relatedSymptoms[0])
        continue

    
    if intent == "NEGATIVE":
        shouldNotAskAgain.append(relatedSymptoms[0])
        for s in shouldNotAskAgain:
            try:
                relatedSymptoms.remove(s)
            except:
                pass
        # symptom = relatedSymptoms[0]
        #relatedSymptoms = handler.rejectSymptoms(relatedSymptoms,symptom)
        
        if len(possibleDiseases) == 1 or len(relatedSymptoms) == 0:
            handler.printDisease(possibleDiseases)
            possibleDiseases = set()
            allSymptoms = set()
            message = ""
            relatedSymptoms = []
            shouldNotAskAgain =[]
            continue
        print("\n\t Do you have any symptoms of "+relatedSymptoms[0])
        


    
    
    
    
    
    if intent == "SYMPTOM" and symptom!="":
        pass
    elif intent == "SYMPTOM":
        pass


    if intent == "PRECAUTION" and disease!="":
        pass
    elif intent == "PRECAUTION":
        pass


    if intent =="TREATMENT" and disease!="":
        pass
    elif intent =="TREATMENT":
        pass


    if intent == "HI":
        print("""\tHi there! \n\tI'm dhanvant your medical Assistance..\n\tTry asking me\n\t1)I have headache\n\t2)Precautions of Malaria ...""")
        pass
    if intent == "THANKS":
        print("\tAlways At your service Thank you")
        break
