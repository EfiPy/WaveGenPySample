#!/usr/bin/python3

# Copyright (C) 2021 MaxWu (EfiPy.Core@gmail.com)

#
# Cos Function: generate Cos wave
#
from math import sin, cos, pow, pi, sqrt

def SinWav (nth, SampleRate, ChannelInfo, PackFunc):

    f, a, p = ChannelInfo
    s = 1 / SampleRate
    t = nth * s
    x = 2 * pi * f * t

    r = sin(x)

    return PackFunc (a * r)

def CosWav (nth, SampleRate, ChannelInfo, PackFunc):

    f, a, p = ChannelInfo
    s = 1 / SampleRate
    t = nth * s
    x = 2 * pi * f * t

    r = cos(x)

    return PackFunc (a * r)

WavformDict = {
    'cos':  CosWav,
    'sin':  SinWav,
}

#
# Parameter
#
para = ( (                      # File parameters
          'simple.wav',         # Output file name
          4,                    # Second
          48000,                # Sampling rate
          16                    # Resolution
          ),
         (
          (                     # Channels information
                'sin',          # Wave generation function
                100,            # Frequency
                70,             # Amplitude
                0               # Phase
           ),
           (                    # Channel 1
                'cos',          # Wave generation function
                200,            # Frequency
                70,             # Amplitude
                0               # Phase
           ),
          ),
       )

import WaveGenPy.WaveGenEngine as WaveGenEngine
from WaveGenPy.OutWaveFunc    import WavPackDict, WavPackOp

OutWave = WaveGenEngine.Tone (*para, WavformDict, WavPackDict, WavPackOp)
print ('parameters...')
print (OutWave)

OutWave.Generate ()
