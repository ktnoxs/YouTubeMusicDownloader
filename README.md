# YouTube Music Downloader

Console program that extracts audio from a YouTube video link.
> For korean, [click here](https://github.com/ktnoxs/YoutubeMusic/blob/main/README-ko.md)

# Library
- yt-dlp (youtube-dl)
- pytube (search)
- pillow (thumbnail)
- pydub (split the music)
- pathvalidate

# Download
You can download it via GitHub Releases.
> [Download Link](https://github.com/ktnoxs/YoutubeMusic/releases)

# Run

### 1. Setup
```bash
pip install -r requirements.txt
```

### 2. Install ffmpeg

Download ffmpeg and create a ffmpeg folder inside the folder where `Youtube Music Downloader.exe` is located. Then, put the `ffmpeg.exe`, `ffplay.exe`, and `ffprobe.exe` files inside the ffmpeg folder.
<br><br>
Alternatively, you can add the ffmpeg path (`bin`) to the environment variables.

### 3. Run

Run `Youtube Music Downloader.exe`.
You can provide a video link, a playlist link, or input links via a text file(`*.txt`), which will be automatically processed for download. You can also search as you would on YouTube.

# Build

You can build it using `python build.py`. The output will be generated in the `output` folder.