from flask import request
class Parser:
    possibleDiseases = set()
    allSymptoms = set()
    message = ""
    relatedSymptoms = []
    shouldNotAskAgain =[]
    i = 0
    crossQuestion = False
    previousStatement = ""
    statement = ""

    def __init__(self,request):
        self.possibleDiseases = set(request.get("pd").split(","))
        try:
            self.possibleDiseases.remove("")
        except:
            pass

        self.allSymptoms = set(request.get("as").split(","))
        try:
            self.allSymptoms.remove("")
        except:
            pass

        self.message = request.get("m")

        self.relatedSymptoms = request.get("rs").split(",")
        try:
            self.relatedSymptoms.remove("")
        except:
            pass

        self.shouldNotAskAgain =request.get("snaa").split(",")
        try:
            self.shouldNotAskAgain.remove("")
        except:
            pass

        self.i = int(request.get("i"))

        self.crossQuestion = True if request.get("cq") == "true" else False

        self.previousStatement = request.get("ps")

        self.statement = request.get("s")


    def respons(self):
        a = dict()
        a["possibleDiseases"] =list(self.possibleDiseases)
        a["allSymptoms"]=list(self.allSymptoms)
        a["message"]=self.message
        a["relatedSymptoms"]=self.relatedSymptoms
        a["shouldNotAskAgain"]=self.shouldNotAskAgain
        a["i"] =self.i
        a["crossQuestion"]=self.crossQuestion
        a["previousStatement"]=self.previousStatement
        a["statement"]=self.statement
        return a
    

    def createResponse(self):
        self.message  = "Based on the given symptom we identified the possibe diseases.."
        for s in self.possibleDiseases:
            self.message+="\n"+s
        self.possibleDiseases = set()
        self.allSymptoms = set()
        self.relatedSymptoms = []
        self.shouldNotAskAgain =[]
        self.i = 0
        self.crossQuestion = False
        self.previousStatement = ""
        self.statement = ""
        return self.respons()
        
