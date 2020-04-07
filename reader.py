import csv
import matplotlib.pyplot as plt

import scipy.signal as sig
import numpy as np


# 31.3.2020 physics


def convert(experiment):
    out = []
    for row in experiment:
        r = []
        for val in row:
            r.append(float(val))
        out.append(r)
    return out


def convert2(experiment):
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


def readcsv(filename, d=","):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=d, quotechar="|")
        out = []
        for row in reader:
            out.append(row)
        return convert2(out[1:])
    raise FileNotFoundError("file not found")


def print_duration(experiment, name=""):
    print("{} {} s".format(name, experiment[0][-1]-experiment[0][0]))



def distinguish(data, time_axis=None, plot=True, stack=False, colors=("black","red")):
    motion = np.array(data)
    peaks, properties = sig.find_peaks(motion, prominence=(6, 100))
    time = list(range(len(data)))
    duration = len(data)
    dt = 1
    offset = 0
    if time_axis:
        dt = time_axis[1]-time_axis[0]
        time = time_axis
        duration = time_axis[-1] - time_axis[0]
        offset = time_axis[0]
    if plot:
        plt.plot(peaks*dt+offset, motion[peaks], "x", color=colors[1])
        plt.plot(time, data, color=colors[0])
        plt.xlabel("time")
        plt.ylabel("m/(s**2)")
        if not stack:
            plt.show()

    frequency = len(peaks)/duration

    return len(peaks), duration, frequency


if __name__ == "__main__":

    run_c = readcsv("data/run_c/Accelerometer.csv")
    walk_c = readcsv("data/walk_c/Accelerometer.csv")
    run_v = readcsv("data/run_v/Accelerometer.csv")
    walk_v = readcsv("data/walk_v/Accelerometer.csv")

    peaks, duration, freq = distinguish(
        run_c[1][1000:1500], run_c[0][1000:1500], stack=True)
    print("{} peaks in {} seconds => {} ".format(peaks, duration, freq))
    peaks, duration, freq = distinguish(walk_v[1][1000:1500], walk_v[0][1000:1500])
    print("{} peaks in {} seconds => {} ".format(peaks, duration, freq))


