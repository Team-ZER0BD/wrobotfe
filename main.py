import numpy as np
import cv2
import serial


# Sending signals to arduino based on the image data
ser = serial.Serial('/dev/ttyACMO', 9600)
def go(direction):
    if direction == "right":
        ser.write('1')
    elif direction == "left":
        ser.write('2')
    else: ser.write('0')

# Taking video through raspberry pi camera v2
webcam = cv2.VideoCapture(0)

# Looping through all the frames 
while(1):
    
    _, iframe = webcam.read() 

    # Converting the iframe in BGR(RGB color space) to HSV(hue-saturation-value) color space 
    hsv_frame = cv2.cvtColor(iframe, cv2.COLOR_BGR2HSV) 


    # Setting range for red color
    red_lower = np.array([136, 87, 111], np.uint8) 
    red_upper = np.array([180, 255, 255], np.uint8) 
    maskr = cv2.inRange(hsv_frame, red_lower, red_upper) 

    # Set range for green color
    green_lower = np.array([25, 52, 72], np.uint8) 
    green_upper = np.array([102, 255, 255], np.uint8) 
    maskb = cv2.inRange(hsv_frame, green_lower, green_upper) 


    # Bitwise and operator between iframe and mask to detect only that particular color 
    par_color = np.ones((5, 5), "uint8") 


    # For red color 
    maskr = cv2.dilate(maskr, par_color) 
    res_red = cv2.bitwise_and(iframe, iframe, mask = maskr)      

    # For green color 
    maskb = cv2.dilate(maskb, par_color) 
    res_green = cv2.bitwise_and(iframe, iframe, mask = maskb) 

    ar_green = 0
    ar_red = 0
    x_red = 0
    x_green = 0
    
    # Tracking red color 
    contours, hierarchy = cv2.findContours(maskr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    for pic, contour in enumerate(contours): 

        ar1 = cv2.contourArea(contour)
            
        if(ar1 > 1000): 
            x1, y1, w1, h1 = cv2.boundingRect(contour) 
            iframe = cv2.rectangle(iframe, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)
            
            if ar1 > ar_red:
                ar_red = ar1
                x_red = x1
                

  
    # Tracking green color 
    contours, hierarchy = cv2.findContours(maskb, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

    for pic, contour in enumerate(contours):
        
        ar2 = cv2.contourArea(contour)
        if ar2 > ar_green: ar_green = ar2
        if(ar2 > 3000): 
            x2, y2, w2, h2 = cv2.boundingRect(contour)
            iframe = cv2.rectangle(iframe, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 2)
            if ar2 > ar_green:
                ar_green = ar2
                x_green = x2
    
    
    if ar2 > ar1 and abs(320 - x_green) < 50:
        go("left")
    elif ar1 > ar2 and abs(320 - x_red) < 50:
        go("right")
    else:
        go("straight")
    
    # Real time view of the algorithm, uncomment top open a window
    # cv2.imshow("color detection", iframe)
    
    # Program end
    if cv2.waitKey(10) & 0xFF == ord('q'): 
        cap.release() 
        cv2.destroyAllWindows() 
        break