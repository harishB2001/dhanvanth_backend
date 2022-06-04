from flask import Flask
from flask import request
import parser

import application_util
import handler

app = Flask(__name__)



@app.route('/')
def index():
    ##start
    p = parser.Parser(request.args)
    ##end

    while(True):
        sentence=''
        if p.crossQuestion == False:
            sentence = p.statement
        else:
            p.crossQuestion = False
            sentence = p.previousStatement
        
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
            try:
                symptom = p.relatedSymptoms[0]
            except:
                pass
            symptom = application_util.getExactSymptom(symptom)["exactWord"]
            p.allSymptoms = handler.acceptSymptoms(p.allSymptoms, symptom)
            relatedSymptomsTF = application_util.lookup_operations.getRelevantSymptoms(p.allSymptoms)
            p.possibleDiseases = relatedSymptomsTF["diseaseSet"]
            p.relatedSymptoms = relatedSymptomsTF["relevantsymptoms"]
          
            for s in p.shouldNotAskAgain:
                try:
                    p.relatedSymptoms.remove(s)
                except:
                    pass
            # ##
            # return p.respons()
            # ##

            if p.i>=3:
                if (len(p.possibleDiseases) <=3  or len(p.relatedSymptoms) == 0):
                    return p.createResponse()
            try:
               p.message = "Do you have any symptoms of "+p.relatedSymptoms[0] +" ?"
               p.i+=1
               return  p.respons()
            except:
                p.previousStatement = sentence
                p.crossQuestion = True
                p.possibleDiseases = set()
                p.allSymptoms = set()
                p.message = ""
                p.relatedSymptoms = []
                p.shouldNotAskAgain =[]
                p.i = 0
                # allSymptoms = handler.acceptSymptoms(allSymptoms, symptom)
                continue
    #end of positive response

    #Stat of negative response
        if intent == "NEGATIVE":
            p.shouldNotAskAgain.append(p.relatedSymptoms[0])
            
            for s in p.shouldNotAskAgain:
                try:
                    p.relatedSymptoms.remove(s)
                except:
                    pass
       
                    
            if p.i>=3:
                if (len(p.possibleDiseases) <= 3 or len(p.relatedSymptoms) == 0):
                    return p.createResponse()
            try:
                p.message = "Do you have any symptoms of "+p.relatedSymptoms[0] +" ?"
                p.i+=1
                return  p.respons()
            except:
                p.previousStatement = sentence
                p.crossQuestion = True
                p.possibleDiseases = set()
                p.allSymptoms = set()
                p.message = ""
                p.relatedSymptoms = []
                p.shouldNotAskAgain =[]
                p.i = 0
                # allSymptoms = handler.acceptSymptoms(allSymptoms, symptom)
                continue
    #Stat of negative response


        if intent == "SYMPTOM" and disease!="":
            disease = application_util.getExactDisease(disease)
            allSymp = application_util.getSymptoms(disease)
            s = 'Few Symptoms of '+disease["exactWord"]+" are:\n"
            p.message = s+",\n".join(allSymp)
            return p.respons()
        elif intent == "SYMPTOM":
            p.message = "Try Asking..'what are the symptoms of malaria'"
            return p.respons()
            


        if intent == "PRECAUTION" and disease!="":
            disease = application_util.getExactDisease(disease)
            allPre = application_util.getPrecaution(disease)
            s = 'Few precautions of '+disease["exactWord"]+" are:"
            for i in allPre:
                s+="\n"+i+","
            p.message = s
            return p.respons()
        elif intent == "PRECAUTION":
            p.message = "Try Asking..'what are the Precaution of jaundice'"
            return p.respons()

        if intent == "HI":
            p.message = """\tHi there! \n\tI'm dhanvant. your medical Assistance..\n\tTry asking me..\n\t1)I have headache,\n\t2)Precautions of Malaria ..."""
            return p.respons()
        if intent == "THANKS":
            p.message = "\tAlways At your service.Thank you"
            return p.respons()

app.run()

