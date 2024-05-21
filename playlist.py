import multiprocessing
from pytube import Playlist

from gui import print_


def playlist(url, extract_list):
    """
    youtube url을 이용하여 해당 동영상의 음악 파일을 추출합니다. (youtube_dl)
    :param url: youtube url
    :param extract_list: 플레이리스트인 경우 추출한 url을 저장하기 위한 메모리
    """
    try:
        music_list = Playlist(url)
        if len(music_list):
            print_(f"플레이리스트 추출 완료 : {url} {len(music_list)}곡")
            extract_list.append((url, music_list))
    except Exception:
        pass


def playlist_wrapper(queue, extract_list):
    """
    멀티 프로세스 큐에서 작업을 할당 받고, post_processing을 실행합니다.
    :param queue: downloading_queue
    :param extract_list: 플레이리스트인 경우 추출한 url을 저장하기 위한 메모리
    """
    url = None
    try:
        while not queue.empty():
            url = queue.get()
            playlist(url, extract_list)
    except Exception as e:
        print_(f"Error downloading {url} : {e}")


def playlist_start(url_list, extract_list, available_core_count, extract_queue):
    """
    download 작업을 시작하기 위한 함수.
    :param url_list: Youtube URL List
    :param extract_list: 멀티 프로세스 작업 결과물을 공유하기 위한 메모리
    :param available_core_count: 멀티 프로세싱을 위한 코어 할당량 수
    :param extract_queue: extract_queue
    """

    for url in url_list:
        extract_queue.put(url)

    processes = []
    for i in range(available_core_count):
        process = multiprocessing.Process(
            target=playlist_wrapper, args=(extract_queue, extract_list)
        )
        processes.append(process)
        process.daemon = True
        process.start()
        print_(f"playlist_{i} start")

    for process in processes:
        process.join()

    for origin_url, pl in extract_list:
        url_list.remove(origin_url)
        url_list.extend(pl)
