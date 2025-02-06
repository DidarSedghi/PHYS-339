import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson


"""
Part I: Logistics and data extraction.
"""
# Declare path of all the data files.
paths = [
    r"P:\lab3_data_CPI_LOWER_200s_(178_5mm)_sample1_interval1s_2025-02-05-15h09m32s.txt",
    r"P:\lab3_data_CPI_LOWER_200s_(178_5mm)_sample2_interval1s_2025-02-05-14h31m32s.txt",
    r"P:\lab3_data_CPI_LOWER_200s_(178_5mm)_sample3_interval1s_2025-02-05-15h19m22s.txt",
    r"P:\lab3_data_CPI_LOWER_200s_(178_5mm)_sample4_interval1s_2025-02-05-14h48m55s.txt",
    r"P:\lab3_data_CPI_LOWER_200s_(178_5mm)_sample5_interval1s_2025-02-05-14h58m45s.txt"
    ]


# Read the content of the data files and put in string_data dictionary.
string_data = {}
for i in range(len(paths)):
    with open(paths[i], "r") as doc:
        content = doc.read()
        string_data[i] = content.split(',')
        print(f"String data {i+1}: ", string_data[i])
# All the data is now put in a dictionary as lists with string values.


# We would like to now turn the string values inside the lists as integer values.
data = {}
for index in range(len(string_data)):
    if string_data[index][-1] == '':
        string_data[index].pop() # Deletes that pesky ''.
        
    for j in range(len(string_data[index])):
        string_data[index][j] = int(string_data[index][j])
    data[index] = string_data[index]

print("Data dictionnary: ", data)
for i in range(len(data)):
    print("Data ", i + 1, data[i])


"""
Part II: Plotting Histogram of data.
"""
# Create the bin arrays.
bins_matrix = {}

for x in range(len(data)):
    bins_matrix[x] = np.arange(min(data[x]), max(data[x]) + 2, 1)
#print(bins_matrix[0])

# Creating histograms.
def Poisson_fit(k, lamb):
    return poisson.pmf(k, lamb) * sum(counts)

for j in range(len(bins_matrix)):
    counts, bins_matrix[j], patches = plt.hist(data[j],
                                               bins=bins_matrix[j],
                                               edgecolor="black",
                                               alpha=0.7, label=f'Mean = {round(np.mean(data[j]), 2)}')
    poisson_lambda = np.mean(data[j])
    bin_values_new = np.delete(bins_matrix[j], -1)
    parameters, cov_matrix = curve_fit(Poisson_fit, bin_values_new, counts, p0=[poisson_lambda])
    print("Mean: ", j, parameters[0])
    print("Covariance matrix: ", j, cov_matrix)
    
    
    plt.plot(bin_values_new, Poisson_fit(bin_values_new, *parameters), marker='o',
             linestyle='-', label='Poisson fit')
    
    print("COUNTS: ", j+1, counts)
    plt.legend()
    plt.style.use('seaborn-v0_8-paper')
    plt.title(f'Lower Mean Sample {j+1} (178.5mm)')
    plt.xlabel('Clicks per Interval')
    plt.ylabel('Occurrences')
    plt.show()


"""
Part III: Poisson fitting each replica sample data set.
"""
def Poisson_fit(k, lamb, factor):
    return factor * poisson.pmf(k, lamb)



"""
Part IV: Plot the total collapsed 
"""


data_set = np.concatenate(list(data.values()))
print(len(data_set), data_set)

bin_data_set_values = np.arange(min(data_set), max(data_set) + 2, 1)

new_counts, bin_data_set_values, patches = plt.hist(data_set, bins=bin_data_set_values,
                                                    edgecolor='black', alpha=0.7,
                                                    label='Massive data')
plt.legend()
plt.show()



























