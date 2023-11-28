import subprocess
from dotenv import load_dotenv
import os

load_dotenv() # loading in env variables from .env

yt_dlp_path = os.getenv('yt_dlp_path')
songs_txt = os.getenv('songs_txt') # path to txt file with YT URLs
output_file = os.getenv('output_file') # path where downloads are made
audio_format = 'aac' 
audio_quality = '0' # best

def load_songs(songs_txt): # creates songs list from txt file
    with open(songs_txt, 'r') as file:
        urls = file.readlines()
        return [url.strip() for url in urls if url.strip()]
        # list comprehension, discards any leading or trailing newlines

def convert(songs): # runs command line on songs list
    counter = 0
    size = len(songs)

    for song in songs:
        output_template = f"{output_file}/%(title)s.%(ext)s" 
        # ^ needed for custom download directory
        command = [yt_dlp_path, song, 
                   '-x', '--audio-format', audio_format,
                    '--audio-quality', audio_quality, 
                    '--embed-thumbnail', 
                    '--add-metadata', '--embed-metadata',
                    '-o', output_template]
        try:
            subprocess.run(command, check=True)
            print(f"Downloaded and converted {song} to {audio_format} successfully!\n")
            counter += 1

        except subprocess.CalledProcessError as e:
            print(f"Error downloading {song}: {e}\n")
    
    print(f'Songs list size: {size}')
    print(f'Successful Downloads: {counter}\n')
    
songs = load_songs(songs_txt)      
convert(songs)
