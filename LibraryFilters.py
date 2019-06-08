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

def pasaBajas():


def main():
    canal = 0
    audio1 = 'DrummerExample.wav'
    path1 = os.path.join('/Users/user/Desktop/PDS/ProyectoFinal/pytAudio/',audio1)
    y1, Fs1 = librosa.load(path1, mono=False)
    channel1 = y1[canal]
    N = len(channel1)
    #playAudio(path1)
    #playAudio(path2)


if __name__ == '__main__':
    main()
