from tkinter import *
from pytube import YouTube

window=Tk()
window.geometry("400x600")
window.config(bg="tomato")
window.title("Neeraj Downloader")




Label(window,text="Video Downloader", font="arial 30 bold",bg="red",fg="lightgreen").pack(padx=5,pady=50)

link = StringVar()

Label(window, text="Paste the Link Here:", font="arial 15 bold").pack(padx=5,pady=5)

enter_link = Entry(window, width=50, font=35, textvariable=link,bd=4).pack(padx=5,pady=20)


def downloader():
    url = YouTube(str(link.get()))
    videos=url.streams.first()
    videos.download()

    Label(window, text="Downloaded!!",font="arial 45 bold",bg="lightpink",fg="black").pack(padx=5,pady=15)
    Label(window, text="check out folder", font="arial 30 bold", bg="yellow", fg="red").pack(padx=5, pady=15)

Button(window,text="DOWNLOAD", font="arial 25 bold", bg="Green",bd=4, command=downloader).pack(padx=5,pady=10)

window.mainloop()
