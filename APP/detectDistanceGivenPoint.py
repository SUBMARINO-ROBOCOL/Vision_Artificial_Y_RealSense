import cv2
import pyrealsense2
from realsense_depth import *

#Inicia la cámara
dc = DepthCamera()

while True:
    ret, depth_frame, color_frame = dc.get_frame ()
    
    # Muestra la distancia de un punto en específico defindo por las coordenadas de la variable point.
    point = (400, 300)
    cv2.circle(color_frame, point, 4, (0, 0, 255))
    distance = depth_frame [point[1], point [0]]
    print (distance) cv2.imshow("depth frame", depth_frame)
    
    
    cv2.imshow ("Color frame", color_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break