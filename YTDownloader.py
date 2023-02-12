from pytube import YouTube
import os
import sys
state = True

while state:
    input1 = input("Entrer un lien youtube pour mp3 file: ")
    if input1 =="":
        sys.exit()
    else:
        vid = YouTube(input1)
        video = vid.streams.filter(only_audio=True).first()
        destination = "PATH"
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file,new_file)
        print(vid.title + " has been downladed")

