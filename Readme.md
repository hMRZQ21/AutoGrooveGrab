# AutoGrooveGrab

A script that utilizes the free and open source [`yt_dlp`](https://github.com/yt-dlp/yt-dlp) GitHub repository to convert URLs from YouTube into audio files. 

[`yt_dlp`](https://github.com/yt-dlp/yt-dlp) has extensive documentation with support on many different processing functions with YouTube videos. This is one simple application of the yt-dlp command line. 

This script works by adding a list of URLs into a text file, seperated by a newline, the script executes a yt_dlp command via the command line on each URLs and places the converted file into a directory of your choosing. 

1. Create a `songs.txt file` this is where your YouTube URLs will go. 

2. Create a destination folder for your downloads. this is where the converted files will be deposited. 

3. Create a `.env` file with the approprite paths to your yt_dlp executable, download destination, and songs text file.

**Example:**
```yml
yt_dlp_path=path\to\yt-dlp.exe
songs_txt=path\to\Song URLs.txt
output_file=path\to\Downloaded Songs
```

4. You can optionally create a `.bat` or `.sh` file to run the python script by a double click instead of invoking the command line manually. I called mine `run me.bat`.

**Example:**
```bat
@echo off
python dlp_script.py
pause
```
