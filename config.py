from __future__ import annotations
import flet as ft
from typing import TYPE_CHECKING
from src.ui.pipe import PipeTile
if TYPE_CHECKING:
    from src.manager import Manager
    from src.ui.common import ConfigPage
    import packages.input_video as input_video
    import src.pipe as pipe
from src.pipe import Pipe, Config, ConfigUI

class InputVideoConfig(Config):
    pipe: Pipe | None = None
    src: str = "0"
    cap_x: int = 1280
    cap_y: int = 720
    crop_x: int = 1280
    crop_y: int = 720
    fps: int = 10

class InputVideoConfigUI(ConfigUI):
    def __init__(self, instance: input_video.InputVideoPipe, manager: Manager, config_page: ConfigPage) -> None:
        super().__init__(instance, manager, config_page)
        self.instance: input_video.InputVideoPipe = instance
        self.pipe = PipeTile(
            "Pipe",
            self.manager,
            self.config_page,
            self.select_pipe,
            self.delete_pipe,
            self.instance.config.pipe,
        )
        self.content: ft.Column = ft.Column([
            self.pipe,
            ft.TextField(self.instance.config.src, label="Video Source", border_color="grey"),
            ft.TextField(self.instance.config.cap_x, label="Capture Width", border_color="grey", input_filter=ft.NumbersOnlyInputFilter()),
            ft.TextField(self.instance.config.cap_y, label="Capture Height", border_color="grey", input_filter=ft.NumbersOnlyInputFilter()),
            ft.TextField(self.instance.config.crop_x, label="Crop Width", border_color="grey", input_filter=ft.NumbersOnlyInputFilter()),
            ft.TextField(self.instance.config.crop_y, label="Crop Height", border_color="grey", input_filter=ft.NumbersOnlyInputFilter()),
            ft.TextField(self.instance.config.fps, label="Frame(s) per Second", border_color="grey", input_filter=ft.NumbersOnlyInputFilter()),
        ])

    def select_pipe(self, cls: type[pipe.Pipe] | pipe.Pipe) -> pipe.Pipe:
        if isinstance(cls, type):
            cls: pipe.Pipe = cls(cls.cls_name, self.manager, cls.cls_config())
        return cls

    def delete_pipe(self, e) -> None:
        self.pipe.pipe_selector.value = None
        self.pipe.select_changed(None)
        self.update()

    def dismiss(self) -> None:
        self.instance.config = InputVideoConfig(
            pipe=self.pipe.instance,
            src=self.content.controls[1].value,
            cap_x=int(self.content.controls[2].value),
            cap_y=int(self.content.controls[3].value),
            crop_x=int(self.content.controls[4].value),
            crop_y=int(self.content.controls[5].value),
            fps=int(self.content.controls[6].value),
        )
