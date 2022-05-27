import similarity_finder
import ner_operation
import lookup_operations
import intent_classifier

def getExactSymptom(symptom):
    return similarity_finder.cosineSimilarities(symptom,'asset\\symptoms.csv')

def getExactDisease(disease):
    return similarity_finder.cosineSimilarities(disease,'asset\\diseases.csv')

def nerOperations(sentence):
    return ner_operation.nerOperations(sentence)

def lookupOperations(symptom):
    return lookup_operations.getRelevantSymptoms(symptom)

def getIntent(sentence):
    return intent_classifier.getIntent(sentence)