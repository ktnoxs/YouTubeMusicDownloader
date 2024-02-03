import yt_dlp as youtube_dl


def create_ytdl() -> youtube_dl.YoutubeDL:
    ytdl_format_options = {
        'format': 'bestaudio/best',
        'cachedir': '/data',
        'outtmpl': '/temp/%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

    return youtube_dl.YoutubeDL(ytdl_format_options)
