#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from tut_msgs.srv import *

roslib.load_manifest('beginner_tutorials')
rospy.init_node('ShapePublisher')


#Create a publisher to publish on the correct topic
#twistPublisher = rospy.Publisher("""add Topic name here""",Twist,queue_size = 100) 
def main():

    while not rospy.is_shutdown():
        rospy.loginfo("In while")
        #Add code here
        rospy.spin() #This will block termination of the program. It can be replaced by rospy.sleep(s), to repeate the while loop every s seconds

 """ Use the method as a callback from the service"""
#def handleShapeSelector(msg):
#    return shapeSelectorResponse() 

""" This method will command the turle to move. x specifies the 
    linear movement and z specifies the rotational movement"""
def cmdTurtle(x,z):
    msg = Twist()
    msg.linear.x = x
    msg.linear.y = 0
    msg.linear.z = 0

    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = z
    rospy.sleep(1)
    #twistPublisher.publish(msg)



if __name__ == '__main__':
    main()
