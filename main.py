import multiprocessing

from src import command, gui
from src.gui import print_
from src.available_core import get_available_core

from src.ffmpeg.ffmpeg_init import register_ffmpeg
from src.folder import exist_folder
from src.process.playlist import playlist_start
from src.process.download import download_start
from src.process.split_music import split_start
from src.process.post_processing import post_processing_start
from src.temp import remove_temp

"""
1.  파이썬 스크립트이며, if __name__ == '__main__': 구문을 사용하여 메인 코드를 실행하는 경우,
    이 구문 안에서 multiprocessing을 사용해야 합니다.

2.  Windows에서는 스크립트를 실행할 때 새로운 프로세스가 생성되는데, 이 때 새로운 프로세스가
    메인 코드를 다시 실행하려는데, 이때 메인 코드가 재진입되면 문제가 발생할 수 있습니다.
    이를 방지하기 위해 multiprocessing.freeze_support()를 호출합니다.
"""


def main():
    gui.show_logo()
    ffmpeg_flag = register_ffmpeg(__import__("os").getcwd())
    if ffmpeg_flag is False:
        print_("프로그램을 종료합니다.")
    else:
        working_core_count = 8
        cpu_count = multiprocessing.cpu_count()
        print_(f"사용 가능한 코어수 : {cpu_count}")

        extract_queue = multiprocessing.Queue()
        downloading_queue = multiprocessing.Queue()
        splitting_queue = multiprocessing.Queue()
        post_processing_queue = multiprocessing.Queue()

        exist_folder("download")
        exist_folder("temp")

        manager = multiprocessing.Manager()

        while True:
            extract_list = manager.list()
            chater_list = manager.list()
            shared_list = manager.list()
            url_list = command.user_prompt()
            if url_list is False:
                print_("프로그램을 종료합니다.")
                break

            if url_list is True:
                continue

            if len(url_list) == 0:
                print_("URL을 입력하세요.")
                continue

            playlist_start(
                url_list=url_list,
                extract_list=extract_list,
                available_core_count=get_available_core(working_core_count, cpu_count, len(url_list)),
                extract_queue=extract_queue
            )
            download_start(
                url_list=url_list,
                chater_list=chater_list,
                shared_list=shared_list,
                available_core_count=get_available_core(working_core_count, cpu_count, len(url_list)),
                downloading_queue=downloading_queue
            )
            split_start(
                chater_list=chater_list,
                available_core_count=get_available_core(working_core_count, cpu_count, len(chater_list)),
                splitting_queue=splitting_queue
            )
            post_processing_start(
                shared_list=shared_list,
                available_core_count=get_available_core(working_core_count, cpu_count, len(list(shared_list))),
                post_processing_queue=post_processing_queue
            )
            remove_temp()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
