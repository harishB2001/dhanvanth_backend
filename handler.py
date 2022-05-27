
def acceptSymptoms(allSymptom,symptom):
    allSymptom.add(symptom)
    return allSymptom

def rejectSymptoms(relatedSymptoms,symptom):
    relatedSymptoms.remove(symptom)
    return relatedSymptoms

def printDisease(diseaseSet):
    print("Based on the given Symptoms we identified these Diseases")
    i = 1
    for s in diseaseSet:
        print(str(i)+")."+s)
        i+=1