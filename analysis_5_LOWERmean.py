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
Part I: Data extraction and logistics.
"""
# Declare path of data.
path = '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample1_interval1s_2025-02-05-15h09m32s.txt'

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
print("BIN VALUES: ", bin_values)

bin_centers = (bin_values[:-1] + bin_values[1:]) / 2
print("BIN CENTERS: ", bin_centers)

center = []
for j in range(len(bin_centers)):
    center.append(int(bin_centers[j]))
print("CENTER: ", np.array(center))
    

counts, bin_values, patches = plt.hist(data, bins=bin_values,
                              edgecolor="black", alpha=0.7,label='Data')
plt.legend()
plt.show()


counts, bin_values, patches = plt.hist(data, bins=bin_values,
                              edgecolor="black", alpha=0.7,label='Data Centered')

plt.xticks(bin_centers)
plt.xticks(bin_centers, labels=[f'{int(x)}' for x in bin_centers])
plt.title('centered')
plt.legend()
#plt.show()


"""
Part III: Poisson Fit
"""

# Define the Poisson function for fitting
def Poisson_fit(k, lamb):
    return poisson.pmf(k, lamb) * sum(counts)  # Scale to match total counts

# Estimate initial lambda (mean of data)
poisson_lambda = np.mean(data)

# Fit the Poisson model to histogram data using bin_centers
parameters, cov_matrix = curve_fit(Poisson_fit, bin_centers, counts, p0=[poisson_lambda])



# Plot the fitted Poisson distribution
plt.plot(bin_centers, Poisson_fit(bin_centers, *parameters), linestyle='', marker='o', label='Fitted Poisson')

plt.xticks(bin_centers, labels=[f'{int(x)}' for x in bin_centers])
plt.title('Poisson Fit to Data')
plt.legend()
plt.show()




