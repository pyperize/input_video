# Input Video pipe for pyperize
Using OpenCV Video Capture and FFmpeg

## Prerequisites
- FFmpeg

## Install

1. Copy this package into ```./packages/```
2. Edit ```./packages/__init__.py``` to import the package
3. Add the package name and instance to the ```PACKAGES``` global variable in ```./packages/__init__.py```

```./packages/__init__.py``` should contain something like this where ```...``` are the other packages

```
from src.package import Package
from packages import (
    ...
    input_video,
    ...
)

PACKAGES: dict[str, Package] = {
    ...
    input_video.InputVideoPackage.name: input_video.InputVideoPackage(),
    ...
}
```
