import multiprocessing
from yt_dl import create_ytdl
from pathvalidate import sanitize_filename

from gui import print_


def download(url, shared_list):
    """
    youtube url을 이용하여 해당 동영상의 음악 파일을 추출합니다. (youtube_dl)
    :param url: youtube url
    :param shared_list: 멀티 프로세스 간의 자원 공유를 위한 리스트
    """
    ytdl = create_ytdl()
    data = ytdl.extract_info(url, download=True)
    if 'entries' in data:
        # take first item from a playlist
        for _data in data['entries']:
            music_title = sanitize_filename(_data["title"])
            file_name = ytdl.prepare_filename(_data)[:-5]
            queue_data = (music_title, file_name)
            shared_list.append(queue_data)
            print_(f"다운로드 완료 : {_data['title']}")
    
    else:
        music_title = sanitize_filename(data["title"])
        file_name = ytdl.prepare_filename(data)[:-5]
        queue_data = (music_title, file_name)
        shared_list.append(queue_data)
        print_(f"다운로드 완료 : {data['title']}")


def download_wrapper(queue, shared_list):
    """
    멀티 프로세스 큐에서 작업을 할당 받고, post_processing을 실행합니다.
    :param queue: downloading_queue
    :param shared_list: 멀티 프로세스에서 작업한 결과물 공유 (공유메모리)
    """
    url = None
    try:
        while not queue.empty():
            url = queue.get()
            download(url, shared_list)
    except Exception as e:
        print_(f"Error downloading {url}")


def download_start(url_list, shared_list, available_core_count, downloading_queue):
    """
    download 작업을 시작하기 위한 함수.
    :param url_list: Youtube URL List
    :param shared_list: 멀티 프로세스 작업 결과물을 공유하기 위한 메모리
    :param available_core_count: 멀티 프로세싱을 위한 코어 할당량 수
    :param downloading_queue: downloading_queue
    """

    for url in url_list:
        downloading_queue.put(url)

    processes = []
    for i in range(available_core_count):
        process = multiprocessing.Process(
            target=download_wrapper, args=(downloading_queue, shared_list)
        )
        processes.append(process)
        process.daemon = True
        process.start()
        print_(f"download_{i} start")

    for process in processes:
        process.join()