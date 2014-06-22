#!/usr/bin/env python
import roslib; roslib.load_manifest('beginner_tutorials')
import rospy
from std_msgs.msg import Float64


def talker():
	pubL = rospy.Publisher('servoleft', Float64)
	pubR = rospy.Publisher('servoright', Float64)
	rospy.init_node('OctoroachCommand')
	while not rospy.is_shutdown():
		commandL = input('Please enter a Left speed between 0.0 - 255.0:')
		commandR = input('Please enter a Right speed between 0.0 - 255.0:')
#rospy.loginfo(commandL)
#rospy.loginfo(commandR)
pubL.publish(commandL)
pubR.publish(commandR)
rospy.sleep(1.0)
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException: pass