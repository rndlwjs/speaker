import soundfile as sf
import pandas as pd

short   = "/home/rndlwjs/dataset/ECAPA/6_short_independent_1960.txt"

#a = "/home/rndlwjs/dataset/ECAPA/6_short_dependent_embedding.txt"

name    = ['label', 'spk1', 'spk2', "duration1", "duration2"]
test    = pd.read_csv(short, sep='\t', names=name)

#filename = "/home/rndlwjs/dataset/himia/test/wav/"
filename = "/home/rndlwjs/dataset/"
#filename = "/home/rndlwjs/dataset/cv_7_singleword/"

for i in range(len(test)):
#    print(test["spk1"][i]); exit()
    audio, _ = sf.read(filename+test["spk1"][i])
    test["duration1"][i] = len(audio) / _
    audio, _ = sf.read(filename+test["spk2"][i])
    test["duration2"][i] = len(audio) / _    
    #print(test.head()); exit()

test.to_csv("~/short1960.csv")
