from colorama import Fore, Style, init
from src.version import VERSION

# 초기화 (Windows에서는 이 단계가 필요합니다)
init()

logo = \
f"""
{Fore.GREEN}{Style.BRIGHT}=========================================================

            {Fore.WHITE}YouTube Music Downloader {VERSION}
            {Fore.CYAN}Developer: 갈대
            
{Fore.GREEN}========================================================={Style.RESET_ALL}
프로그램을 종료하시려면, exit()를 입력하시거나 [X]버튼을 누르세요.
"파일이름.txt"로 입력하면 txt 파일 안의 링크를 자동으로 받습니다.
다운로드된 폴더를 여시려면 open()을 입력하세요.
유튜브 링크를 입력하시면 자동으로 다운로드가 진행됩니다.
노래 이름을 검색하듯이 입력하면 유튜브 검색결과 첫번째가 다운로드됩니다.
"""


def show_logo():
    print(logo)


def get_form():
    return f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}YoutubeMusic{Fore.LIGHTBLACK_EX}｜{Style.RESET_ALL}"


def print_(text):
    print(f"{get_form()}{text}")
