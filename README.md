# YouTube-Terminal-Download
The Terminal-based YouTube Downloader is a Python program designed to facilitate the downloading of YouTube videos directly from the command line interface. This project leverages the power of Python and the popular library pytube to interact with YouTube's API and retrieve video content seamlessly.

## Features :-
### 1. Command-Line Interface (CLI)
The program operates entirely within the terminal, offering a user-friendly command-line interface. Users can initiate downloads by providing video URLs as command-line arguments.

### 2. Dependency
The project relies on the pytube library, a powerful Python module for interacting with YouTube's API and downloading video content. The library abstracts the complexities of handling YouTube URLs, formats, and metadata retrieval.

### 3. Video Quality Options
Users can choose the desired video quality for their downloads, such as 720p, 1080p, or higher, depending on the availability of formats for the selected video.
Users can also download Playlist in one GO & download only Audio from the youtube video link as well.

### 4. Error Handling
The program includes robust error handling to gracefully manage scenarios such as invalid URLs, network issues, or unavailable video content. Users receive informative messages to understand and address any encountered issues.

### 5. Output Directory
For video downloads it will be downloaded in Downloads Folder and for Playlist It will create a separate folder or directory with the name of Playlist. This flexibility allows for organized storage of downloaded ?content.

## How To Use :-
Insatll all the dependencies present in the requirements.txt

``` pip install -r requirements.txt  ```

Run the program then by *main.py*
``` run main.py  ```
