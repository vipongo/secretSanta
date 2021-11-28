import os, sys, random, shutil
from datetime import date

def createFolder():
    try:
        os.mkdir(str(date.today()))
        print("Directory called ", str(date.today()), " successfully created")
    except:
        print("Directory called ", str(date.today()), " already exists")

def deleteFiles(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def createSecretSanta(personList):
    personListToGive = personList.copy()
    createFolder()
    for person in personList:
        print(person)
        randomPerson = random.randint(0, len(personListToGive)-1)
        check = 0
        while (personListToGive[randomPerson] == person):
            randomPerson = random.randint(0, len(personListToGive)-1)
            check += 1
            if check > 100:
                deleteFiles(str(date.today()))
                createSecretSanta(personList)
                return True
        
        #Write in the file
        fileName = str(date.today())+"/"+str(person)+".txt"
        f = open(fileName, "w")
        f.write(personListToGive[randomPerson])
        f.close()
        personListToGive.remove(personListToGive[randomPerson])
    
    print("All files have been created")


personList = list(sys.argv)[1:]
print(personList)
createSecretSanta(personList)