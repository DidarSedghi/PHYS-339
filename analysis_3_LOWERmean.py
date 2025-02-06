import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson

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



# Define the bins
bins = np.arange(min(data), max(data) + 2, 1)  # Define bin edges
print("BINS: ", bins)

bin_centers = (bins[:-1] + bins[1:]) / 2
centers = []
for j in range(len(bin_centers)):
    centers.append(int(bin_centers[j]))
print(centers)

counts, centers, patches = plt.hist(data, bins=centers, edgecolor="black", alpha=0.7,
                                  label='Data')
plt.xticks(bin_centers)
plt.xticks(bin_centers, labels=[f'{int(x)}' for x in bin_centers])
plt.show()

# Create the histogram (using the edges)
#counts, bins, patches = plt.hist(data, bins=bins, edgecolor="black", alpha=0.7,
                                  #label='Data')

# Get the bin centers
# bin_centers = (bins[:-1] + bins[1:]) / 2
# centers = []
# for j in range(len(bin_centers)):
#     centers.append(int(bin_centers[j]))
# print(centers)
    

# # Plot the histogram again, but this time set xticks to bin centers
# plt.xticks(bin_centers)

# # Manually set the labels for the ticks to the actual values (no shift)
# plt.xticks(bin_centers, labels=[f'{int(x)}' for x in bin_centers])

# plt.xlabel("(CPI) Clicks per Interval")
# plt.ylabel("Occurrences")
# plt.title("Sample 1 LOWER mean value 178.5mm")

#plt.show()


"""
In this section, we will now do a best fit to our data.
"""

# Best fit Poisson distribution.
def Poisson_fit(k, lamb):
    return sum(counts) * poisson.pmf(k, lamb)

# fit with curve_fit
poisson_lambda = np.mean(data)
parameters, cov_matrix = curve_fit(Poisson_fit, centers, counts,
                                    p0=[poisson_lambda])



plt.plot(bin_centers, Poisson_fit(centers, *parameters), marker='o', linestyle='', 
          label='Fitted Poisson')
plt.legend()
plt.show()





# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm, poisson

# # Your data
# #data = [1, 2, 4, 7, 2, 4, 3, 6, 2, 0, 0, 6, 2, 3, 2, 5, 2, 4, 2, 3, 5, 4, 5, 3, 2, 0, 3, 6, 8, 4, 3, 7, 6, 4, 5, 2, 3, 2, 4, 6, 4, 3, 3, 3, 6, 5, 2, 3, 4, 2, 3, 1, 2, 4, 1, 5, 1, 7, 4, 3, 2, 3, 1, 5, 4, 7, 1, 6, 0, 2, 4, 6, 3, 6, 6, 7, 5, 2, 5, 3, 2, 2, 4, 3, 4, 2, 3, 3, 2, 3, 5, 10, 3, 4, 1, 1, 4, 4, 3, 0, 2, 5, 1, 2, 3, 2, 0, 1, 3, 0, 3, 4, 5, 6, 4, 2, 5, 3, 4, 4, 6, 4, 7, 3, 3, 3, 3, 2, 5, 2, 5, 4, 4, 1, 1, 4, 3, 3, 3, 0, 3, 5, 3, 2, 6, 4, 3, 5, 2, 3, 2, 2, 7, 6, 3, 6, 2, 1, 5, 7, 3, 3, 2, 1, 3, 1, 3, 3, 6, 1, 4, 3, 2, 0, 5, 3, 1, 1, 2, 3, 4, 4, 5, 3, 2, 2, 7, 3, 0, 6, 2, 2, 3, 4, 2, 3, 0, 4, 3, 2, 4]

# # Compute histogram
# bins = np.arange(min(data), max(data) + 2, 1)  # Define integer bins
# counts, bin_edges = np.histogram(data, bins=bins)

# # Compute bin centers
# bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# # Fit a Gaussian (Normal) distribution
# mu, sigma = norm.fit(data)  # Get mean and std dev
# gaussian_fit = norm.pdf(bin_centers, mu, sigma) * sum(counts)  # Scale to match histogram

# # Fit a Poisson distribution
# lambda_ = np.mean(data)  # Poisson lambda is the mean of the data
# poisson_fit = poisson.pmf(bin_centers, lambda_) * sum(counts)  # Scale to match histogram

# # Plot the histogram
# plt.bar(bin_centers, counts, width=1.0, edgecolor="black", alpha=0.6, label="Data")

# # Plot the Gaussian fit as a scatter plot
# #plt.scatter(bin_centers, gaussian_fit, color='red', label="Gaussian Fit", zorder=3)

# # Plot the Poisson fit as a scatter plot
# plt.scatter(bin_centers, poisson_fit, color='blue', label="Poisson Fit", zorder=3)

# # Labels and legend
# plt.xlabel("(CPI) Clicks per Interval")
# plt.ylabel("Occurrences")
# plt.title("Histogram with Best-Fit (Gaussian & Poisson)")
# plt.legend()
# plt.grid(True, linestyle="--", alpha=0.5)

# plt.show()




