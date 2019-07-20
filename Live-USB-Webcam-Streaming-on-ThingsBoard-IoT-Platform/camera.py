from os import system

import cv2
haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
         self.video = cv2.VideoCapture(0)
         self.frameWidth = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
         self.frameHeight = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        image_gray = cv2.cvtColor(image, cv2.FONT_HERSHEY_SIMPLEX)
        faces_rects = haar_cascade_face.detectMultiScale(image_gray, scaleFactor=1.3, minNeighbors=10,minSize=(75, 75));

        for (x, y, w, h) in faces_rects:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if len(faces_rects) > 0:
            cv2.putText(img = image, text = 'Faces found:' + str(len(faces_rects)), org=(50,50), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 0, 255))
            system("echo  '%s %s' > data.txt" % (len(faces_rects), 1 ))
        else:
            system("echo '%s %s' > data.txt " % (len(faces_rects), 0 ))
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
