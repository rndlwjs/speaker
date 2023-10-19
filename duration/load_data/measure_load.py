import torch
import io, os, time
import numpy as np
import soundfile as sf

#extracting files
file_root = ""
train_path = ""
lines = open(file_root).read().split("\n")
for i in range(len(lines)):
    lines[i] = lines[i][8:]
    if lines[i].startswith("id")==False:
        print("The wrong path: ", lines[i])
    lines[i] = os.path.join(train_path, lines[i])

lines.sort()

num_files = 55680 # change the number

start_time_np = time.time()
for j in lines[:num_files]:                     
    audio, _ = sf.read(j)
end_time_np = time.time()
loading_time_np = end_time_np - start_time_np
print(f"Loading time for sound file: {loading_time_np} seconds")

start_time_np = time.time()
for q in lines[:num_files]:
    np.save("prac/"+q.replace("/","_"), audio)
end_time_np = time.time()
loading_time_np = end_time_np - start_time_np
print(f"Saving time for Numpy array file: {loading_time_np} seconds")

start_time_np = time.time()
for w in lines[:num_files]:
    aaa = np.load("prac/" + q.replace("/","_")+".npy")
end_time_np = time.time()
loading_time_np = end_time_np - start_time_np
print(f"Loading time for Numpy array file: {loading_time_np} seconds")
