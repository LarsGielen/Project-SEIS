"""robot_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from Modules.input_module import Input
from Modules.movement_module import Movement
from Modules.perception_module import Perception
from Webots.Project.controllers.robot_controller.Modules.videostream_module import VideoStreamServer
import numpy as np
import math

# create the Robot instance.
robot = Robot()

input = Input()
movement = Movement(robot, 6.5)
perception = Perception(robot)
video_stream = VideoStreamServer()
video_stream.startServerThreaded()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:

    # Process sensor data here.
    lidar_points = perception.getPointsInRange(0.3)

    if len(lidar_points) == 0:
        movement.move(input.input_data.direction_forward, input.input_data.direction_right)
    else:
        movement.move(0, 0)
        average_point = np.mean(lidar_points, axis=0)
        if (int(math.copysign(1, input.input_data.direction_forward)) != int(math.copysign(1, average_point[0])) or input.input_data.direction_forward == 0):    
            movement.move(input.input_data.direction_forward, input.input_data.direction_right)

    video_stream.setImageData(perception.getCameraImageData())

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
