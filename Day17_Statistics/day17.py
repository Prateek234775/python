import statistics

marks = [70, 80, 90, 85, 95, 80]

print("Marks:", marks)

print("Mean:", statistics.mean(marks))

print("Median:", statistics.mean(marks))

print("Mode:", statistics.mode(marks))

print("Variance:",statistics.variance(marks))

print("Standard Deviation:", statistics.stdev(marks))

import numpy as np

marks = np.array([70, 80, 90, 85, 95])
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))