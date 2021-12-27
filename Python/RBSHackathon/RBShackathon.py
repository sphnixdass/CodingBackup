from flask import Flask, render_template, request, url_for, redirect, Response
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO
import speech_recognition as sr
import cv2
import time
import requests

import requests
import ssl
import ast



try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context





app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
Bootstrap(app)

tempvar = "hi dass"
client_id='ncThG4QMy3GwEZ6jThcQCqCmbrHPWr_z8yAdUu5Q6FU%3D'
client_secret='Nqh5FWyOdcd6JoKddgz4nfgkIAeXldFu_LCCVmWcGxA%3D'




 
def natwest_api(skip6):

    # 1- retrieve access token
    url = "https://ob.natwest.useinfinite.io/token"

    payload = 'grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret + '&scope=accounts'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data = payload, verify = False )
    jsonResponse = response.json()

    tempaccesstoken = ""
    #print("Print each key-value pair from JSON response")
    for key, value in jsonResponse.items():
        #print(key, ":", value)
        if key == "access_token":
            tempaccesstoken = value

    print("1======================")
    #2- post account request

    url = "https://ob.natwest.useinfinite.io/open-banking/v3.1/aisp/account-access-consents"

    payload = "{\n  \"Data\": {\n    \"Permissions\": [\n      \"ReadAccountsDetail\",\n      \"ReadBalances\",\n      \"ReadTransactionsCredits\",\n      \"ReadTransactionsDebits\",\n      \"ReadTransactionsDetail\"\n    ]\n  },\n  \"Risk\": {}\n}"
    headers = {
    'Authorization': 'Bearer ' + tempaccesstoken,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload, verify =False)
    print(response.text.encode('utf8'))

    jsonResponse = response.json()
    ConsentId = ""
    for key, value in jsonResponse.items():
        if key == "Data":
            ConsentId = value['ConsentId']
            print("ConsentId", ConsentId)
        

    # url = "https://ob.natwest.useinfinite.io/open-banking/v3.1/aisp/account-access-consents"

    # payload = "{\n  \"Data\": {\n    \"Permissions\": [\n      \"ReadAccountsDetail\",\n      \"ReadBalances\",\n      \"ReadTransactionsCredits\",\n      \"ReadTransactionsDebits\",\n      \"ReadTransactionsDetail\"\n    ]\n  },\n  \"Risk\": {}\n}"
    # headers = {
    #   'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHAiOiJkZW1vLWFwcC1jZTllYzJmYS04NTVhLTQ2Y2YtYjVkYy1iMGZkZGY2YTliZTEiLCJvcmciOiJjZTllYzJmYS04NTVhLTQ2Y2YtYjVkYy1iMGZkZGY2YTliZTEuZXhhbXBsZS5vcmciLCJpc3MiOiJuYXR3ZXN0LnVzZWluZmluaXRlLmlvIiwidG9rZW5fdHlwZSI6IkFDQ0VTU19UT0tFTiIsImV4dGVybmFsX2NsaWVudF9pZCI6Im5jVGhHNFFNeTNHd0VaNmpUaGNRQ3FDbWJySFBXcl96OHlBZFV1NVE2RlU9IiwiY2xpZW50X2lkIjoiZjA1NDJmNGItZGFjYi00YmM1LThkMGQtMTJjMDBhODY3N2UyIiwibWF4X2FnZSI6ODY0MDAsImF1ZCI6ImYwNTQyZjRiLWRhY2ItNGJjNS04ZDBkLTEyYzAwYTg2NzdlMiIsInNjb3BlIjoiYWNjb3VudHMiLCJleHAiOjE1OTUyNjE2NDEsImlhdCI6MTU5NTI2MTM0MSwianRpIjoiMTcyOTMyY2MtOGM4MS00YjAwLWJiNGMtMDg0YjAyNmRlM2RiIiwidGVuYW50IjoiTmF0V2VzdCJ9.aWVJIZ2z7JyzcEBoGrNV-OIJbn0f_n2Tj4FHIGel0Qn0Vq0WPNSrhsL6l7otP_CCd5y7RhicdTByY5Pg6jE_NcdmNnvJmGi3aZs2L1LsUP5MTc8eJ1SgjURSHi6dEpqVcMECOCR1E8b5iDrqVMTcGX32MhLpIMk4jjlIrnxMXjSVTgyrIdqr58ufFqG_-GLx-Pj-BLRvaj6R8FsBdpS6bj35yUKhieoIsMSHKRSOwOIE32zheDnh2zlmTZNwQcZH7Xn8ePnaBVySVG9U_MMMTczo_gF4LnMaSAkuds3k20gO5TU-J5g7cCKBQ6nyXNfWCUN08xbr5JPPrUHThhwiPA',
    #   'Content-Type': 'application/json'
    # }

    # response = requests.request("POST", url, headers=headers, data = payload, verify=False)


    print("2======================")

    print("ConsentId", ConsentId)
    # 3 - Approve Consent prog
    url = "https://api.natwest.useinfinite.io/authorize?client_id=" + client_id + "&response_type=code id_token&scope=openid accounts&redirect_uri=https%3A%2F%2Fce9ec2fa-855a-46cf-b5dc-b0fddf6a9be1.example.org%2Fredirect&state=ABC&request=" + ConsentId + "&authorization_mode=AUTO_POSTMAN&authorization_username=123456789012@ce9ec2fa-855a-46cf-b5dc-b0fddf6a9be1.example.org"


    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload, verify =False)

    tempsplit = response.text.encode('utf8')

    codeid = ""
    print(response.text.encode('utf8'))
    sp1 = tempsplit.decode().split("code=")
    print("sp1[1]", sp1[1])
    sp3= sp1[1]
    sp2 = sp3.split("&id_token")
    codeid = sp2[0]
    print("codeid", codeid)
    print("3====================")


    #4 = exchange code for access token
    url = "https://ob.natwest.useinfinite.io/token"

    payload = 'client_id=' + client_id + '&client_secret=' + client_secret + '&redirect_uri=https%3A//ce9ec2fa-855a-46cf-b5dc-b0fddf6a9be1.example.org/redirect&grant_type=authorization_code&code=' + codeid 


    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }


    response = requests.request("POST", url, headers=headers, data = payload, verify=False)

    accesstoken2 = response.text.encode('utf8')
    print("accesstoken2", type(accesstoken2))
    dict_str = accesstoken2.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    print("mydata", mydata["access_token"])
    accesstoken3 = mydata["access_token"]
    print(response.text.encode('utf8'))
    print("4====================")

    #5 - list accounts
    url = "https://ob.natwest.useinfinite.io/open-banking/v3.1/aisp/accounts"

    payload = {}
    headers = {
    'Authorization': 'Bearer ' + accesstoken3
    }

    response = requests.request("GET", url, headers=headers, data = payload, verify=False)
    jsonResponselistacc = response.json()
    listaccount = ""
    for key, value in jsonResponselistacc.items():
        print("key", key)
        print("value", value)
        print("value", value["Account"])
        listaccount = value["Account"]
        break
    print("listaccount", type(listaccount))
    print("listaccount", len(listaccount))
    listaccountdata = ""

    for i in range(len(listaccount)):
    # print("DDDDD" + str(i) + str(listaccount[i]["AccountId"]))
        listaccountdata = listaccountdata + listaccount[i]["AccountId"] + "<:>" + listaccount[i]["Nickname"] + "<,>"

    print("listaccountdata", listaccountdata)
    # for key2, value2 in value.json().items():
    #     print("key2", key2)
    #     print("value2", value2)


    print(response.text.encode('utf8'))
    print("5====================")

    if (skip6 == True):
        #6 = list transactions
        url = "https://ob.natwest.useinfinite.io/open-banking/v3.1/aisp/accounts/09b8a760-3539-4a96-a3d0-61936845a5a5/transactions"

        payload = {}
        headers = {
        'Authorization': 'Bearer ' + accesstoken3
        }

        response = requests.request("GET", url, headers=headers, data = payload, verify=False)
        jsonResponsetransaction = response.json()
        listtrans = ""
        for key, value in jsonResponsetransaction.items():
        #print("key", key)
        #print("value", value)
            if key == "Data":
                print("ddddddd", value["Transaction"])
                for i in range(len(value["Transaction"])):
                    templisttrans = value["Transaction"][i] 
                    #print(type(value["Transaction"][i]))
                    #print(templisttrans["CreditDebitIndicator"])
                    listtrans = listtrans + str(templisttrans["CreditDebitIndicator"]) + "<:>" + str(templisttrans["Amount"]["Amount"]) + "<:>" + str(templisttrans["Amount"]["Currency"])  + "<:>" + str(templisttrans["Balance"]["Amount"]["Amount"])  + "<:>" + str(templisttrans["Balance"]["Amount"]["Currency"]) + "<,>"
                    print(type(templisttrans["Amount"]))


        print(listtrans)
        #print(response.text.encode('utf8'))
        print("6====================")
        socketio.emit('apiresponseaccountype', listtrans)
    
    if (skip6 == False):
        socketio.emit('apiresponse', listaccountdata)





def gen():
    global facefound
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    print(tempvar)
    # To capture video from webcam. 
    cap = cv2.VideoCapture(0)
    # To use a video file as input 
    # cap = cv2.VideoCapture('filename.mp4')

    while True:
        # Read the frame
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cap.release()
            facefound()
            frame2 = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame2 + b'\r\n')
            return "dddd"
            break

        frame2 = cv2.imencode('.jpg', img)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame2 + b'\r\n')
        time.sleep(0.1)

        # Display
        # cv2.imshow('img', img)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            cap.release()
            break


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def loginpage():
    return render_template('login.html')

@app.route('/main_webpage', methods=['GET', 'POST'])
def main_webpage():
   return render_template('main_webpage.html')


@app.route('/index')
def main_index():
    print("main menu")
    return render_template('index.html')

@app.route('/main_menu')
def main_menu():
    print("main menu")
    return render_template('main_menu.html')

@app.route('/get_api')
def get_api():
    print("get api")
    rbs_api()
    return rbs_api()

def facefound():
    socketio.emit('myresponse', "found")

def messageReceived():
    print('message was received!!!')


def voicecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_text = r.listen(source)
        try:
            print("Text: "+r.recognize_google(audio_text))
        except:
            print("Sorry, I did not get that")
            

@socketio.on('myevent')
def handle_my_custom_event(data):
    print('received my event: ' + str(data))
    if tempvar == "found":
        main_menu()


@socketio.on('indexemit')
def indexemit(data):
    print("indexemit" + str(data))
    natwest_api(False)

@socketio.on('indexemitaccounttype')
def indexemitaccounttype(data):
    print("indexemitaccounttype" + str(data))
    natwest_api(True)


@socketio.on('speakresponse')
def handle_speak(data):
    print("speak function is called")
    voicecommand()


    # socketio.emit('myresponse', data, callback=messageReceived)


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

    

if __name__ == '__main__':
   app.run('0.0.0.0', 5000, debug = True)