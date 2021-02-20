# Author: CodePlayer
# Date: 17.02.2021
# IMPORTANT: You need to install ffmpeg for the audio to video merging to take place!
from pytube import YouTube
import ffmpeg
import pathlib


def download_audio(yt):
    file_name = input("\nWhat should the downloaded audio file be called?\n")
    print("Downloading audio...")
    yt.streams.filter(mime_type="audio/mp4").first().download(filename=file_name)


def download_video(yt, res):
    print('''
                              +==============+
                                IMPORTANT!!!
                              +==============+
    The script will download the video and audio to merge them together. 
          Otherwise the video would be without sound (limitations)
    ''')
    print("Downloading video...")
    try:
        yt.streams.filter(res=res, mime_type="video/mp4").first().download(output_path='Cache',
                                                                           filename='temp_v')
    except AttributeError:
        print("The selected resolution is not available\nDownloading the highest resolution...")
        yt.streams.filter(adaptive=True, mime_type="video/mp4").first().download(output_path='Cache',
                                                                                 filename='temp_v')
    print("Downloading audio...")
    yt.streams.filter(mime_type="audio/mp4").first().download(output_path='Cache',
                                                              filename='temp_a')
    processing()


def processing():
    name_video = input("\nWhat should the downloaded file be called?\n") + '.mp4'
    path_video = pathlib.Path("Cache").joinpath("temp_v.mp4")
    path_audio = pathlib.Path("Cache").joinpath("temp_a.mp4")
    stream_video = ffmpeg.input(path_video)
    stream_audio = ffmpeg.input(path_audio)
    print("Merging...")
    ffmpeg.output(stream_video, stream_audio, name_video).run()
    print("Removing the cache files...")
    pathlib.Path(path_video).unlink()
    pathlib.Path(path_audio).unlink()
    print("Done!!!")


def get_res(yt):
    global res_list
    res_list = []
    for x in yt.streams.filter(adaptive=True):
        check = x.resolution
        if (check is None) or (check in res_list):
            pass
        else:
            res_list.append(check)
    return res_list


def get_url():
    while True:
        link = input("Paste (or enter) the link to the YouTube video\n")
        if 'youtube' not in link:
            print("This is not a link to a YouTube video!\nPlease try again")
        else:
            return YouTube(link)


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
        print(f"Title: {yt.title} \nAuthor: {yt.author}")
        if choice == '1':
            print("Available resolutions:")
            print(*get_res(yt))
            res = input("Enter the resolution you want to download: ")
            download_video(yt, res)
        elif choice == '2':
            download_audio(yt)
        else:
            print("Invalid options!\nPlease, try again")


if __name__ == '__main__':
    main()
