import cv2
import numpy as np


def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))


def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)


def change_res(width=320, height=240):
    cap.set(3, width)
    cap.set(4, height)
cap=cv2.VideoCapture(0)
# cap1=cv2.VideoCapture(0)
# cap2=cv2.VideoCapture(0)




# make_480p()
# change_res()


frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# make_720p()
#
# frame_width1= int(cap1.get(3))
# frame_height1 = int(cap1.get(4))
#

# frame_width2 = int(cap2.get(3))
# frame_height2 = int(cap2.get(4))











# out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
# out1 = cv2.VideoWriter('outpy1.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width1, frame_height1))
out2 = cv2.VideoWriter('outpy5.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (frame_width, frame_height))


while True:
    ret,image=cap.read()

    w,h=image.shape[ :2]
    print(w,h)
    cv2.imshow("original_480",image)
    out2.write(image)


    # ret1,image1=cap1.read()
    #
    #
    # w,h=image1.shape[ :2]
    # print(w,h)
    # cv2.imshow("720",image1)
    # out1.write(image1)
    #
    # ret2,image2=cap2.read()
    #
    # w,h=image2.shape[ :2]
    #
    # print(w,h)
    # cv2.imshow("320x240",image2)
    # out2.write(image2)

    key = cv2.waitKey(1) & 0xFF




    # if the `q` key was pressed, break from the loop
    if key == ord("q") or key == ord("Q"):
        break
