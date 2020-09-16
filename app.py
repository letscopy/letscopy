
import ctypes
from firebase import firebase
from time import sleep
import threading 
import json


print("APP")
print("----------")
message_sent = False
firebase = firebase.FirebaseApplication("https://classroomclasspy.firebaseio.com/", None)
data_message = ""
def listener():

    i = 0
    old_message = "Eyy que tal"
    global message_sent
    while True:
        i = i+1
        data_source = firebase.get("/Exams", None)
        
        data = list(data_source.values())[-1]
        data_json = json.loads(data)
        data_author = data_json["name"]
        data_message = data_json["message"]
        data_str = str(data_author) + ": " + str(data_message)

        if  message_sent == True:
            old_message = message
            message_sent = False
        if data_message != old_message:
            ctypes.windll.user32.MessageBoxW(0, data_str, "Error", 6)
        old_message = data_message


t1 = threading.Thread(target=listener)
author = input("Author: \n")
t1.start()

while True:
    message = input("Message: \n")
    if message != "":
        tosend = {
        "name": author,
        "message": message }
        tosend_json = json.dumps(tosend)
        firebase.post('/Exams', tosend_json)
        message_sent = True