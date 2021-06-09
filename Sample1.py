#!/usr/bin/python3

# Copyright (C) 2021 MaxWu (EfiPy.Core@gmail.com)

#
# Parameter, The same as
# python3 SampleTone.py -c 4 -w sine
#
para = ( (                      # File parameters
          'Sample1.wav',         # Output file name
          3,                    # Second
          48000,                # Sampling rate
          32                    # Resolution
          ),
         (
          (                     # Channels information
                'sine',         # Wave generation function
                1000,           # Frequency
                100,            # Amplitude
                0               # Phase
          ),
          (                     # Channels information
                'sine',         # Wave generation function
                1000,           # Frequency
                100,            # Amplitude
                0               # Phase
          ),
          (                     # Channels information
                'sine',         # Wave generation function
                1000,           # Frequency
                100,            # Amplitude
                0               # Phase
          ),
          (                     # Channels information
                'sine',         # Wave generation function
                1000,           # Frequency
                100,            # Amplitude
                0               # Phase
          ),
         ),
       )

import WaveGenPy.WaveGenEngine  as WaveGenEngine
import WaveGenPy.InToneFunc     as InToneFunc

from WaveGenPy.OutWaveFunc      import WavPackDict, WavPackOp

OutWave = WaveGenEngine.Tone (*para, InToneFunc.WavformDict, WavPackDict, WavPackOp)
print ('parameters...')
print (OutWave)

OutWave.Generate ()
