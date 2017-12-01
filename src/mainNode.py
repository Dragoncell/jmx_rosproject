#!/usr/bin/env python
import rospy
from jmx_rosproject.srv import NLPio
from std_msgs.msg import String
from jmx_rosproject.msg import TurnAction, TurnGoal,TurnResult, TurnFeedback
import actionlib
import math

class MainNode():
	def __init__(self):
		### start 
		rospy.init_node('mainNode') 

		### setup NLP service
		rospy.wait_for_service('get_number')
		self.getNumber = rospy.ServiceProxy('get_number', NLPio) 

		### setup turn action server
		self.turn_client = actionlib.SimpleActionClient("turn",TurnAction)
		self.turn_client.wait_for_server()

		### listern to the command console
		self.sub = rospy.Subscriber('/demo/command', String, self.callback)

	def feedback(self,feedback):
		rospy.loginfo('Degree left '+ str(math.degrees(feedback.remainDegree)) + ' degree.')	
	
        def run(self):
	 	rospy.spin()

	def callback(self,msg):
		words = msg.data
		number = self.getNumber(words)
		print "get degree number"+ str(number.number)
                 
		goal = TurnGoal()
		goal.turnDegree = float(number.number)
		self.turn_client.send_goal(goal, feedback_cb=self.feedback)
		
		self.turn_client.wait_for_result()
		rospy.loginfo('Degree turned: %s' % (self.turn_client.get_result().turnedDegree))


MainNode().run()
