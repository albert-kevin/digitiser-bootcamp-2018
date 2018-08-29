def calc_sum(data_list):
    """
    self written basic function to read a list of data and sum up all and output a total sum
    data_list can be of the list type with either float or int values
    """
    x = data_list[0]
    for i in range(len(data_list)-1):
        x += data_list[i+1]
    return x

def calc_mean(data_list):
    """
    self written basic function to read a list of data and calculate the mean
    data_list can be of the list type with either float or int values
    """
    return calc_sum(data_list) / len(data_list)

def calc_sample_variance(data_list):
    """
    self written basic function to read a list of data and calculate the variance
    data_list can be of the list type with either float or int values
    """
    n = len(data_list)  #number of sample values
    sample_mean = calc_mean(data_list)  #sample mean of the sample values
    difference = [(data_list[i] - sample_mean)*(data_list[i] - sample_mean) for i in range(len(data_list))]
    return calc_sum(difference) / n

def calc_sample_std(data_list):
    """
    self written basic function to read a list of data and calculate the sample standard deviation
    data_list can be of the list type with either float or int values
    """
    from math import sqrt
    return sqrt(calc_sample_variance(data_list))