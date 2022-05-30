
def acceptSymptoms(allSymptom,symptom):
    allSymptom.add(symptom)
    return allSymptom

def rejectSymptoms(relatedSymptoms,symptom):
    relatedSymptoms.remove(symptom)
    return relatedSymptoms

