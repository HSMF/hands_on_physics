# util.py contains general utility functions

import csv
import scipy.signal as sig

# for readcsv()
def convert(experiment):
    t = []
    x = []
    y = []
    z = []
    for row in experiment:
        t.append(float(row[0]))
        x.append(float(row[1]))
        y.append(float(row[2]))
        z.append(float(row[3]))
    return (t, x, y, z)


# return the mean of a one dimensional numpy array
def mean(arr):
    arr = list(arr)
    return sum(arr)/len(arr)


# read a csv file and convert it ot floats
def readcsv(filename, d=","):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=d, quotechar="|")
        out = []
        for row in reader:
            out.append(row)
        return convert(out[1:])
    raise FileNotFoundError("file not found")


# find peaks
def peakfinder(x):
    peaks , properties = sig.find_peaks(x, prominence=(6,100))
    return peaks, len(peaks)
