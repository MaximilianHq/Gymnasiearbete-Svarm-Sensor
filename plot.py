import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt

file = 'example.wav'

#read audio sample
s_rate, signal = wavfile.read(file)

#get wav amplitude
FFT = abs(scipy.fft.fft(signal))
#get wav frequency
freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))

def plotFreqAmp():
    plt.plot(freqs[range(0, 40000)], FFT[range(0, 40000)])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.show()

def getMaxValueIndex(array):
    #get index of max value
    print(array)
    max_value_index = np.where(array == max(array))[0][0]
    return max_value_index

def calcFreqPeak():
    index = getMaxValueIndex(FFT)
    peak = freqs[index]
    print(peak)


calcFreqPeak()
plotFreqAmp()