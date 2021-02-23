# Author: CodePlayer
# Date: 23.02.2021
from pathlib import Path

host_path = r"C:\Windows\System32\drivers\etc\hosts"
blocked_sites = []
website = Path('website.txt')


def load_file():
    global blocked_sites
    with open(website, 'r') as f:
        lines = f.read().split('\n')
        blocked_sites = [l.strip() for l in lines if len(l) > 0]


def unblock():
    load_file()
    with open(host_path, 'r+') as hostfile:
        hosts = hostfile.readlines()
        hostfile.seek(0)
        for host in hosts:
            if not any(site in host for site in blocked_sites):
                hostfile.write(host)
        hostfile.truncate()
    print("Unblocked websites:")
    for _, site in enumerate(blocked_sites):
        print(f"> {site}")

    input("\nEnter anything to exit \n> ")


if __name__ == '__main__':
    unblock()