
## Ros Project Info
There are main four nodes in this project, they are  FakeNLP, TurnServer, MainNode, and ConsoleNode. 

### Run Project
You can clone this repository from git to your own workspace by:
```
$ cd ~/catkin_ws/src
$ git clone <my git hub repo>
```
Go back to catkin_ws and build the packages in the workspace by running catkin_make command:
```
$ cd ..
$ catkin_make
```
Now you can run the solution by launch file:
```
$ roslaunch jmx_rosproject project.launch
```
If launched successfully, you will see the line "Input command please:",

now type in command to activate the console reader. For example:
```
$ turn 84
```
### Test Project
Turn on the gazebo simulator: 
```
$ roslaunch turtlebot_gazebo turtlebot_world.launch
```
You can see it in simulator and also can play with it in real world.
