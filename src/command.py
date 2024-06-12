import os
from src.gui import get_form, print_


def user_prompt():
    """
    사용자 입력을 받고 처리 후 전달합니다.
    :return: URL List
    """
    split_step = ","
    user_input = input(f"{get_form()}입력 : ").strip()

    if user_input in "exit()":
        return False

    if user_input in "open()":
        os.startfile("download")
        return True

    if user_input.endswith(".txt"):
        try:
            with open(user_input, "r", encoding="utf-8") as f:
                user_input = f.read().split()
                return user_input
        except:
            print_(f"{user_input} 파일이 존재하지 않습니다.")
        return True

    if user_input.find(split_step) == -1:
        return [user_input]
    else:
        return list(map(str.strip, user_input.split(split_step)))
