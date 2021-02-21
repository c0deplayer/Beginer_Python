# Author: CodePlayer
# Date: 21.02.2021
# IMPORTANT: You need to install ffmpeg for the audio to video merging to take place!
import ffmpeg
import pathlib


def processing(name_video, path_video, path_audio):
    stream_video = ffmpeg.input(path_video)
    stream_audio = ffmpeg.input(path_audio)
    print("Merging...")
    ffmpeg.output(stream_video, stream_audio, name_video).run()
    print("Removing the cache files...")
    pathlib.Path(path_video).unlink()
    pathlib.Path(path_audio).unlink()
    print("Done!!!")
