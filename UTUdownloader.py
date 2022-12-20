from pytube import YouTube
from pytube.cli import on_progress

def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

def progress_function(self,stream, chunk,file_handle, bytes_remaining):

    size = stream.filesize
    p = 0
    while p <= 100:
        progress = p
        print (str(p)+'%')
        p = percent(bytes_remaining, size)

def Download(link,resinput):
    youtubeObject = YouTube(link, on_progress_callback=on_progress)
    #youtubeObject = youtubeObject.streams.get_by_resolution(resinput)
    #youtubeObject = youtubeObject.streams.filter(res='144p').first()
    youtubeObject = youtubeObject.streams.filter(res=resinput)
    if youtubeObject:
        try:
            youtubeObject.first().download()
        except:
            return print("Error ocurred, couldn't download the video, sorry :( Try Again!")
    return print("Download completed, let's watch it together :D!")

    
    

link = input("Paste the link here~ URL:")
resolink = YouTube(link)

resolution =[str(i)for i in (list(dict.fromkeys([i.resolution for i in resolink.streams if i.resolution])))]
print("these are the avaliable resolutions:")
print(resolution)
resinput = str(input("Choose a resolution: "))
if resinput not in resolution:
    while True:
        resinput = str(input("Choose a a correct format for the resolution: "))
        if resinput in resolution:
            break
Download(link,resinput)


#Download(link)