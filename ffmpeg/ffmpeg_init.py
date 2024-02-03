import shutil

from gui import print_


def is_ffmpeg_installed():
    return shutil.which("ffmpeg") is not None


def register_ffmpeg(workdir):
    import os

    if is_ffmpeg_installed():
        print_("ffmpeg is installed in the PATH.")
    else:
        ffmpeg_path = workdir + "\\ffmpeg"
        print_(ffmpeg_path)
        current_path = os.environ.get("Path", "")
        new_path_value = f"{current_path};{ffmpeg_path}"
        os.environ["Path"] = new_path_value
        print_("ffmpeg is added in the PATH.")

        if "ffmpeg" not in os.listdir():
            print_("ERROR: ffmpeg folder does not exist.")
            os.mkdir("ffmpeg")

        if "ffmpeg.exe" not in os.listdir(f"{workdir}\\ffmpeg"):
            print_("ERROR: ffmpeg.exe does not exist in the ffmpeg folder.")
            return False

    return True
