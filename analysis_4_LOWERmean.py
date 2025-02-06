import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson

"""
Appendix
"""
# # Read the content of the data files and put in string_data.
# for i in range(len(paths)):
#     with open(paths[i], "r") as doc:
#         content = doc.read()
#         globals()[f'string_data{i+1}'] = content.split(',')
#         print(f"String data {i+1}", globals()[f'string_data{i+1}'], '\n')

# # Transform the string values into integer values.
# for index in range(len(paths)):
#     globals()[f'data{index + 1}'].append(int(globals()[f'string_data{index + 1}']))
#     print(globals()[f'data{index + 1}'])

# # Declare path of all the data files.
# path1 = '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample1_interval1s_2025-02-05-15h09m32s.txt'
# path2 = '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample2_interval1s_2025-02-05-14h31m32s.txt'
# path3 = '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample3_interval1s_2025-02-05-15h19m22s.txt'
# path4 = '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample4_interval1s_2025-02-05-14h48m55s.txt'
# path5 = '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample5_interval1s_2025-02-05-14h58m45s.txt'

# for i in range(1, 6):
#     with open(globals()[f'path{i}'], "r") as doc:
#         content = doc.read()
#         globals()[f'string_data{i}'] = content.split(',')
#         print(globals()[f'string_data{i}'])

"""
Part I: Logistics and data extraction.
"""
# Declare path of all the data files.
paths = [
    '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample1_interval1s_2025-02-05-15h09m32s.txt',
    '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample2_interval1s_2025-02-05-14h31m32s.txt',
    '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample3_interval1s_2025-02-05-15h19m22s.txt',
    '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample4_interval1s_2025-02-05-14h48m55s.txt',
    '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Winter/PHYS-339 Measurmenets and Lab/Data/Data February 5/LOWER MEAN/lab3_data_CPI_LOWER_200s_(178_5mm)_sample5_interval1s_2025-02-05-14h58m45s.txt'
]


# Read the content of the data files and put in string_data dictionary.
string_data = {}
for i in range(len(paths)):
    with open(paths[i], "r") as doc:
        content = doc.read()
        string_data[i] = content.split(',')
        #print(f"String data {i+1}: ", string_data[i])
# All the data is now put in a dictionary as lists with string values.


# We would like to now turn the string values inside the lists as integer values.
data = {}
for index in range(len(string_data)):
    if string_data[index][-1] == '':
        string_data[index].pop()
        
    for j in range(len(string_data[index])):
        string_data[index][j] = int(string_data[index][j])
    data[index] = string_data[index]

#print(data)


"""
Part II: Plotting Histogram of data.
"""
# Create the bin arrays.
bins_matrix = {}

for x in range(len(data)):
    bins_matrix[x] = np.arange(min(data[x]), max(data[x]) + 2, 1)
#print(bins_matrix[0])

# Creating histograms.
for j in range(len(bins_matrix)):
    counts, 
































