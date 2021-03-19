# Author: CodePlayer
# Date: 17.02.2021
# IMPORTANT: You need to install ffmpeg-python and pytube
from pytube import YouTube
from pathlib import Path
import convert
import re
cache = Path("Cache")


def check_folder():   # If 'Cache' folder doesn't exist, it will be created
    if not Path.exists(cache):
        Path(cache).mkdir(parents=True, exist_ok=False)
        print("Cache folder does not exist or has been deleted \nCreating...")


def download_video(yt, resolution, file_ext):   # Downloads video and audio file
    print('''
                              +==============+
                                IMPORTANT!!!
                              +==============+
    The script will download the video and audio to merge them together. 
          Otherwise the video would be without sound (limitations)
    ''')
    print("Downloading video...")
    stream = yt.streams.filter(res=resolution, file_extension=file_ext).first()
    stream.download(output_path=cache, filename='temp_v')
    print("Downloading audio...")
    stream = yt.streams.filter(file_extension=file_ext, type="audio").first()
    stream.download(output_path=cache, filename='temp_a')


def join_files(file_ext):   # Merges the files
    name_video = sanitised_input(
        "\nWhat should the downloaded file be called?\n", r"^[\w\-.]*$") + f".{file_ext}"
    path_video = Path(cache).joinpath("temp_v." + file_ext)
    path_audio = Path(cache).joinpath("temp_a." + file_ext)
    convert.processing(name_video, path_video, path_audio)


def show_info(yt, file_ext):   # Shows information about video (title, author, available resolutions)
    global res_reg
    res_list = []
    for x in yt.streams.filter(adaptive=True, file_extension=file_ext):
        check = x.resolution
        if (check is None) or (check in res_list):
            pass
        else:
            res_list.append(check)

    print(f'''
    Information:
    > Title: {yt.title}
    > Author: {yt.author}
    > Resolutions: ''', end="")
    print(*res_list, sep=", ")
    res_reg = "(" + ")|(".join(res_list) + ")"


def sanitised_input(prompt, regex):   # Validates the entered data
    while True:
        value = input(prompt)
        if re.match(regex, value):
            return value
        print(f"Invalid input \nPlease, try again")


def main():   # Main menu
    while True:
        print('''
        ===================================================
                Welcome to Youtube Video Downloader
        ===================================================
        ''')
        yt = YouTube(sanitised_input("Paste the link to the YouTube video\n",
                                     r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]{11})(\S+)?$"))
        file_ext = sanitised_input(
            "Select the file extension [mp4/webm]: ", r"(mp4)|(webm)")
        show_info(yt, file_ext)
        resolution = sanitised_input(
            "\nEnter the resolution you want to download: ", res_reg)
        download_video(yt, resolution, file_ext)
        join_files(file_ext)

        leave = input("Do you want to leave the program? [y/n] ").lower()
        if leave in {'y', 'yes'}:
            print("Have a good day/night!")
            break


if __name__ == '__main__':
    check_folder()
    main()
