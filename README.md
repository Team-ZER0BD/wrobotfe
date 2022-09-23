# wrobotfe
Here we have the dumbbot version 1.0, designed to operate faultlessly on the WRO FE field, regardless of whether there are obstacles. The portable automobile can drive itself around the field track for a few laps due to its simulation of analog sensors and OpenCV software.
 
The boundaries of the Future Engineer track will be identified with the assistance of a Sonar Sensor HC-Sr04 model. The HC-Sr04 does not have a wide field of vision when spotting any impediment or item. Because of this, we have installed three of these sensors in our automobile. There have been three different uses for them in front of the automobile, all of which have been in separate directions. To ensure that everything runs well, the sensors have been oriented in a variety of ways in order to determine the distance between the left and right walls.
 
In order to exercise control over the car's two DC motors, an Arduino Uno has been installed in the vehicle. The sonar sensors communicate with the Arduino Uno, which assists the car in achieving the ideal movement.
 
L298n is an introductory go-to for any new person interested in robotics. Two of these simple motor drivers have been put into operation. They were configured to control not only the motor attached to our rear wheels but also the steering motor attached to our front wheels. In order to achieve the smoothest movement possible on the track, two DC motors were assembled with two separate motor drivers.
 
 
 
The dumbbot v1.0 has been outfitted with a total of four rubber wheels. Rubber wheels were used for this project due to their superior gripping ability. The fact that the rubber wheels do not abruptly slip explains why this is such a good option for the automobile.
 
 
 
The dumbbot v1.0 has a Central processing unit that is a Raspberry Pi 3B+ model. The primary purpose of this system is to obtain data from the camera module. The information received from the camera module contributes to the process of identifying the Red and Green colored obstacles that are approaching it. At the very instant of detecting any red block, the program will immediately rotate the vehicle around so that it is facing in the correct direction. In addition, if it finds an obstruction that is green in color, the vehicle will turn to the left. A USB port was utilized in order to establish communication between the Raspberry Pi 3B+ model and the Arduino Uno. The Raspberry Pi 3B+ microprocessor and the Arduino Uno have been powered by a portable power supply (Power bank).
 
Camera module: Considering that our microcontroller board is a Raspberry pi, we planned to utilize a Raspberry pi camera module 2 since it is ideally suited for the task at hand. The camera has been positioned above the automobile to provide an unobstructed view of the surrounding region. The camera incorporated with the Raspberry Pi has been calibrated to detect the motion of the red and green blocks as they go along the track in a smooth and consistent manner.
 
The Motion sensor: 10 DOF IMU Sensor (B) is excellent at motion monitoring. It was created to detect and measure the position, height, and temperature while burning the field track because it offers exceptional man-machine interaction. In addition, it is good at monitoring motion.
 
Arduino Uno and a proto shield are two more fundamental components of robotics utilized in this project to control our motor drivers and put the whole thing together.
 
Because our country lacked access to the vast majority of long-lasting robotics technology, we were forced to construct self-driving vehicles using whatever resources were available. We wanted to go about the field without any problems; therefore, we reduced the amount of velocity to the lowest possible level.
