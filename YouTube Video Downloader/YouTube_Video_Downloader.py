# Author: CodePlayer
# Date: 17.02.2021
# IMPORTANT: You need to install ffmpeg for the audio to video merging to take place!
import ffmpeg
import os
import time
from pytube import YouTube


def download_video(choice, yt, resolution):
    file_name = input("What should the downloaded file be called? (Can't contain spaces!)?\n")
    print("Downloading video...")
    yt.streams.filter(res=resolution, mime_type="video/mp4").first().download(filename=file_name)
    print("Done!")

    if resolution not in ['240p', '360p'] and choice == '1':
        print('''
                                      +==============+
                                        IMPORTANT!!!
                                      +==============+
        Because you have selected a video with audio at a resolution higher than 360p 
        we also need to download the audio to merge it with the video (limitations)
        ''')
        file_video = ffmpeg.input(file_name + ".mp4")
        time.sleep(7)
        print("Downloading audio...")
        yt.streams.filter(mime_type="audio/mp4").first().download(filename="temp_a")
        file_audio = ffmpeg.input('temp_a.mp4')
        print("Done!!")
        merging(file_video, file_audio, file_name + "(M).mp4")
        clearing(file_name + ".mp4")


def merging(video, audio, file_name):
    print("Merging...")
    ffmpeg.concat(video, audio, v=1, a=1).output(file_name).run()
    print("Done!!")


def clearing(file_name):
    print("Removal of residual...")
    os.remove(file_name)
    os.remove('temp_a.mp4')
    print("Done!!!")


def main():
    while True:
        print('''
        ========================================================
             Welcome to Youtube Video Downloader (Alpha!!!)
        ========================================================
        
            1. Download video w/ audio
            2. Download video w/o audio
            3. Download only audio
            4. Exit
        ''')
        choice = input("Enter one of the available option: ")
        if choice == '4':
            print("Goodbye!")
            break

        link = input("Please paste (or enter) the link from where you want to download the video\n")
        yt = YouTube(link)
        print(f"Video title: {yt.title}")
        if choice in ['1', '2']:
            resolution = input("Specify the resolution you want to download (max for now. 1080p): ")
            download_video(choice, yt, resolution)
        elif choice == '3':
            print("WIP")
        else:
            print("Invalid options!\nPlease, try again")


if __name__ == '__main__':
    main()
