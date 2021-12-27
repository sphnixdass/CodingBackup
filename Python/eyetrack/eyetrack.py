# import the necessary packages
from imutils import face_utils
import dlib
import cv2
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
def captureEye():
    p = "shape_predictor_68_face_landmarks.dat"
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(p)
    j =1
    # load the input image and convert it to grayscale
    cap = cv2.VideoCapture(0)
    while True:
        #image = cv2.imread("example.jpg")
        ret, image = cap.read()
        orgimg = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # detect faces in the grayscale image
        rects = detector(gray, 0)
        eyetop =0
        eyebottom =0
        eyeleft =0
        eyeright =0 
        # loop over the face detections
        for (i, rect) in enumerate(rects):
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            
            _, eyetop = shape[44]
            _, eyebottom = shape[47]
            eyeleft, _ = shape[42]
            eyeright, _ = shape[46]

            # loop over the (x, y)-coordinates for the facial landmarks
            # and draw them on the image
            for (x, y) in shape:
                cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
    # show the output image with the face detections + facial landmarks
        print(eyetop, eyebottom, eyeleft, eyeright)
        if eyetop != 0 and eyebottom != 0 and eyeleft !=0 and eyeright !=0:
            orggray = cv2.cvtColor(orgimg, cv2.COLOR_BGR2GRAY)
            roi = orggray[eyetop:eyebottom+5, eyeleft:eyeright+5]
            cv2.imshow("roi output", roi)
            cv2.imwrite("img/" + str(j) + "output.jpg",roi)
            j +=1

        cv2.imshow("Output", image)
        key = cv2.waitKey(30)
        if key == 27:
            break

    cv2.destroyAllWindows()


def find_eye_location():
    gray = cv2.imread("27output.jpg", 0)
    gray_filtered = cv2.inRange(gray, 50, 255)
    while True:
        cv2.imshow("Output", gray_filtered)
        key = cv2.waitKey(30)
        if key == 27:
            break
    cv2.destroyAllWindows()

#find_eye_location()
captureEye()