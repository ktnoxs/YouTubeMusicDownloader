from colorama import Fore, Style, init

# 초기화 (Windows에서는 이 단계가 필요합니다)
init()

logo = \
f"""
{Fore.GREEN}{Style.BRIGHT}=========================================================

            {Fore.WHITE}YouTube Music Downloader
            {Fore.CYAN}Made By. 갈대
            
{Fore.GREEN}========================================================={Style.RESET_ALL}
프로그램을 종료하시려면, exit()를 입력하시거나 [X]버튼을 누르세요.
"파일이름.txt"로 입력하면 txt 파일 안의 링크를 자동으로 받습니다.
"""


def show_logo():
    print(logo)


def print_(text):
    print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}YoutubeMusic{Fore.LIGHTBLACK_EX}｜{Style.RESET_ALL}{text}")
