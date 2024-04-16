import multiprocessing
import os

from gui import print_


def splitting(music_data):
    import importlib

    pydub = importlib.import_module("pydub")
    audio = pydub.AudioSegment.from_file(f'{music_data["filename"]}.webm', 'webm')

    for chapter in music_data["chapters"]:

        start = chapter["start_time"]*1000
        end = chapter["end_time"]*1000
        chapter_title = chapter["title"]

        chapter_music = audio[start:end]
        output_name = f"{music_data['title']} - {chapter_title}"

        flag = False
        for file in os.listdir('download'):
            if f"{output_name}.mp3" == file:
                print_(f"이미 존재하는 곡 : {output_name}")
                flag = True
                break

        if flag is True:
            continue

        chapter_music.export(f"download/{output_name}.mp3", format="mp3", parameters=music_data["thumbnail"])
        print_(f"챕터 분리 완료 : {output_name}")


def split_wrapper(queue):
    """
    멀티 프로세스 큐에서 작업을 할당 받고, splitting을 실행합니다.
    :param queue: splitting_queue
    """
    try:
        while not queue.empty():
            music_data = queue.get()
            splitting(music_data)
    except Exception as e:
        print_(f"Error chater_split: {e}")


def split_start(chater_list, available_core_count, splitting_queue):
    """
    download 작업을 시작하기 위한 함수.
    :param chater_list: 챕터별로 있는 음악을 공유하기 위한 메모리
    :param available_core_count: 멀티 프로세싱을 위한 코어 할당량 수
    :param splitting_queue: splitting_queue
    """

    for music_data in list(chater_list):
        splitting_queue.put(music_data)

    processes = []
    for i in range(available_core_count):
        process = multiprocessing.Process(
            target=split_wrapper, args=(splitting_queue,)
        )
        processes.append(process)
        process.daemon = True
        process.start()
        print_(f"chater_split_{i} start")

    for process in processes:
        process.join()
