#!/usr/bin/python3

# Copyright (C) 2021 MaxWu (EfiPy.Core@gmail.com)

#
# Parameter, The same as
# python3 SampleTone.py -W sine square triangle sawtooth dc -f 30 -t 0.3 -v 70
#
para = ( (                      # File parameters
          'Sample2.wav',        # Output file name
          0.3,                  # Second
          48000,                # Sampling rate
          32                    # Resolution
          ),
         (
          (                     # Channels information
                'sine',         # Wave generation function
                30,             # Frequency
                70,             # Amplitude
                0               # Phase
          ),
          (                     # Channels information
                'square',       # Wave generation function
                30,             # Frequency
                70,             # Amplitude
                0               # Phase
          ),
          (                     # Channels information
                'triangle',     # Wave generation function
                30,             # Frequency
                70,             # Amplitude
                0               # Phase
          ),
          (                     # Channels information
                'sawtooth',     # Wave generation function
                30,             # Frequency
                70,             # Amplitude
                0               # Phase
          ),
          (                     # Channels information
                'dc',           # Wave generation function
                30,             # Frequency
                70,             # Amplitude
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
