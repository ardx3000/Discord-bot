import json

def validation(author):
    points = 1000;

# Initializare retard

    errorBool = True # True daca user-ul nu exista , false daca exista.

    with open('profile.json', 'w', encoding='utf-8') as f: #Bubuit ori aici in F
        dataFromJson = json.load(f)

        #create a method to extrac data from Json
        try:
            for i in dataFromJson.values():
                if dataFromJson(i['name']) != author: #ori cacatul asta de if
                    dataToBeInserted = {"name": author, "points": points}
                    createUpdateJson(dataToBeInserted)
                    print("a reusit")
                    return errorBool
        except:
            print("a Esuat")
            errorBool = False
            return errorBool



def createUpdateJson(validatedData):

    with open('profile.json', 'w', encoding='utf-8') as f:
        json.dump(validatedData, f, ensure_ascii=False, indent=2)


def testMethod(authorxd):
    with open('profile.json', 'w', encoding='utf-8') as f:
        json.dump(authorxd, f, ensure_ascii=False, indent=2)

'''def viewProfile(author):
    with open('profile.json', 'w', encoding='utf-8') as f:
        try:'''