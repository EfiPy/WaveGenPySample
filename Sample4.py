#!/usr/bin/python3

# Copyright (C) 2021 MaxWu (EfiPy.Core@gmail.com)

#
# Parameter, The same as
# python3 SampleSquareFourier.py -f 30 -t 0.3 -v 70 -W SF1 SF2 SF3 SF4 SF5 SF30
#
para = ( (                      # File parameters
          'Sample4.wav',        # Output file name
          0.3,                  # Second
          48000,                # Sampling rate
          32                    # Resolution
          ),
         (
          (                     # Channels information
                'SF1',          # Wave generation function
                30,             # Frequency
                70,             # Amplitude
                0               # Phase
          ),
          (                     # Channels information
                'SF2',          # Wave generation function
                30,             # Frequency
                70,             # Amplitude
                0               # Phase
          ),
          (                     # Channels information
                'SF3',          # Wave generation function
                30,             # Frequency
                70,             # Amplitude
                0               # Phase
          ),
          (                     # Channels information
                'SF4',          # Wave generation function
                30,             # Frequency
                70,             # Amplitude
                0               # Phase
          ),
          (                     # Channels information
                'SF5',          # Wave generation function
                30,             # Frequency
                70,             # Amplitude
                0               # Phase
          ),
          (                     # Channels information
                'SF30',         # Wave generation function
                30,             # Frequency
                70,             # Amplitude
                0               # Phase
          ),
         ),
       )

import WaveGenPy.WaveGenEngine      as WaveGenEngine
import WaveGenPy.InSquareFourier    as InToneFunc

from WaveGenPy.OutWaveFunc      import WavPackDict, WavPackOp

OutWave = WaveGenEngine.Tone (*para, InToneFunc.WavformDict, WavPackDict, WavPackOp)
print ('parameters...')
print (OutWave)

OutWave.Generate ()
