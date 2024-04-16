from Modules.videostream_module import VideoStreamServer
from typing import List

class Output():
    def __init__(self) -> None:
        self._video_stream = VideoStreamServer()
        self._video_stream.startServerThreaded()

    def setCameraData(self, camera_data: str):
        self._video_stream.setImageData(camera_data)