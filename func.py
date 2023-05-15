import record
import analyze
import datetime
import os

#get current date
date = datetime.datetime.now()
s_date = f"{date.strftime('%Y')}{date.strftime('%m')}{date.strftime('%d')}"
s_time = f"{date.strftime('%H')}{date.strftime('%M')}{date.strftime('%S')}"

#get data path
script_dir = os.path.dirname(__file__) #<-- absolute dir of script
rel_path = f"Data/{date.strftime('%B')} {date.strftime('%Y')}/{date.strftime('%d')}/"
path = os.path.join(script_dir, rel_path)

audio_sample_name = f"{s_date}_{s_time}"

#check whether the specified path exists
if not os.path.exists(path):
    #create new directory
    os.makedirs(f"{path}")
    print(f"created new dir {path}")

#make new audio sample
def genAudioSample(rec_len_s:int):
    task = "generating audio sample"
    print(task)
    record.recordSample(path, audio_sample_name, rec_len_s)
    print(f"{task} done!")

#get the peak frequency
def getPeak() -> float:
    task = "calculating peak"
    print(task)
    peak = analyze.calcFreqPeak(f"{path}{audio_sample_name}.wav")
    peak = round(peak, 2)
    print(f"{task} done!")

    return peak

#write data to file
def writeData(data:float):
    task = "writing data"
    print(task)
    with open(f"{path}{s_date}.txt", "a") as file:
        file.write(f"{s_time} {data}\n")
        file.close()
    print(f"{task} done!")