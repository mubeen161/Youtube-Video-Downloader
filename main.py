from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.config(background="black",border=12)
root.title("Youtube video downloader")
Label(root,text = 'Youtube Video Downloader', font ='Verdana 18 bold',fg="red",background="black").pack()
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold',bd=5).place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link,border=2).place(x = 32, y = 90)
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'red', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()