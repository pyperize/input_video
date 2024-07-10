from __future__ import annotations
from packages.input_video.config import InputVideoConfig, InputVideoConfigUI
from packages.input_video.function import InputVideoFunction, InputVideoOutput
from packages.input_video.pipe import InputVideoPipe
from src.package.package import Package
from typing import TYPE_CHECKING, Iterable
if TYPE_CHECKING:
    from src.pipe import Pipe

class InputVideoPackage(Package):
    name: str = "Input Video"
    _pipes: Iterable[type[Pipe]] = [InputVideoPipe]
    dependencies: dict[str, Package] = {}
