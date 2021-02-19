# Author: CodePlayer
# Date: 17.02.2021
# IMPORTANT: You need to install ffmpeg for the audio to video merging to take place!
import ffmpeg
import os
from pytube import YouTube


def download_audio(yt):
    file_name = input("\nWhat should the downloaded audio file be called?\n")
    print("Downloading audio...")
    yt.streams.filter(mime_type="audio/mp4").first().download(filename=file_name)
    print("Done!!")


def download_video(yt, resolution):
    print('''
                              +==============+
                                IMPORTANT!!!
                              +==============+
    The script will download the video and audio to merge them together. 
          Otherwise the video would be without sound (limitations)
    ''')
    print("Downloading video...")
    try:
        yt.streams.filter(res=resolution, mime_type="video/mp4").first().download(filename='temp_v')
    except AttributeError:
        print("The selected resolution is not available\nDownloading the highest resolution...")
        yt.streams.filter(adaptive=True, mime_type="video/mp4").first().download(filename='temp_v')
    print("Done!")
    file_video = ffmpeg.input('temp_v.mp4')
    print("Downloading audio...")
    yt.streams.filter(mime_type="audio/mp4").first().download(filename='temp_a')
    file_audio = ffmpeg.input('temp_a.mp4')
    print("Done!!")
    file_name = input("\nWhat should the downloaded file be called?\n") + '.mp4'
    merging(file_video, file_audio, file_name)
    clearing()


def merging(video, audio, name):
    print("Merging...")
    ffmpeg.concat(video, audio, v=1, a=1).output(name).run()
    print("Done!!")


def clearing():
    print("Removal of residual...")
    os.remove('temp_v.mp4')
    os.remove('temp_a.mp4')
    print("Done!!!")


def get_url():
    while True:
        link = input("Paste (or enter) the link to the YouTube video\n")
        if 'youtube' in link:
            return YouTube(link)
        else:
            print("This is not a link to a YouTube video!\nPlease try again")


def main():
    while True:
        print('''
        =======================================================
             Welcome to Youtube Video Downloader (Beta!!!)
        =======================================================
        
            1. Download video
            2. Download audio
            3. Exit
        ''')
        choice = input("Enter one of the available option: ")
        if choice == '3':
            print("Goodbye!")
            break

        yt = get_url()
        print(f"Title: {yt.title}")
        if choice == '1':
            resolution = input("Specify the resolution you want to download (max for now. 1080p): ")
            download_video(yt, resolution)
        elif choice == '2':
            download_audio(yt)
        else:
            print("Invalid options!\nPlease, try again")


if __name__ == '__main__':
    main()
