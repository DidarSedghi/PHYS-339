import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.ticker import MaxNLocator  # Import tick control
from scipy.stats import poisson
"""
author: Didar Sedghi
Last updated on McGill PC: 7th of February 2025
This code rocks.
"""

"""
Part I: Logistics and data extraction.
"""
# Declare path of all the data files.
paths = [
    r'/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample1_interval1s_2025-02-05-15h09m32s.txt',
    r'/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample2_interval1s_2025-02-05-14h31m32s.txt',
    r'/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample3_interval1s_2025-02-05-15h19m22s.txt',
    r'/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample4_interval1s_2025-02-05-14h48m55s.txt',
    r'/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample5_interval1s_2025-02-05-14h58m45s.txt'
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

print("Data dictionnary: ", data, "\n")
for i in range(len(data)):
    print("Data ", i + 1, data[i], "\n")


"""
Part II: Plotting Histogram of data with Poisson fit plots.
"""
# Create the bin arrays.
bins_matrix = {}

for x in range(len(data)):
    bins_matrix[x] = np.arange(min(data[x]), max(data[x]) + 2, 1)
print(bins_matrix[0], bins_matrix)

# Creating histograms.
def Poisson_fit(k, lamb):
    return poisson.pmf(k, lamb) * sum(counts)

def Poisson_fit_collapsed(k, lamb):
    return poisson.pmf(k, lamb) * sum(new_counts)

poisson_fit_expected = {}
COUNTS_dict = {}
for j in range(len(bins_matrix)):
    counts, bins_matrix[j], patches = plt.hist(data[j],
                                               bins=bins_matrix[j],
                                               edgecolor="black",
                                               color='green',
                                               alpha=0.7, label=f'Replica {j+1} Mean: λ = {round(np.mean(data[j]), 2)}')
    poisson_lambda = np.mean(data[j])
    bin_values_new = np.delete(bins_matrix[j], -1)
    parameters, cov_matrix = curve_fit(Poisson_fit, bin_values_new, counts, p0=[poisson_lambda])
    print("Mean: ", j+1, parameters[0])
    print("Covariance matrix: ", j+1, cov_matrix)
    
    
    
    
    
    
    plt.plot(bin_values_new, Poisson_fit(bin_values_new, *parameters), marker='o',
             linestyle='-', color=(1, 0, 0), label='Poisson fit')
    
    #print("\n", "\n", "THIS IS POISSON PARAMETERS: ", parameters, Poisson_fit(bin_values_new, *parameters))
    
    poisson_fit_expected[j] = Poisson_fit(bin_values_new, *parameters) # Expected values.
    
    COUNTS_dict[j] = counts # Counts stored in a dictionnary.
    print("COUNTS: ", j+1, counts)
    plt.legend()
    plt.style.use('seaborn')
    plt.title(f'Replica {j+1} (Source Distance = 178.5mm) \n Target Mean λ ~ 3 CPI \n Interval 1.00s')
    plt.xlabel('(CPI) Clicks per Interval')
    plt.ylabel('Number of Occurrences')
    plt.show()



"""
Part III: Plot the total collapsed data set.
"""
data_set = np.concatenate(list(data.values()))
print(len(data_set), data_set, "\n")

# Bins for the massive data set.
bin_data_set_values = np.arange(min(data_set), max(data_set) + 2, 1)

# y-axis counts for the new data set.
new_counts, bin_data_set_values, patches = plt.hist(data_set, bins=bin_data_set_values,
                                                    edgecolor='black', alpha=0.7,
                                                    label='Massive data')
plt.title('Collapsed Data Set for Lower Mean')
plt.xlabel('Clicks per Interval')
plt.ylabel('Occurrences')
plt.legend()
plt.show()


"""
Part IV: Calculations of statistical information.
"""
# We first start the calculation of the variance of each bin.
# First we calculate the average for a particular bin.
# Then we calculate the variance by x_i - <x> where
# x_i is the value of bin 'i' and <x> is the average value
# of that particular bin.


# Here I am just debugging stuff.
print(COUNTS_dict)
print()
# print("ACTUAL OBSERVED VALUES", '\n')
# print("This is the counts for replica 1: ", COUNTS_dict[0])
# print()
# print("This is the counts for the replica 3: ", COUNTS_dict[2])
# print()
# #print(bins_matrix)


print()
print(poisson_fit_expected)
print()
# print("POISSON EXPECTED VALUES", '\n')
# print("This is the poisson fit values for replica 1: ", poisson_fit_expected[0])
# print()
# print("This is the poisson fit values for replica 3: ", poisson_fit_expected[2])



# Main body of the code starts here.
"""
This function calculates the variance interval between (x_i - <x>)^2 and stores
it into an array where it can then be summed over.
"""
# First we take care of the observed measurements.
print("Replica counts")
for index in range(len(COUNTS_dict)):
    print(f'Counts for Replica {index+1}', COUNTS_dict[index])
    print()

# Max length of a list in counts dictionnary.
max_length = max(len(array) for array in COUNTS_dict.values())
print(max_length)

# Separating bins.
extracted_lists = {f'bin_Observed_{i}': [] for i in range(max_length)}


# Fill the lists
for key in COUNTS_dict:
    for i, value in enumerate(COUNTS_dict[key]):
        extracted_lists[f'bin_Observed_{i}'].append(int(value))

print("\n", extracted_lists, "\n")

# Print the extracted lists
for key, values in extracted_lists.items():
    print(f"{key}: {values}")





####
# Now we will take care of the expected poisson fit values.
print("Poisson expected counts")
for index in range(len(poisson_fit_expected)):
    print(f'Counts for Poisson expected {index+1}', poisson_fit_expected[index])
    print()

# Max length of a list in counts dictionnary.
max_length_poisson = max(len(array) for array in poisson_fit_expected.values())
print(max_length_poisson)

# Separating bins.
extracted_lists_poisson = {f'poisson_{i}': [] for i in range(max_length_poisson)}


# Fill the lists
for key in poisson_fit_expected:
    for i, value in enumerate(poisson_fit_expected[key]):
        extracted_lists_poisson[f'poisson_{i}'].append(float(value))

print("\n", extracted_lists_poisson, "\n")

# Print the extracted lists
for key, values in extracted_lists_poisson.items():
    print(f"{key}: {values}")

print(extracted_lists_poisson['poisson_0'], "\n", "\n", extracted_lists['bin_Observed_0'])


# Calculate the mean for each bin.
average = []
for index in range(len(extracted_lists)):
    average.append(float(np.mean(extracted_lists[f'bin_Observed_{index}'])))

print("Average of each bin: ", average, "\n")

# The following code will calculate the variance interval for each bin.
# We will take care of summing them later no worries!
variance_interval = {f'variance{i}': [] for i in range(len(extracted_lists))}
print(variance_interval)

for index in range(len(extracted_lists)):
    print(index)
    for j in range(len(extracted_lists[f'bin_Observed_{index}'])):
        interval = extracted_lists[f'bin_Observed_{index}'][j] - average[index]
        variance_interval[f'variance{index}'].append(interval**2)

print()
print(variance_interval)
print()
for i in range(len(variance_interval)):
    print(f'variance{i}', variance_interval[f'variance{i}'])


# Summing and taking care of the rest of the formula.
variance_bin = []

for i in range(len(variance_interval)):
    n = len(extracted_lists[f'bin_Observed_{i}']) # bin length
    variance_bin.append(1/n * sum(variance_interval[f'variance{i}']))


print('\n', 'Variance of each bin: ', variance_bin, len(variance_bin))









"""
Part V: Plotting total collapsed data set but for Poisson adjusted error bars.
"""
std_dev_bin = np.sqrt(variance_bin)
print(std_dev_bin)
scale_factor = 1  # Adjust this if necessary
scaled_std_dev_bin = std_dev_bin * scale_factor

data_set = np.concatenate(list(data.values()))

# Bins for the massive data set.
bin_data_set_values = np.arange(min(data_set), max(data_set) + 2, 1)

# y-axis counts for the new data set.
new_counts, bin_data_set_values, patches = plt.hist(data_set, bins=bin_data_set_values,
                                                    edgecolor='black', alpha=0.7,
                                                    label='Massive data')
# Overlay error bars directly on histogram bar heights
plt.errorbar(
    bin_data_set_values[:-1],  # Use left bin edges directly
    new_counts,
    yerr=scaled_std_dev_bin,
    fmt='o',
    color='black',
    capsize=4,                   # Length of caps (horizontal lines)
    capthick=1,                  # Thickness of cap lines
    elinewidth=1,
    markersize=4,
    label='Error bars'
)

# Here Im going to Poisson fit.
poisson_lambda_collapsed = np.mean(data_set)
bin_collapsed = np.delete(bin_data_set_values, -1)
parameters_new, cov_matrix_new = curve_fit(Poisson_fit_collapsed, bin_collapsed, new_counts, p0=[poisson_lambda_collapsed])
plt.plot(bin_collapsed, Poisson_fit_collapsed(bin_collapsed, *parameters_new), marker='o',
             linestyle='-', color='red', label='Poisson fit', alpha=0.5)



plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=20))  # Adjust "nbins" to change tick density


plt.style.use('seaborn')

plt.title('Collapsed Total Data Set (Source Distance = 178.5mm) \n Target Mean λ ~ 3 CPI \n Interval 1.00s')
plt.xlabel('Clicks Per 1second Interval')
plt.ylabel('Frequency of Click Per Interval')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.9)
plt.show()




"""
Part VI: Putting error bars on the replicas.
"""
# The following code will take what we had previously and combine with the std
# and error bar calculations.
for j in range(len(bins_matrix)):
    counts, bins_matrix[j], patches = plt.hist(data[j],
                                               bins=bins_matrix[j],
                                               edgecolor="black",
                                               alpha=0.7, label=f'Replica {j+1} Mean: λ = {round(np.mean(data[j]), 2)}')
    poisson_lambda = np.mean(data[j])
    bin_values_new = np.delete(bins_matrix[j], -1)
    parameters, cov_matrix = curve_fit(Poisson_fit, bin_values_new, counts, p0=[poisson_lambda])

    
    
    plt.plot(bin_values_new, Poisson_fit(bin_values_new, *parameters), marker='o',
             linestyle='-', color='red', label='Poisson fit')
    
    print(f"Bins matrix {j}: ", len(bin_values_new), "std_dev_bin: ", len(std_dev_bin))
    print(f"Counts {j}: ", len(counts))
    
    if len(std_dev_bin) != len(counts):
        std_dev_bin = std_dev_bin[:-1]
    print("STD DEV BIN: ", len(std_dev_bin),"counts len: ", len(counts))
    plt.errorbar(
        bin_values_new,  # Use left bin edges directly
        counts,
        yerr=std_dev_bin,
        fmt='o',
        color='black',
        capsize=4,                   # Length of caps (horizontal lines)
        capthick=0.6,                  # Thickness of cap lines
        elinewidth=2,
        markersize=5,
        label='Error bars'
    )

    
    plt.legend()
    plt.style.use('seaborn')
    plt.title(f'Replica {j+1} (Source Distance = 178.5mm) \n Target Mean λ ~ 3 CPI \n Interval 1.00s')
    plt.xlabel('(CPI) Clicks per 1second Interval')
    plt.ylabel('Frequency of Click per Interval')
    plt.show()



"""
Part VII: Chi-Squared Test
"""
E_i = Poisson_fit_collapsed(bin_collapsed, *parameters_new)
# These are the necessary variables.
print("O_i: ", new_counts, len(new_counts), "\n")
print("E_i: ", E_i , len(E_i)) 
print()
print("sigma_i: ", variance_bin, len(variance_bin))

# Chi-squared calculations.

numerator_chi = []
for index in range(len(new_counts)):
    numerator_chi.append( (new_counts[index] - E_i[index])**2 )

denominator_chi = []
for index in range(len(new_counts)):
    denominator_chi.append(1/variance_bin[index]**2)

chi_squared = []
for index in range(len(new_counts)):
    
