import time
import requests
from fake_useragent import UserAgent
import colorama
from colorama import Fore, Back, Style



def main():
    print("""
          _ _   _                  ___   _ 
__      _(_) |_| |__   ___ _ __   / _ \ / |
\ \ /\ / / | __| '_ \ / _ \ '__| | | | || |
 \ V  V /| | |_| | | |  __/ |    | |_| || |
  \_/\_/ |_|\__|_| |_|\___|_|     \___(_)_|
                                           """)
    print(Fore.GREEN + "Input: URL suite")
    print(Fore.GREEN + "FORMAT: https://www.example.com")
    url = input()
    check_url(url=url)


def check_url(url):
    if url[:8] != "https://":
        print(Fore.RED + "Неправильный формат ввода сообщения")
        exit()
    work_check(url=url)


def work_check(url):
    ua = UserAgent()
    dictfile = open("trash/baza.txt").readlines()
    for i in dictfile:
        attack = url + "/" + i
        headers = {'User-Agent': ua.chrome}
        req = requests.get(attack, headers=headers)

        if req.status_code == 200:
            print(Fore.BLUE + f"{attack} Status code", end=" ")
            print(Fore.GREEN + f"{req.status_code}")

        else:
            print(Fore.BLUE + f"{attack} Status code:", end=" ")
            print(Fore.RED + f"{req.status_code}")



if __name__ == "__main__":
    main()