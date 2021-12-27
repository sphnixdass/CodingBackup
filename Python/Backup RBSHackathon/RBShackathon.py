from flask import Flask, render_template, request, url_for, redirect, Response
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO
import speech_recognition as sr
import cv2
import time
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
Bootstrap(app)

tempvar = "hi dass"
 
def rbs_api():
    url = "https://api.natwest.useinfinite.io/.well-known/openid-configuration"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
    return response.text.encode('utf8')


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

@app.route('/loginpage')
def loginpage():
    return render_template('loginpage.html')

@app.route('/main_webpage', methods=['GET', 'POST'])
def main_webpage():
   return render_template('main_webpage.html')


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