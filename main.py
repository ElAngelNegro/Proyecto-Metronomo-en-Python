import tkinter
from tkinter import *
from tkinter.ttk import *
import time
import threading
import pygame
import os
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("Metronomo")
root.geometry("640x360+400+200")
root.configure(bg="#eccece")

# Cargar imagen de fondo
try:
    imagen = Image.open(os.path.join(os.path.dirname(__file__), "imagen fondo metronomo.jpg"))
    imagen = imagen.resize((640, 360))
    foto = ImageTk.PhotoImage(imagen)
    
    # Crear label con imagen de fondo
    fondo = Label(root, image=foto)
    fondo.image = foto
    fondo.place(x=0, y=0, width=640, height=360)
except:
    pass  # Si no encuentra la imagen, usa el color de fondo

# Inicializar pygame para audio
pygame.mixer.init()
sound_file = os.path.join(os.path.dirname(__file__), "Perc_Can_hi.wav")
if os.path.exists(sound_file):
    click_sound = pygame.mixer.Sound(sound_file)
else:
    click_sound = None

# Segundo sonido para tiempos 2-4
sound_file2 = os.path.join(os.path.dirname(__file__), "Perc_Can_lo.wav")
if os.path.exists(sound_file2):
    click_sound2 = pygame.mixer.Sound(sound_file2)
else:
    click_sound2 = None

metro_thread = None
is_running = False
beat_count = 0  # Contador para los tiempos

def play_click():
    if click_sound:
        pygame.mixer.stop()  # Detiene cualquier sonido anterior
        click_sound.play()

def play_click2():
    if click_sound2:
        pygame.mixer.stop()  # Detiene cualquier sonido anterior
        click_sound2.play()

def play_metronomo():
    global metro_thread, is_running
    if not is_running:
        is_running = True
        metro_thread = threading.Thread(target=metronomo_loop, daemon=True)
        metro_thread.start()
        btn_iniciar.config(state="disabled")

def stop_metronomo():
    global is_running
    is_running = False
    btn_iniciar.config(state="normal")

def metronomo_loop():
    global beat_count
    segundos_por_metronomo = 60 / int(velocidad_metronomo.get())
    i = 0
    while is_running:
        beat_count = (i % 4) + 1  # Ciclo de 1 a 4
        
        if beat_count == 1:
            play_click()  # Sonido principal en el tiempo 1
        elif beat_count in [2, 3, 4]:
            play_click2()  # Sonido secundario en tiempos 2-4
        
        print(f"Tiempo: {beat_count}")
        
        i += 1
        time.sleep(max(0.1, segundos_por_metronomo - 0.1))  # Deja espacio para que el sonido termine


# Boton Inicio

btn_iniciar = Button(root, text="Iniciar", width=6, command=play_metronomo)
btn_iniciar.place(x=100, y=100)

# Boton Detener
btn_detener = Button(root, text="Detener", width=6, command=stop_metronomo)
btn_detener.place(x=200, y=100)

# Boton salir
btn_salir = Button(root, text="Salir", width=6, command=root.destroy)
btn_salir.place(x=300, y=100)

#Labels
Label(root, text="Tempo", font=('Calibri', 15)).place(x=30, y=200)

# Velocidad Metronomo

velocidad_metronomo = Entry(root, width=10, font=('Calibri', 15))
velocidad_metronomo.place(x=100, y=200)

# Titulo

title = Label(root, text="Metronomo", font=('Calibri', 24))
title.place(x=250, y=0)

root.mainloop()