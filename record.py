import pyaudio
import wave

p = pyaudio.PyAudio()

CHANNELS = 1 #number of audio channels (mono)
CHUNK = 1024 * 4 #frames per buffer
FORMAT = pyaudio.paInt16 #sample size (2 bytes)
SAMPLE_RATE = 16000 #samples per second

def recordSample(path:str, audio_sample_name:str, rec_len_s:int):
    stream = p.open(
        channels = CHANNELS,
        format = FORMAT,
        rate = SAMPLE_RATE,
        input = True,
        output = True,
        frames_per_buffer = CHUNK
        )

    print("recording")

    frames = list()
    for i in range(0, int((SAMPLE_RATE/CHUNK)*rec_len_s)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("recording done!")

    stream.stop_stream
    stream.close
    p.terminate

    obj = wave.open(f"{path}{audio_sample_name}.wav", "wb")
    obj.setnchannels(CHANNELS)
    obj.setsampwidth(p.get_sample_size(FORMAT))
    obj.setframerate(SAMPLE_RATE)
    obj.writeframes(b"".join(frames))
    obj.close