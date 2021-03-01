# Author: CodePlayer
# Date: 21.02.2021
# IMPORTANT: You need to install ffmpeg-python
from pathlib import Path
import ffmpeg


def processing(name_video, path_video, path_audio):
    stream_video = ffmpeg.input(path_video)
    stream_audio = ffmpeg.input(path_audio)
    print("Merging...")
    ffmpeg.output(stream_video, stream_audio, name_video).run()
    Path(path_video).unlink()
    Path(path_audio).unlink()
    print("Removing the cache files...")
    print("Done!!!")
