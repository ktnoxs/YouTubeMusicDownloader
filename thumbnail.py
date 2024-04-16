from io import BytesIO

import requests
from PIL import Image

from gui import print_


def edit_thumbnail(music_title, image_url):
    try:
        response = requests.get(image_url)
        image_data = response.content
    except Exception as e:
        print_(f"썸네일 다운로드 중 문제가 발생함. {e}")
        return False

    try:
        image = Image.open(BytesIO(image_data))
        width, height = image.size

        diff = (width - height) // 2
        if diff > 0:
            resized_image = image.crop((diff, 0, width - diff, height))
        else:
            diff = abs(diff)
            resized_image = image.crop((0, diff, width, height - diff))
        resized_image = resized_image.resize((500, 500))

        jpg_path = f"temp/{music_title}.jpg"
        resized_image.save(jpg_path)
        image.close()
        resized_image.close()
    except Exception as e:
        print_(f"썸네일 편집 중 문제가 발생함. {e}")

    command = ["-i", str(jpg_path), "-map", "0", "-map", "1", "-id3v2_version", "3",
               "-metadata:s:v", "title='Album cover'", "-metadata:s:v", "comment='Cover (Front)'"
               ]

    return command
