import os.path
import subprocess

from src.version import VERSION

message_txt = """
https://drive.google.com/drive/folders/1ibcY8trXHPQl_84Z4HsIXmi7QzF1XaBC?usp=sharing

ffmpeg 폴더에 위의 링크에서 받은 파일 3개를 넣어주세요.
개발자라면 ffmpeg 경로를 환경변수에 등록해주셔도 됩니다.
"""


def build(command):
    """Run a system command and print the output."""
    venv_cmd = "./venv/Scripts/pyinstaller"
    subprocess.run([venv_cmd, command])


def compress():
    import shutil
    import zipfile
    from zipfile import ZipFile

    ffmpeg_folder = "ffmpeg"
    readme_name = "README.txt"
    file_path = "temp"
    output_path = f"output"
    file_name = "Youtube Music Downloader.exe"
    zip_name = f"Youtube Music Downloader {VERSION}.zip"

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    if not os.path.exists(f"{file_path}/{ffmpeg_folder}"):
        os.mkdir(f"{file_path}/{ffmpeg_folder}")

    # copy build file
    shutil.copy(f"dist/{file_name}", f"{file_path}/{file_name}")
    # create README.txt
    with open(f"{file_path}/{readme_name}", "w", encoding="utf-8") as f:
        f.write(message_txt)

    # compress
    with ZipFile(f"{output_path}/{zip_name}", 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(f"{file_path}/{readme_name}")
        zipf.write(f"{file_path}/{file_name}")
        zipf.write(f"{file_path}/{ffmpeg_folder}")

    # remove temp
    shutil.rmtree(file_path, onerror=lambda x: print(x))


if __name__ == "__main__":
    build("main.spec")
    compress()
