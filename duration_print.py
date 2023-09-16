import pandas as pd
import statistics as st

a = pd.read_csv("/home/rndlwjs/multi.csv", sep=",")
#("/home/rndlwjs/vox1.csv", sep=",")

b = a[["spk1", "duration1"]]
c = a[["spk2", "duration2"]]

#name has to be same in order to concatenate
b = b.rename(columns={'spk1':'spk', 'duration1':'duration'})
c = c.rename(columns={'spk2':'spk', 'duration2':'duration'})

d = pd.concat([b, c], axis=0, ignore_index=True, join="outer") #outer은 합집합

d = d.drop_duplicates() #4708 files

e = d['duration'].tolist()

print(st.mean(e), st.median(e), max(e), min(e), "speaker: ", len(e))   #5초 이하, 4초 이하, 3초 이하, 2초 이하, 1.5초 이하, 1초 이하
print(sum(i < 2 for i in e))