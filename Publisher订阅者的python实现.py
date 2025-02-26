#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String


if __name__ =="__main__":
    rospy.init_node("wang_node")
    rospy.logwarn("start.")

    pub = rospy.Publisher("HNU1",String,queue_size=10)
    
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo("msg sending")
        msg = String()
        msg.data = "test"
        pub.publish(msg)
        rate.sleep()
