from colorama import Fore, Style
from gui import print_


def user_prompt():
    """
    사용자 입력을 받고 처리 후 전달합니다.
    :return: URL List
    """
    split_step = ","
    user_input = input(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}YoutubeMusic{Fore.LIGHTBLACK_EX}｜{Style.RESET_ALL}Enter url : ").strip()

    if user_input in ["exit", "exit()"]:
        return False

    if user_input.endswith(".txt"):
        try:
            with open(user_input, "r", encoding="utf-8") as f:
                user_input = f.read()
                split_step = None
        except:
            print_(f"{user_input} 파일이 존재하지 않습니다.")
            return True

    url_list = list(map(str.strip, user_input.split(split_step)))
    return url_list
