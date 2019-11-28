import cv2
import matplotlib
import numpy as np



line_coord1=(100, 0)
line_coord2=(200, 800)
point_coord=(10, 100)








matplotlib.use('Agg')

def is_above(point, line_coord1, line_coord2):
    if np.cross(point - line_coord1, line_coord2 - line_coord1) < 0:
        return True
    else:
        return False
w=800
h=600

frame=cv2.imread('basic_shapes2.png')






cv2.line(frame, (line_coord1), (line_coord2), (200, 200, 0), 4)
cv2.line(frame, (point_coord), (point_coord), (0, 200, 0), 10)


a = np.array([line_coord1])  # [x,y]
b = np.array([line_coord2])  # [x,y](100, 100)
p1 = np.array(point_coord)

if not is_above(p1, b, a):
    print('below')
else:
    print('above')

cv2.imshow("Frame", frame)
cv2.waitKey(0)