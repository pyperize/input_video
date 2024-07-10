from __future__ import annotations
import src.pipe as pipe
import packages.input_video as input_video
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.manager import Manager
    from src.ui.common.config import ConfigPage

class InputVideoPipe(pipe.Pipe):
    cls_name: str = "Input Video"
    cls_config: type[pipe.Config] = input_video.InputVideoConfig
    cls_function: type[pipe.Function] = input_video.InputVideoFunction

    def __init__(self, name: str, manager: Manager, config: input_video.InputVideoConfig) -> None:
        super().__init__(name, manager, config)
        self.config: input_video.InputVideoConfig = config

    def config_ui(self, manager: Manager, config_page: ConfigPage) -> input_video.InputVideoConfigUI:
        return input_video.InputVideoConfigUI(self, manager, config_page)

    def play(self, manager: Manager) -> None:
        if self.playing:
            return
        self.playing = True
        if self.config.pipe: self.config.pipe.play(manager)

    def stop(self, manager: Manager, result) -> None:
        if not self.playing:
            return
        self.playing = False
        if self.config.pipe: self.config.pipe.stop(manager, result)
