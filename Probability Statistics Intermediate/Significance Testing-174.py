## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt
mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)
print(mean_group_a)
print(mean_group_b)
plt.hist(weight_lost_a)
plt.show()
plt.hist(weight_lost_b)
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation test ##

import numpy as np
mean_difference = 2.52
print(all_values)
mean_differences = []
for i in range(1000):
    group_a, group_b = [],[]
    for loop in all_values:
        tmp = np.random.rand()
        if tmp >= 0.5: group_a.append(loop)
        else: group_b.append(loop)
    iteration_mean_difference = numpy.mean(group_b) - numpy.mean(group_a)
    mean_differences.append(iteration_mean_difference)
plt.hist(mean_differences)
plt.show()

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}
for loop in mean_differences:
    if sampling_distribution.get(loop,False):
        val =sampling_distribution.get(loop)
        sampling_distribution[loop] = val+1
    else:
        sampling_distribution[loop] = 1
       

## 8. P value ##

frequencies = []
for lopp in sampling_distribution:
    if lopp >= 2.52: frequencies.append(lopp)
p_value = sum(frequencies) / 1000        