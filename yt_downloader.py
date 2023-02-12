import tkinter
import customtkinter
from pytube import YouTube


#create gui 

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


#frame

app=customtkinter.CTk()
app.geometry("800x400")
app.title("downloader")


#elements

title=customtkinter.CTkLabel(app,text="insert a youtube link")
title.pack(padx=10,pady=10)



#link
url=tkinter.StringVar()
link=customtkinter.CTkEntry(app,width=350,height=40)
link.pack(pady=40)

successLabel=customtkinter.CTkLabel(app,text='')
successLabel.pack()



#button
def downloadHandler():
    try:
        ytlink=link.get()
        ytobject=YouTube(ytlink)
        video=ytobject.streams.get_highest_resolution()
        video.download()
    except:
        print('error')

    successLabel.configure(text='Download successfull')


download=customtkinter.CTkButton(app,text="download",command=downloadHandler)
download.pack(padx=10,pady=10)


#run frame
app.mainloop()

