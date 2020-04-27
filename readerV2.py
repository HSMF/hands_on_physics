import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy as np
import util

def reduce_data(x,y,z, start=0, stop=-1):
    _x = np.array(x[start:stop])
    _y = np.array(y[start:stop])
    _z = np.array(z[start:stop])
    out = (_x**2 + _y**2 + _z**2) **(1/2)
    return out


def get_mean(x,y,z, samplesize=100, start_at=1000):
    length = len(x)
    peaks = []
    for i in range(start_at,length-samplesize, 10):
        peaks.append(reduce_data(x,y,z, start=i, stop=i+samplesize)[1])

    plt.plot(np.array(peaks))
    plt.show()

    return util.mean(peaks)


if __name__ == "__main__":
    run_c = util.readcsv("data/run_c/Accelerometer.csv")
    run_v = util.readcsv("data/run_v/Accelerometer.csv")
    walk_c = util.readcsv("data/walk_c/Accelerometer.csv")
    walk_v = util.readcsv("data/walk_v/Accelerometer.csv")

    print(f"run  1: {get_mean(run_c[1], run_c[2], run_c[3])}")
    print(f"run  2: {get_mean(run_v[1], run_v[2], run_v[3])}")
    print(f"walk 1: {get_mean(walk_c[1], walk_c[2], walk_c[3])}")
    print(f"walk 2: {get_mean(walk_v[1], walk_v[2], walk_v[3])}")
