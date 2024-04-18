"""robot_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from Modules.input_module import Input
from Modules.movement_module import Movement
from Modules.perception_module import Perception
from Modules.output_module import Output
from Modules.videostream_module import VideoStreamServer
import numpy as np
import math
from PIL import Image
# create the Robot instance.
robot = Robot()

input = Input()
movement = Movement(robot, 6.5)
perception = Perception(robot)
output = Output()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    lidar_points = perception.getPointsInRange(0.3)

    # Move Based on input and sensor values
    if len(lidar_points) == 0:
        movement.move(input.input_data.direction_forward, input.input_data.direction_right)
    else:
        movement.move(0, 0)
        average_point = np.mean(lidar_points, axis=0)
        if (int(math.copysign(1, input.input_data.direction_forward)) != int(math.copysign(1, average_point[0])) or input.input_data.direction_forward == 0):
            movement.move(input.input_data.direction_forward, input.input_data.direction_right)

    # Send sensor data to interface
    output.setCameraData(perception.getCameraCameraData())

    # Send lidar data to the interface
    output.setLidarData(perception.getPointsInRange(3))

# Enter here exit cleanup code.
