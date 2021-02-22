# Author: CodePlayer
# Date: 17.02.2021
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import convert
import pathlib


def download_audio(yt):
    name_audio = input("\nWhat should the downloaded audio file be called?\n")
    print("Downloading audio...")
    yt.streams.filter(mime_type="audio/mp4").first().download(filename=name_audio)


def download_video(yt, res):
    print('''
                              +==============+
                                IMPORTANT!!!
                              +==============+
    The script will download the video and audio to merge them together. 
          Otherwise the video would be without sound (limitations)
    ''')
    print("Downloading video...")
    yt.streams.filter(res=res, mime_type="video/mp4").first().download(output_path='Cache',
                                                                       filename='temp_v')
    print("Downloading audio...")
    yt.streams.filter(mime_type="audio/mp4").first().download(output_path='Cache',
                                                              filename='temp_a')
    join_files()


def join_files():
    name_video = input("\nWhat should the downloaded file be called?\n") + '.mp4'
    path_video = pathlib.Path("Cache").joinpath("temp_v.mp4")
    path_audio = pathlib.Path("Cache").joinpath("temp_a.mp4")
    convert.processing(name_video, path_video, path_audio)


def show_info(yt):
    global res_list
    res_list = []
    for x in yt.streams.filter(adaptive=True, file_extension='mp4'):
        check = x.resolution
        if check is None:
            pass
        else:
            res_list.append(check)

    print(f'''
    Information:
    > Title: {yt.title}
    > Author: {yt.author}
    > Resolutions: ''', end="")
    print(*res_list, sep=", ")


def get_res(yt):
    while True:
        resolution = input("\nEnter the resolution you want to download: ")
        if resolution in res_list:
            return resolution

        print("This resolution is not available")


def get_url():
    while True:
        try:
            link = input("Paste (or enter) the link to the YouTube video\n")
            return YouTube(link)
        except RegexMatchError:
            print("This is not a link to the YouTube video or the link is incorrect"
                  "\nPlease try again")


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

        if choice == '1':
            yt = get_url()
            show_info(yt)
            res = get_res(yt)
            download_video(yt, res)
        elif choice == '2':
            yt = get_url()
            show_info(yt)
            download_audio(yt)
        else:
            print("Invalid options!\nPlease, try again")


if __name__ == '__main__':
    main()
