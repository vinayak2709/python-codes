
import numpy as np
import cv2
import os
import imutils

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp"
#cap = cv2.VideoCapture("rtsp://admin:admin123@192.168.0.10:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif")
#cap = cv2.VideoCapture("rtsp://admin:incerno123@192.168.1.36:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif")
#cap = cv2.VideoCapture("rtsp://192.168.0.123:8080/h264_ulaw.sdp")
#cap = cv2.VideoCapture('v4l2src device=/dev/video0 ! video/x-raw,framerate=20/1 ! videoscale ! videoconvert ! appsink', cv2.CAP_GSTREAMER)
#cap = cv2.VideoCapture('1.mp4')
cap = cv2.VideoCapture('rtspsrc location=rtsp://192.168.1.51:8080/h264_ulaw.sdp latency=20 ! rtph264depay ! h264parse ! omxh264dec ! nvvidconv ! video/x-raw, width=(int)640, height=(int)480, format=(string)BGRx ! videoconvert ! appsink', cv2.CAP_GSTREAMER)
#cap = cv2.VideoCapture('rtspsrc location=rtsp://192.168.0.8:8080/h264_ulaw.sdp latency=20 ! rtph264depay ! h264parse ! avdec_h264 ! autovideoconvert ! autovideosink', cv2.CAP_GSTREAMER)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret==True:
        # Display the resulting frame
        frame = imutils.resize(frame, width=800)
        cv2.imshow('frame',frame)

    else:
        cap = cv2.VideoCapture(
            'rtspsrc location=rtsp://admin:incerno123@192.168.1.36:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif latency=20 ! rtph264depay ! h264parse ! omxh264dec ! nvvidconv ! video/x-raw, width=(int)640, height=(int)480, format=(string)BGRx ! videoconvert ! appsink',           cv2.CAP_GSTREAMER)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
