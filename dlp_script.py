import subprocess

yt_dlp_path = r'C:\yt_dlp\yt-dlp.exe'
songs_txt = r'C:\yt_dlp\Song URLs.txt' # path to txt file with YT URLs
output_file = r'C:\yt_dlp\Downloaded Songs' # path where downloads are made
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

# Code improvements:
# 1. the format is turned into m4a for some reason. 
# 2. test if ignoring newlines is actually working
# 3. clear out the txt file (handle unsuccessful downloads)
# 4. potentially make a web scraper for adding URLs to the txt
# 5. potentially use more commands 

# iTunes improvements:
# 1. test to see if itunes ignores existing songs in 'Downloaded Songs'
# 2. see if i can add things into albums instead of each song being its own album
# 3. clear out more storage for songs

# SHOULD I PUT THIS ON GITHUB?
# YES, write a nice readme on this