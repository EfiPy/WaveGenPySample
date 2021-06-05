#!/usr/bin/python3

# Copyright (C) 2021 MaxWu (EfiPy.Core@gmail.com)

from WaveGenPy.InSquareFourier import WavformName, WavformDict

import WaveGenPy.ParaCli as Parameter

para = Parameter.Get (WavformName)
Parameter.Dump (para)

import WaveGenPy.WaveGenEngine as WaveGenEngine
from WaveGenPy.OutWaveFunc    import WavPackDict

OutWave = WaveGenEngine.Tone (*para, WavformDict, WavPackDict)
print ('parameters...')
print (OutWave)

OutWave.Generate ()
