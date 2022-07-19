import matplotlib.pyplot as plt
import pandas as pd
import scipy.signal

def ecg_from_file(path="1.crv"):
    ecg = []
    sec = 1
    with open(path) as file:
        for line in file:
            if line[0] != ";":
                currline = line.split()
                ecg.append([int(currline[0]), sec])
                sec += 1
    return ecg

column_names = ["ecg", "t"]

ecg = pd.DataFrame.from_records(ecg_from_file(), columns=column_names)

ecg.t = ecg.t/1000
ecg.ecg = ecg.ecg*0.0001185

b, a = scipy.signal.butter(4, 0.1, 'low', analog=False)
filt_ecg = scipy.signal.filtfilt(b, a, ecg.ecg)

plt.plot(ecg.t, filt_ecg)
plt.grid()
plt.show()