import numpy as np

def calculate_sum(list):
    list_sum = 0
    for x in range(len(list)):
        list_sum += list[x]
    return list_sum

def calculate_mean(list):
    element_sum = calculate_sum(list)
    mean = element_sum / len(list)
    return mean

def create_mean_list(array, list):
    axis1_means = []
    axis2_means = []
    flattened_mean = calculate_mean(list)
    for x in range(len(array[0])):
        axis1_mean = calculate_mean(array[x])
        axis1_means.append(axis1_mean)
        axis2_mean = calculate_mean([array[0,x], array[1,x], array[2,x]])
        axis2_means.append(axis2_mean)
    mean_list = [axis1_means, axis2_means, flattened_mean]
    return mean_list

def create_sum_list(array, list):
    axis1_sums = []
    axis2_sums = []
    flattened_sum = calculate_sum(list)
    for x in range(len(array[0])):
        axis1_sum = calculate_sum(array[x])
        axis1_sums.append(axis1_sum)
        axis2_sum = calculate_sum([array[0,x], array[1,x], array[2,x]])
        axis2_sums.append(axis2_sum)
    sum_list = [axis1_sums, axis2_sums, flattened_sum]
    return sum_list


def calculate(list):
    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }
    if (len(list) != 9):
        raise ValueError('List must contain nine numbers.')
    
    # convert list to 3x3 numpy array
    array = np.array(list)
    array.shape = (3, 3)

    calculations['mean'] = create_mean_list(array, list)
    calculations['sum'] = create_sum_list(array, list)

    return calculations