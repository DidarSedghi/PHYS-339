import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson
"""
This code only handles a specific data sample set for reference. The entire
sample is taken care of in analysis 4.
"""
"""
NEWER.
"""




"""
Part I: Data extraction and logistics.
"""
# Declare path of data.
path = r"\\campus.mcgill.ca\students\users\dsedgh\Desktop\lab3_data_CPI_LOWER_200s_(178_5mm)_sample1_interval1s_2025-02-05-15h09m32s.txt"


# Open data file and put into a string form in an array.
with open(path, "r") as doc:
    content = doc.read()
    string_data = content.split(',')

#print(string_data)

# Put the raw data in integer form in an array.
data = []
for index in range(len(string_data) - 1):
    data.append(int(string_data[index]))
print("Data in integer data form: ", data)



"""
Part II: Plotting and graphing.
"""

bin_values = np.arange(min(data), max(data) + 2, 1)
#print("BIN VALUES: ", bin_values)


counts, bin_values, patches = plt.hist(data, bins=bin_values, edgecolor='black',
                                       alpha=0.7, label='Data')
#plt.show()
print("Summation of counts and counts: ", sum(counts), counts)

print("BIN VALUES: ", len(bin_values), bin_values, "\n")
print("COUNTS: ", len(counts), counts, "\n")

bin_values_new = np.delete(bin_values, -1)

def Poisson_fit(k, lamb):
    return poisson.pmf(k, lamb) * sum(counts)

poisson_lambda = np.mean(data)

parameters, cov_matrix = curve_fit(Poisson_fit, bin_values_new, counts, p0=[poisson_lambda])

print("Optimized poisson mean: ", parameters[0])
print("Covariance matrix: ", cov_matrix)

plt.plot(bin_values_new, Poisson_fit(bin_values_new, *parameters), marker='o',
         linestyle='', label='Poisson fit')

plt.legend()
plt.xlabel('Clicks Per Interval')
plt.ylabel('Occurrences')
plt.title('Lower Mean Sample 1 (178.5mm)')
plt.show()




