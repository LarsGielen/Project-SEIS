from controller import Robot, Lidar, LidarPoint, Camera
from dataclasses import dataclass
import numpy as np

@dataclass
class Point():
    x: float
    y: float

class Perception():
    def __init__(self, robot: Robot):
        self.robot = robot

        # Lidar
        self.lidar: Lidar = robot.getDevice('LDS-01')
        self.lidar.enable(10)
        self.lidar.enablePointCloud()

        # Camera
        self.camera: Camera = robot.getDevice('camera')
        self.camera.enable(10)

    def getLidarPoints(self) -> list[LidarPoint]:
        ''' Returns all lidar points '''
        return self.lidar.getPointCloud()
    
    def getPointsInRange(self, range: float) -> list[Point]:
        ''' Returns all lidar points that are closer than 'range' meters and the average of these points'''
        lidar_points = self.getLidarPoints()
        squared_distances = np.array([(point.x**2 + point.y**2) for point in lidar_points])
        indices_points_in_range = np.where(squared_distances < range**2)[0]
        
        return [(lidar_points[i].x, lidar_points[i].y) for i in indices_points_in_range]

