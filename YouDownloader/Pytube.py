from pytube import YouTube
from  tkinter import  *
from tkinter import filedialog
from os import path
from moviepy.editor import VideoFileClip
import shutil
from tkinter import messagebox

formato = [".mp4" ,".mp3"]  #mp4(audio y video) y mp3(solo audio)
calidad = ["144p","240p","360p","480p","720p","1080p"]
resolucion = "480p"

def descargar():
    global resolucion
    enlace = entrada.get()         #Este comando toma el link que ingrese el usuario en el Entry
    userPath = lbl.cget("text")
    ventana.title('Descargando...')
    ytMP4 = YouTube(enlace).streams.get_highest_resolution().download() #Este comando deswcarga el video o cancion em alta resolucion
    video = VideoFileClip(ytMP4) 
    video.close()
    shutil.move(ytMP4, userPath ) #Este comando mueve el archivo al directorio elegido por el usuario
    mensaje = messagebox.showinfo(message="La descarga se ha completado", title="Download")
    if mensaje:
        ventana.title('YouDownload')
   


def guardarComo():
    path = filedialog.askdirectory()                                              #Sirve para seleccionar un directorio donde vamos a guardar el video/cancion.
    lbl.config(text = path)
    
                                                                                                              
 ###############################
ventana = Tk()
ventana.title('YouDownload')
ventana.iconbitmap('yt.ico')
ventana.config(bg='black')
ventana.geometry("600x800")


Intro = Label (ventana, text = 'Bienvenido a YouDownload', padx= 5, fg = 'Snow', bg ="black", font =("Times New Roman", 20))
Intro.pack()

img = PhotoImage(file ='you.png')
imgn = Label(ventana, image= img, border = 0)
imgn.pack()

lbl= Label(ventana, bg ="black", fg = "white")
lbl.pack(anchor= S)

texto = Label(lbl, text = "Link del video que quiere descargar\n↓↓↓↓↓↓↓↓↓↓↓↓↓")
texto.config(bg = "black", fg ="white",font =("Times New Roman", 10))
texto.pack(pady = 3)

entrada = Entry(lbl)
entrada.pack(pady=5)

lbl2 = Label(lbl, text = "Seleccionar ruta para guardar el archivo", border = 0, bg = "black", fg = "snow")
lbl2.pack(pady = 3)

boton = Button(lbl, text ="Guardar ",  bg="white", cursor = 'hand2', command = lambda : guardarComo())
boton.pack(pady = 3)

boton2 = Button(lbl, text = "Descargar", bg="white", cursor = 'hand2', command = lambda :  descargar())
boton2.pack(pady = 3)




ventana.mainloop()

    


