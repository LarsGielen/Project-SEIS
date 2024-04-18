from Modules.videostream_module import VideoStreamServer
from Modules.lidarstream_module import LidarStreamServer
from Modules.perception_module import Point
from typing import List

class Output():
    def __init__(self) -> None:
        self._video_stream = VideoStreamServer()
        self._video_stream.startServerThreaded()

        self._lidar_stream = LidarStreamServer()
        self._lidar_stream.startServerThreaded()

    def setCameraData(self, camera_data: str):
        self._video_stream.setImageData(camera_data)

    def setLidarData(self, lidar_data: List[Point]):
        self._lidar_stream.setLidarData(lidar_data)