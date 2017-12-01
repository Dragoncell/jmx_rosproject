#!/usr/bin/env python
import rospy
import re
from jmx_rosproject.srv import NLPio,NLPioResponse

### get_number callback
def get_number(request):
  result = re.findall("\d+", request.command);
  if len(result)==1 :
  	return NLPioResponse(float(result[0]))
  else:
  	print "command can't be recoginezed"

### node init 
rospy.init_node('fakeNLP_server')

### define get_number service 
service = rospy.Service('get_number', NLPio, get_number)

rospy.spin()

