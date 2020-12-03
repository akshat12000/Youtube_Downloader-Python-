from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

# total size
file_size = 0


# this gets called for updating percentage
def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    # gets the percentage of the file that has been downloaded
    file_down = (file_size - file_handle)
    per = (file_down / file_size) * 100
    Dbtn.config(text="{:00.0f} % downloaded".format(per))


def startDownload():
    global file_size
    try:
        url = urlField.get()
        # print(url)
        # changing button text
        Dbtn.config(text="Please Wait....")
        Dbtn.config(state=DISABLED)  # button will be disabled for please wait...
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return
        # creating youtube object with url..
        ob = YouTube(url, on_progress_callback=progress)
        # strms = ob.streams.all()
        # for s in strms:                  to display every kind of information about video
        #   print(s)
        strm = ob.streams.get_highest_resolution()
        file_size = strm.filesize
        # print(strm)
        # print(strm.filesize)
        # print(strm.title)
        # print(ob.description)
        strm.download(path_to_save_video)
        print("done....")
        Dbtn.config(text="Start Download")
        Dbtn.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded Successfully")
        urlField.delete(0, END)
    except Exception as e:
        print(e)
        print("Oops! Some Error Occured")


def startDownloadThread():
    # create a thread
    thread = Thread(target=startDownload)  # start a new thread
    thread.start()


# started building GUI
main = Tk()
# creating the title
main.title("Youtube Downloader")
# getting the icon
main.iconbitmap('youtube-logo-png-31812-512x512.ico')
# to fix the size of window
main.geometry("500x600")
# to set heading icon
file = PhotoImage(file='—Pngtree—youtube logo icon_3560541 (1).png')
HeadingIcon = Label(main, image=file)
HeadingIcon.pack(side=TOP)
# creating url box
urlField = Entry(main, font=("Comic Sans MS", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)
# creating download button
Dbtn = Button(main, text="Start Download", font=("Comic Sans MS", 18), justify=CENTER, relief='ridge',
              command=startDownloadThread)
Dbtn.pack(side=TOP, pady=10)
main.mainloop()  # to display window
