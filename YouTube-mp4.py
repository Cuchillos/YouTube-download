#!/usr/bin/env python
#_*_ coding: utf8 _*_

from pytube import YouTube
import time
import os

def banner():
    print("░█████╗░██╗░░░██╗░█████╗░██╗░░██╗██╗██╗░░░░░██╗░░░░░░█████╗░")
    print("██╔══██╗██║░░░██║██╔══██╗██║░░██║██║██║░░░░░██║░░░░░██╔══██╗")
    print("██║░░╚═╝██║░░░██║██║░░╚═╝███████║██║██║░░░░░██║░░░░░██║░░██║")
    print("██║░░██╗██║░░░██║██║░░██╗██╔══██║██║██║░░░░░██║░░░░░██║░░██║")
    print("╚█████╔╝╚██████╔╝╚█████╔╝██║░░██║██║███████╗███████╗╚█████╔╝")
    print("░╚════╝░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝░╚════╝░")
    print()
    print(" Discord:cuchillo#7116 | Github:https://github.com/Cuchillos")
    print()
    print()
banner()
enlace = input("Ingresa el enlace de youtube: ")

time.sleep(1.6)
os.system("cls")

banner()
print("Descargando...")

try:
    YouTube(enlace).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

    print()
    print()
    print("Se ha descargado perfectamente ✔️")
    time.sleep(5)
    exit()
except:
    print()
    print()
    print("ERROR: No se ha podido descargar el video")