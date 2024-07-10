from __future__ import annotations
from typing import Iterable, Generator
import numpy as np
import cv2
from packages.input_video import InputVideoConfig
from src.pipe.function import IO, Function

class InputVideoOutput(IO):
    frame: np.ndarray = np.array([[[0, 0, 0]]])

class InputVideoFunction(Function):
    cls_input: type[IO] = IO
    cls_output: type[InputVideoOutput] = InputVideoOutput
    def __init__(self, config: InputVideoConfig) -> None:
        self.config: InputVideoConfig = config
        if self.config.src.isdigit():
            src = int(self.config.src)
        else:
            src = self.config.src
        self.vc = cv2.VideoCapture(src)
        self.vc.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.vc.set(cv2.CAP_PROP_FRAME_WIDTH, self.config.cap_x)
        self.vc.set(cv2.CAP_PROP_FRAME_HEIGHT, self.config.cap_y)
        self.vc.set(cv2.CAP_PROP_FPS, self.config.fps)
        self.crop = (self.config.crop_x != self.config.cap_x) or (self.config.crop_y != self.config.cap_y)
        self.inner = self.config.pipe.cls_function(self.config.pipe.config) if self.config.pipe else None

    def __call__(self, input: IO) -> IO:
        if self.inner is not None:
            try:
                while True:
                    _, img = self.vc.read()
                    if img is None:
                        print("Input video unavailable")
                        break
                    if self.crop:
                        img = img[:self.config.crop_y,:self.config.crop_x]
                    self.inner(InputVideoOutput(frame=img))
            except Exception as e:
                raise e
            finally:
                self.vc.release()
        return IO()
