# Author: CodePlayer
# Date: 23.02.2021
import ctypes
import sys
import time
blocked_sites = []
default_host = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def input_sites():
    done = 1
    print("Enter either the page to be blocked or 'q' to complete the data entry")
    while done:
        site = input()
        if site.lower() in {'q', 'quit', 'stop'}:
            done = 0
        else:
            blocked_sites.append(site)


def main():
    if is_admin():
        input_sites()
        while True:
            print("\nBlocking sites...")
            with open(default_host, 'r+') as hostfile:
                hosts = hostfile.read()
                for site in blocked_sites:
                    if site not in hosts:
                        hostfile.write(f"{redirect} {site}\n")
            end = input("Enter 'y' to stop the script: ").lower()
            if end in {'y', 'yes'}:
                print("Unblocking sites...")
                with open(default_host, 'r+') as hostfile:
                    hosts = hostfile.readlines()
                    hostfile.seek(0)
                    for host in hosts:
                        if not any(site in host for site in blocked_sites):
                            hostfile.write(host)
                    hostfile.truncate()
                print("The sites have been unlocked!")
                time.sleep(3)
                break
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,
                                            " ".join(sys.argv), None, 1)


if __name__ == '__main__':
    main()
