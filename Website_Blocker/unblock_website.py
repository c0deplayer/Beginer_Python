# Author: CodePlayer
# Date: 23.02.2021
from pathlib import Path
import platform

blocked_sites = []
website = Path('website.txt')


def h_path():   # Returns the path to the hosts file depending on your system
    if platform.system() == 'Windows':
        path = r"C:\Windows\System32\drivers\etc\hosts"
    elif platform.system() == 'Linux':
        path = "/etc/hosts"
    return path


def load_file():   # Loads 'website.txt'
    global blocked_sites
    with open(website, 'r') as f:
        lines = f.read().split('\n')
        blocked_sites = [l.strip() for l in lines if len(l) > 0]


def unblock(): # Unblocks websites by overwriting the hosts file
    load_file()
    path = h_path()
    with open(path, 'r+') as hostfile:
        hosts = hostfile.readlines()
        hostfile.seek(0)
        for host in hosts:
            if not any(site in host for site in blocked_sites):
                hostfile.write(host)
        hostfile.truncate()
    print("Unblocked websites:")
    for _, site in enumerate(blocked_sites):
        print(f"> {site}")

    input("\nEnter anything to exit\n> ")


if __name__ == '__main__':
    unblock()
