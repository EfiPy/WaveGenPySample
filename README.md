# Introduce
This is sample code of [WaveGenPy](https://github.com/EfiPy/WaveGenPy)

# Library installation
pip3 install WaveGenPy

# samples
## SampleTone.py 
simple wave genelator, example
```
python3 SampleTone.py -w sine -P -270 -180 -90 0 90 180 270 -f 30 -t 0.3 -v 70
python3 SampleTone.py -W sine square triangle sawtooth dc -f 30 -t 0.3 -v 70
```
## SampleSquareFourier.py 
square wave generator, example
```
python3 SampleSquareFourier.py -f 30 -t 0.3 -v 70 -W SF1 SF2 SF3 SF4 SF5 SF30
```
## covid19-seat.py 
Integral of [this](https://udn.com/news/story/120911/5472587) and its graph in wav file
```
python3 covid19-seat.py
```
The output...  
Upper graph is cosine from -2 to 2 with 20% scale  
lower graph is [this](https://udn.com/news/story/120911/5472587) graph from -2 to 2  
![output](https://github.com/EfiPy/WaveGenPySample/blob/master/covid19-seat.png?raw=true)  
note:  
Due to it output to wav file, it can only present the time domain from 0.
Due to it output to wav file, its y axis present from -1 to 1.

