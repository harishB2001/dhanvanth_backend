import spacy

nlp = spacy.load('asset\\NER_MODEL')

def nerOperations(sentence):
    doc = nlp(sentence)
    statement = ""
    symptoms = []
    diseases = []
    for token in doc:
        if(token.ent_type_==""):
            statement+=token.text+" "
        if(token.ent_type_=="SYMPTOMS"):
            symptoms.append(token.text)
        if(token.ent_type_=="DISEASE"):
            diseases.append(token.text)
    return {"statement":statement,"symptoms":" ".join(symptoms),"disease":" ".join(diseases)}

# print(nerOperations("im having diarrhoea"))