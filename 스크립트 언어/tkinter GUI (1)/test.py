
import tkinter_ex

sfed = "\n"
print("\n")

def getData(year):
    global CrimeDoc
    req = conn.getresponse()
    #print(req.status)
    if int(req.status) == 200:
        CrimeDoc = req.read().decode('utf-8')
        SearchLibrary()
        #PrintSearchData()
        #return extractBookData(req.read().decode('utf-8'))
    else:
        print("OpenAPI request has been failed!! please retry")
        return None