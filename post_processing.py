import multiprocessing
import subprocess

from gui import print_


def post_processing(music_title, file_name):
    """
    temp 폴더에서 file_name을 이용하여 확장자를 변환합니다. (ffmpeg)
    :param music_title: 음악 제목
    :param file_name: 파일 이름
    :return: 성공 여부
    """
    import os
    for file in os.listdir('download'):
        if f"{music_title}.mp3" == file:
            try:
                os.remove(f"{file_name}.webm")
                print_(f"이미 존재하는 곡 : {music_title}")
            except Exception as e:
                print_(f"파일 삭제 실패 : {e}")
            return False

    try:
        subprocess.run(f'ffmpeg -loglevel error -i {file_name}.webm "download/{music_title}".mp3', shell=True)
        print_(f"변환 완료 : {music_title}")

    except Exception as e:
        print_(f"변환 실패 : {music_title} {e}")

    try:
        os.remove(f"{file_name}.webm")
    except Exception as e:
        print_(f"파일 삭제 실패2 : {e}")
    return True


def post_processing_wrapper(queue):
    """
    멀티 프로세스 큐에서 작업을 할당 받고, post_processing을 실행합니다.
    :param queue: post_processing_queue
    """
    try:
        while not queue.empty():
            music_title, file_name = queue.get()
            post_processing(music_title, file_name)
    except Exception as e:
        print_(f"Error post_processing: {e}")


def post_processing_start(shared_list, available_core_count, post_processing_queue):
    """
    post processing 작업을 시작하기 위한 함수.
    :param shared_list: 이전 멀티 프로세스에서 작업한 결과물 (공유메모리)
    :param available_core_count: 멀티 프로세싱을 위한 코어 할당량 수
    :param post_processing_queue: post_processing_queue
    """
    for data in list(shared_list):
        post_processing_queue.put(data)

    processes = []
    for i in range(available_core_count):
        process = multiprocessing.Process(target=post_processing_wrapper, args=(post_processing_queue,))
        processes.append(process)
        process.daemon = True
        process.start()
        print_(f"post_processing_{i} start")
    
    for process in processes:
        process.join()
