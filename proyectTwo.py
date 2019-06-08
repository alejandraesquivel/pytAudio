import matplotlib.pyplot as plt
import IPython.display as ipd
import scipy.io.wavfile as wf
import librosa.display
import subprocess
from tkinter import *
import tkinter as tk
import librosa
import numpy as np
import os

def playAudio(path):
    subprocess.call(['ffplay', path])

def plotAudio(y, Fs):
    plt.figure(figsize=(14,5))
    librosa.display.waveplot(y, sr=Fs)
    plt.show()

def writeAudio(name,signal,Fs):
    librosa.output.write_wav(name, signal, Fs)

def suma(channel1,channel2,Fs1):
    name = 'suma.wav'
    suma = channel1 + channel2
    writeAudio(name,suma,Fs1)
    plotAudio(suma, Fs1)

def resta(channel1,channel2,Fs1):
    name = 'resta.wav'
    resta = channel1 - channel2
    writeAudio(name,resta,Fs1)
    plotAudio(resta, Fs1)

def multiplicacion(channel1,channel2,Fs1):
    name = 'multiplicacion.wav'
    multiplicacion = channel1 * channel2
    writeAudio(name,multiplicacion,Fs1)
    plotAudio(multiplicacion, Fs1)

def main():
    audio1 = 'DrummerExample.wav'
    audio2 = 'Sylt Kit.wav'
    path1 = os.path.join('/Users/user/Desktop/PDS/ProyectoFinal/pytAudio/',audio1)
    path2 = os.path.join('/Users/user/Desktop/PDS/ProyectoFinal/pytAudio/',audio2)
    y1, Fs1 = librosa.load(path1, mono=False)
    y2, Fs2 = librosa.load(path2, mono=False)
    channel1 = y1[0]
    channel2 = y2[0]
    N = len(channel1)
    channel2 = channel2[:N]
    #playAudio(path1)
    #playAudio(path2)
    suma(channel1,channel2,Fs1)
    resta(channel1,channel2,Fs1)
    multiplicacion(channel1,channel2,Fs1)

if __name__ == '__main__':
    main()
