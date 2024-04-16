from typing import List
from controller import Robot, Lidar, LidarPoint, Camera
from dataclasses import dataclass
import numpy as np

@dataclass
class Point():
    x: float
    y: float

class Perception():
    def __init__(self, robot: Robot):
        self._robot = robot

        # Lidar
        self._lidar: Lidar = robot.getDevice('LDS-01')
        self._lidar.enable(10)
        self._lidar.enablePointCloud()

        # Camera
        self._camera: Camera = robot.getDevice('camera')
        self._camera.enable(10)

    def getLidarPoints(self) -> List[LidarPoint]:
        ''' Returns all lidar points '''
        return self._lidar.getPointCloud()
    
    def getPointsInRange(self, range: float) -> List[Point]:
        ''' Returns all lidar points that are closer than 'range' meters and the average of these points'''
        lidar_points = self.getLidarPoints()
        squared_distances = np.array([(point.x**2 + point.y**2) for point in lidar_points])
        indices_points_in_range = np.where(squared_distances < range**2)[0]
        
        return [(lidar_points[i].x, lidar_points[i].y) for i in indices_points_in_range]
    
    def getCameraCameraData(self) -> List[List[List[int]]]:
        return self._camera.getImageArray()

