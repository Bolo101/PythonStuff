from pytube import YouTube
import os
import sys
import getpass
state = True

username = getpass.getuser()
MusicPath = "/home/{}/Downloads/".format(username)

while state:
    input1 = input("Entrer un lien youtube pour mp3 file: ")
    if input1 =="":
        state = False
        sys.exit()
    else:
        vid = YouTube(input1)
        video = vid.streams.filter(only_audio=True).first()
        destination = MusicPath
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file,new_file)
        print(vid.title + " has been downloaded")
