"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""
from scipy.fftpack import fft, ifft


def fourie_transform(samples):
    
    x = np.array(samples)
    y = fft(x)
    print(y)
    print(len(samples))
    print(len(y))


samples = []

def convert_data(frames):
    number_of_data = 0  
 

    print("********************")
    for data in frames:
        audio_data = np.fromstring(data, np.int16)
        print(audio_data)
        for each in audio_data:
            samples.append(each)

    fourie_transform(samples)


import pyaudio
import wave
import numpy as np
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 0.1
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