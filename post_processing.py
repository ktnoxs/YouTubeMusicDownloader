import multiprocessing

from gui import print_


def post_processing(music_data):
    """
    temp 폴더에서 file_name을 이용하여 확장자를 변환합니다. (ffmpeg)
    :param music_data: 음악 정보
    :return: 성공 여부
    """
    import os
    import importlib

    music_title = music_data["title"]
    file_name = music_data["filename"]

    for file in os.listdir('download'):
        if f"{music_title}.mp3" == file:
            print_(f"이미 존재하는 곡 : {music_title}")
            return False

    try:
        pydub = importlib.import_module("pydub")
        music = pydub.AudioSegment.from_file(f"{file_name}.webm", "webm")
        music.export(f"download/{music_title}.mp3", format="mp3", parameters=music_data["thumbnail"])
        # subprocess.run(f'ffmpeg -loglevel error -i {file_name}.webm "download/{music_title}".mp3', shell=True)
        print_(f"변환 완료 : {music_title}")

    except Exception as e:
        print_(f"변환 실패 : {music_title} {e}")

    return True


def post_processing_wrapper(queue):
    """
    멀티 프로세스 큐에서 작업을 할당 받고, post_processing을 실행합니다.
    :param queue: post_processing_queue
    """
    try:
        while not queue.empty():
            music_data = queue.get()
            post_processing(music_data)
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
