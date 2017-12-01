#!/usr/bin/env python
import rospy
from std_msgs.msg import String
### node init 
rospy.init_node('ConsoleNode')

### publich to a topic 
pub = rospy.Publisher('/demo/command', String ,queue_size=10)
rate = rospy.Rate(2)
while not rospy.is_shutdown():
    ### get command from screen  
    string = raw_input("input command please:")
    pub.publish(string)
    rate.sleep()
