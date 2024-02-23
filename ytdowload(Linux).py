from tkinter import *
from pytube import YouTube
import threading
from time import sleep
import platform

main = Tk()
main.title("BRELoad")
main.config(bg='green')

# Comprobación de la plataforma para ajustar según el sistema operativo
if platform.system() == 'Windows':
    main.attributes("-transparent", "green")  # Ajuste específico de Windows
else:
    main.attributes("-alpha", 0.9)  # Ajuste para sistemas basados en Linux

main.update()

estado = StringVar()  # ESTADO DE LA DESCARGA
FRAME_MAIN = Frame(bg="green")
FRAME_MAIN.pack(ipadx=10, pady=10)

MENSAJE = Label(FRAME_MAIN, bg="green", fg="white", font=("arial", 12, "bold"))
MENSAJE.pack()

Label(FRAME_MAIN, text="★ Youtube", fg="white", bg="red",
      font=("arial", 12, "bold")).pack(ipadx=10, ipady=10)

Label(FRAME_MAIN, text="PEGA EL LINK;", bg="green", fg="white").pack(pady=(20, 0))
LINK = Entry(FRAME_MAIN, width=50, relief=SOLID,
             highlightthickness=2, highlightcolor="white")

LINK.pack(ipady=5)
LINK.focus_set()

def mensaje():
    LINK.config(state=DISABLED)
    DOWLOAD.config(state=DISABLED)
    sms = "Descargando"
    pivot = True
    while len(estado.get()) == 0:
        if pivot:
            sms += " ."
            if len(sms) == 17: pivot = False
        else:
            sms = sms[:-2]
            if len(sms) == 11: pivot = True
        MENSAJE.config(text=sms)
        sleep(1 / 2)
    LINK.config(state=NORMAL)
    DOWLOAD.config(state=NORMAL)
    LINK.delete(0, "end")

def hilo(link):
    h1 = threading.Thread(target=mensaje)
    h1.start()

    def descarga(link):
        try:
            if len(link) != 0:
                yt = YouTube(link).streams.get_highest_resolution()
                yt.download()
                MENSAJE.config(text="Video descargado con exito")
            else:
                raise ValueError("No existe link")
        except Exception:
            MENSAJE.config(text="Se produjo un error al descargar!")
            estado.set("¡ ERROR")
        estado.set("¡ VIDEO DESCARGADO!")

    estado.set("")
    h2 = threading.Thread(target=descarga, args=(link,))
    h2.start()

DOWLOAD = Button(FRAME_MAIN, text="Descargar",
                 bg="lightgreen", cursor="hand2", command=lambda: hilo(LINK.get()))
DOWLOAD.pack(pady=(20, 0))

main.mainloop()

