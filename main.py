import re
from pytube import YouTube
from pytube import Playlist

# for 1080 resolution
import moviepy.editor as mp
import shutil



link = input("Enter your Link Here : ")




def video_options(link):
    yt_tube = YouTube(link)
    i=1
    option_dict = {
        "1080p": 137,
        "720p": 22,
        "480p": 135,
        "360p": 18,
        "144p": 17
    }
    mydict = {}
    for _ in yt_tube.streams:
        if _.resolution not in mydict:
            mydict[_.resolution] = _.filesize_mb
    
    print("Enter the Video-Quality to download from the below list : ")
    for key,value in mydict.items():
        print(f'{i}. {key} || {value}')
        i+=1
    video_quality = input("Enter quality : ")
    return option_dict[video_quality]    # it returns the itag of the video quality to the playlist downloader and ulitmate video downloader function


def Playlist_downloader(link):
    yTube_Playlist = Playlist(link)
    print(f'Downlaoding......{yTube_Playlist.title}')
    print(f"Downloading total no of videos: {yTube_Playlist.length}")
    linked_link = yTube_Playlist.video_urls[0]
    option_itag = video_options(linked_link)
    for url in yTube_Playlist.video_urls:
        ultimate_video_downloader(url,yTube_Playlist.title,option_itag)
    print("COMPLETE PLAYLIST DOWNLOAD SUCCESSFULL!!!!")
    

def video_audio_combiner(title , vid , aud , file_link , place='testDownloads'):
    video_clip = mp.VideoFileClip(vid+file_link)
    audio_clip = mp.AudioFileClip(aud+file_link)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(f'./{place}/{title}.mp4')
    shutil.rmtree(vid)
    shutil.rmtree(aud)


def ultimate_video_downloader(link, place='testDownloads', option_itag = None):
    yt_tube = YouTube(link)
    if option_itag == None: 
        option_itag = video_options(link)
    
    video_stream = yt_tube.streams.get_by_itag(option_itag)
    if video_stream.is_progressive:
        print(f"Downloading....{yt_tube.title} || size = {video_stream.filesize_mb} MB || resolution  = {video_stream.resolution}")
        try:
            video_stream.download(f'./{place}');
        except:
            print("Error has occurred....")
        print("Downloaded Successfully!!!")
    else:
        audio_stream = yt_tube.streams.get_audio_only()
        print(f"Downloading....{yt_tube.title} || size = {video_stream.filesize_mb} MB || resolution = {video_stream.resolution}")
        try:
            video_stream.download(f'./{place}/video');
            audio_stream.download(f'./{place}/audio');
            video_audio_combiner(yt_tube.title, f'./{place}/video' , f'./{place}/audio' , f'/{yt_tube.title}.mp4' , place)
        except:
            print("Error has occurred....")
        print("Downloaded Successfully!!!")
        

def video_download_START(link):
    if re.match(r'^https://www\.youtube\.com/playlist\?list=[\w-]+$', link):
        print("PLAYLIST")
        Playlist_downloader(link)
    else:
        try:
            yt_tube = YouTube(link)
            if yt_tube.check_availability()==None:
                #print("VIDEO")
                ultimate_video_downloader(link)
            else:
                print("VIDEO UNVAILABLE")
        except:
            print("False link!")
                
    
if __name__ == "__main__":
    video_download_START(link)