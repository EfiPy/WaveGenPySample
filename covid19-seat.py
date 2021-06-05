#!/usr/bin/python3

# Copyright (C) 2021 MaxWu (EfiPy.Core@gmail.com)

#
# Cos Function: generate Cos wave
#
from math import sin, cos, pow, pi, sqrt

IntegralValue = 0

def CosWav (nth, SampleRate, ChannelInfo, PackFunc):

    f, a, p = ChannelInfo
    s = 1 / SampleRate
    t = nth * s - 2
    x = 2 * pi * f * t

    r = cos(x)

    return PackFunc (a * r)

#
# https://udn.com/news/story/120911/5472587
#
def Covid19Wave (nth, SampleRate, ChannelInfo, PackFunc):

    global IntegralValue

    f, a, p = ChannelInfo   # frequency, amplitude, phase
    s = 1 / SampleRate      # slice
    t = nth * s - 2         # time

    x = 2 * pi * f * t

    r = (pow(x,3) * cos(x / 2) + 1 / 2) * sqrt (4 - x * x)
    IntegralValue += r * s

    return PackFunc (a * r)

WavformDict = {
    'cos':  CosWav,
    'Covid19':  Covid19Wave,
}

#
# Parameter
#
para = ( (                      # File parameters
          'covid19-seat.wav',   # Output file name
          4,                    # Second
          48000,                # Sampling rate
          16                    # Resolution
          ),
          (                     # Channels information
           (                    # Channel 1
                'cos',          # Wave generation function
                1 / (pi * 2),   # Frequency
                20,             # Amplitude
                0               # Phase
           ),
           (                    # Channel 2
                'Covid19',      # Wave generation function
                1 / (pi * 2),   # Frequency
                20,             # Amplitude
                0               # Phase
           ),
          ),
       )

import WaveGenPy.WaveGenEngine as WaveGenEngine
from WaveGenPy.OutWaveFunc    import WavPackDict

OutWave = WaveGenEngine.Tone (*para, WavformDict, WavPackDict)
print ('parameters...')
print (OutWave)

OutWave.Generate ()
print ('Integral value: %f' % IntegralValue)

