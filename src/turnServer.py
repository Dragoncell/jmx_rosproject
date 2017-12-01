#! /usr/bin/env python
import rospy
import math
import time
import actionlib
from geometry_msgs.msg import Twist
from jmx_rosproject.msg import TurnAction, TurnGoal, TurnResult,TurnFeedback

def do_turn(goal):
        ### print current mission 
        print ("Turn action server got a goal, turn "+ str(goal.turnDegree))
        
        ### convert degree to rad, and then set turn speed and update time
        goal_rad = math.radians((math.fabs(goal.turnDegree))%360); 
        angular_z_speed = 0.5
        update_time = 0.1
        
        ### calculate goal time and get start time of Turn  
        start_time = time.time()
        goal_time = abs(goal_rad)/angular_z_speed

         
        ### set the turn speed to vel_msg 
        vel_msg.angular.z = angular_z_speed

        ### while the action is not finished 
        while (time.time() - start_time) < goal_time:

                ### publish speed 
		velocity_publisher.publish(vel_msg)

                ### check whether the mission is preempted by other process 

        	if server.is_preempt_requested():
			result = TurnResult()
		    	result.turnedDegree = math.degrees((time.time()-start_time)*math.fabs(angular_z_speed))
		    	text = "Other process preempted the action, our mission goal is "+str(goal.turnDegree)
		    	server.set_preempted(result,text)
		   	return
                ### calculate turned degree and remained degree to feedback 
                feedback = TurnFeedback()
                feedback.remainDegree = abs(goal_rad) - (time.time()-start_time)*math.fabs(angular_z_speed)
                server.publish_feedback(feedback)
		
                ### let robot turn for update time 0.1s, if it is less than 0.1s to finished, then turn for that time 
		if (goal_time - (time.time()-start_time)) < update_time:       
		    time.sleep(goal_time - (time.time()-start_time))
		else:
		    time.sleep(update_time)

        ### publish 0 speed to robot to make it stop because we have finished the mission and send to result back 
        velocity_publisher.publish(Twist())
        result = TurnResult()
        result.turnedDegree = math.degrees(goal_rad)
        server.set_succeeded(result,"Complete turn mission")
	
### init node 
rospy.init_node('turn_action_server')

### publich Twist to a topic 
velocity_publisher = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)

### set a action server "turn", with do_turn callback
server = actionlib.SimpleActionServer('turn', TurnAction, do_turn, False)
server.start()

### create a vel_msg of Twist 
vel_msg = Twist()

#We wont use linear components so set those to be 0
vel_msg.linear.x=0
vel_msg.linear.y=0
vel_msg.linear.z=0
vel_msg.angular.x = 0
vel_msg.angular.y = 0

rospy.spin()
