import shutil

from gui import print_

FFMPEG_FOLDER = "ffmpeg"


def is_installed(name):
    return shutil.which(name) is not None


def register_ffmpeg(workdir):
    import os

    if is_installed("ffmpeg") and is_installed("ffplay") and is_installed("ffprobe"):
        print_("ffmpeg is installed in the PATH.")
    else:
        ffmpeg_path = workdir + f"\\{FFMPEG_FOLDER}"
        print_(ffmpeg_path)
        current_path = os.environ.get("Path", "")
        new_path_value = f"{current_path};{ffmpeg_path}"
        os.environ["Path"] = new_path_value
        print_("ffmpeg is added in the PATH.")

        if FFMPEG_FOLDER not in os.listdir():
            print_("ERROR: ffmpeg folder does not exist.")
            os.mkdir(FFMPEG_FOLDER)

        flag = False
        if "ffmpeg.exe" not in os.listdir(f"{workdir}\\{FFMPEG_FOLDER}"):
            print_("ERROR: ffmpeg.exe does not exist in the ffmpeg folder.")
            flag = True

        if "ffplay.exe" not in os.listdir(f"{workdir}\\{FFMPEG_FOLDER}"):
            print_("ERROR: ffplay.exe does not exist in the ffmpeg folder.")
            flag = True

        if "ffprobe.exe" not in os.listdir(f"{workdir}\\{FFMPEG_FOLDER}"):
            print_("ERROR: ffprobe.exe does not exist in the ffmpeg folder.")
            flag = True

        if flag is True:
            return False

    return True
