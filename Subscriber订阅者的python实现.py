#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

def wang_callback(msg):
    rospy.loginfo(msg.data)

def zhang_callback(msg):
    rospy.logwarn(msg.data)

if __name__ =="__main__":
    rospy.init_node("wo_node")

    sub = rospy.Subscriber("HNU",String,wang_callback,queue_size=10)
    sub2 = rospy.Subscriber("DLU",String,wang_callback,queue_size=10)

    rospy.spin()



