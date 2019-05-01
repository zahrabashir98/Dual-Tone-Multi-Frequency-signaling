"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import wave
import numpy as np
import math

frequencies = [1209,1336,1477,1633,697,770,852,941]
XJ = []
sum = 0
samples = []

def calculate_N():
    N = len(samples) / RECORD_SECONDS
    print("N : %s"%N)
    return N

def fourie_transform(samples):
    N = calculate_N()
    x = np.array(samples)
    for freq in frequencies:
        sum = 0
        for n in range(len(x)):
            sum += x[n]*(np.exp(-1j* freq* N *n))
        XJ.append(sum)
    print(XJ)
    print(XJ.index(max(XJ)))
    print(XJ.index(XJ[len(XJ)-2]))
    print("///////////////////////")

    output = []
    for data in XJ :
        output.append(math.sqrt((data.real**2)+(data.imag**2)))
    print(output)
    print(output.index(max(output)))
    print(output.index(output[len(output)-2]))
    # print("///////////////////////")
    # output = sorted(XJ, key=float)

    # print(output[len(output)-1])
    # print(max(output))
    # print(output[len(output)-2])






def convert_data(frames):
    number_of_data = 0  
 

    print("********************")
    for data in frames:
        audio_data = np.fromstring(data, np.int16)
        # print(audio_data)
        for each in audio_data:
            samples.append(each)
    # print(samples)
    fourie_transform(samples)


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 0.5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

convert_data(frames)

# dfft = 10.*np.log10(abs(np.fft.rfft(audio_data)))
# print(dfft)

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()