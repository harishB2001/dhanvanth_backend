import application_util
import handler

possibleDiseases = set()
allSymptoms = set()
message = ""
relatedSymptoms = []
shouldNotAskAgain =[]
i = 0
crossQuestion = False
previousStatement = ""
while(True):
    if crossQuestion == False:
        sentence = input("\nEnter the statement: ")
    else:
        crossQuestion = False
        sentence = previousStatement
    
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

#Stat of positive response 
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
        if i>=3:
            if (len(possibleDiseases) == 1 or len(relatedSymptoms) == 0):
                handler.printDisease(possibleDiseases)
                possibleDiseases = set()
                allSymptoms = set()
                message = ""
                relatedSymptoms = []
                shouldNotAskAgain =[]
                i = 0
                continue
        try:
            print("\n\t Do you have any symptoms of "+relatedSymptoms[0])
        except:
            previousStatement = sentence
            crossQuestion = True
            possibleDiseases = set()
            allSymptoms = set()
            message = ""
            relatedSymptoms = []
            shouldNotAskAgain =[]
            i = 0
            # allSymptoms = handler.acceptSymptoms(allSymptoms, symptom)
            continue
        i+=1
        continue
#end of positive response
    
#Stat of positive response
    if intent == "NEGATIVE":
        shouldNotAskAgain.append(relatedSymptoms[0])
        for s in shouldNotAskAgain:
            try:
                relatedSymptoms.remove(s)
            except:
                pass
        
        if i>=3:
            if (len(possibleDiseases) == 1 or len(relatedSymptoms) == 0):
                handler.printDisease(possibleDiseases)
                possibleDiseases = set()
                allSymptoms = set()
                message = ""
                relatedSymptoms = []
                shouldNotAskAgain =[]
                i = 0
                continue
        try:
            print("\n\t Do you have any symptoms of "+relatedSymptoms[0])
        except:
            previousStatement = sentence
            crossQuestion = True
            possibleDiseases = set()
            allSymptoms = set()
            message = ""
            relatedSymptoms = []
            shouldNotAskAgain =[]
            i = 0
            # allSymptoms = handler.acceptSymptoms(allSymptoms, symptom)
            continue
        i+=1
        continue
#Stat of positive response
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
