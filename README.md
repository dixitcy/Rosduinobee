Rosduinobee
===========
This was a small project I did a while ago trying to integrate my Arduino with ROS over Wifi using the Xbee shield for wifi to control a very simple robot

I am using "Arduino Fio" board on the Robot. Advantage of Fio board is that it comes with easy XBee integration.

The XBee communication is not set up to do programming, and I program Arduino Fio using serial programmer

To get commands from ROS over XBEE module, a simple Arduino Subscriber code is written.

Following node will allow sending simple speed commands/PWM commends to the Arduino motor controller over Xbee. 
