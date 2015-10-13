#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import Twist


roslib.load_manifest('beginner_tutorials')
rospy.init_node('ShapePublisher')



def main():
    twistPublisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 100)
    rate = rospy.Rate(1)
    i = 0
    while not rospy.is_shutdown():
        rospy.loginfo("In while")
        msg = Twist()
        msg.linear.x = 0
        msg.linear.y = 0
        msg.linear.z = 0

        msg.angular.x = i
        msg.angular.y = 0
        msg.angular.z = 0
        rospy.loginfo(msg)
        twistPublisher.publish(msg)
        i= i+1
        rate.sleep()

if __name__ == '__main__':
    main()
