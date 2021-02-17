# Author: CodePlayer
# Date: 17.02.2021
from pytube import YouTube


def downloading(video):
    print("Downloading...")
    video.streams.filter(progressive=True).first().download()
    print("Download completed :D")


def main():
    print('''
    ========================================================
         Welcome to Youtube Video Downloader (Alpha!!!)
    ========================================================
    ''')
    while True:
        link = input("Paste (or enter) the link to the video you want to download\n"
                     "If you want to leave the script, enter 'q'\n")
        if link.lower() in ['q', 'quit', 'exit']:
            print("Goodbye!")
            break

        yt = YouTube(link)
        print(f"Title: {yt.title}")
        downloading(yt)


if __name__ == '__main__':
    main()
