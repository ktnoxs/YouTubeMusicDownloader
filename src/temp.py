import os

from src.gui import print_


def remove_temp():
    for file_name in os.listdir("temp"):
        try:
            os.remove(f"temp/{file_name}")
        except Exception as e:
            print_(f"임시파일을 삭제하는데 오류가 발생했습니다. {e}")
