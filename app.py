from fastapi import FastAPI
import time
from worker import process

app = FastAPI()


class staticMap:
    def __init__(self):
        self.dict1 = {}

sm = staticMap()


@app.get("/inputString/")
def processString(s1: str =""): 

# if key exist and is null then return Request In Progress
    if sm.dict1.get(s1) == "":

        return {"statusMessage":"Request In Progress"}

# if key exist and value is not None and also not contain empty string then return value
    elif sm.dict1.get(s1) != None and sm.dict1.get(s1) != "":

        return {"result": sm.dict1[s1],"statusMessage": "Already Processed"}

# create a new key with default null string and store value after processing 
    else:
        sm.dict1[s1] = ""

        res = process(s1)

        sm.dict1[s1] = res

        return {"result": res,"statusMessage": "Successfully Completed"}



