
import numpy as np
import time
from knapsack import knapsack
import sys

def read_numbers(data_file):
    input_data_file = open(data_file, 'r')
    input_data = input_data_file.readlines()
    input_data_file.close()

    numbers = np.array([])
    for i_line in xrange(len(input_data)):
        entries = input_data[i_line].split()
        entries = filter(None, entries) # remove empty entries
        line_numbers = [ float(x) if x.lower != "inf" else float("inf") for x in entries ]
        numbers = np.append(numbers, line_numbers)
    return numbers

def read_data(data_file):
    numbers = read_numbers(data_file)
    cur_entry = 0

    # number of nodes
    num_items = int(numbers[cur_entry])
    cur_entry += 1
    
    # maximum capacity of the knapsack
    capacity = float(numbers[cur_entry])
    cur_entry += 1
    
    # get data on the items
    value = np.zeros(num_items, dtype = 'float')
    size = np.zeros(num_items, dtype = 'float')
    for i_item in xrange(num_items):
        value[i_item] = float(numbers[cur_entry])
        cur_entry += 1
        size[i_item] = float(numbers[cur_entry])
        cur_entry += 1
        
    return value, size, capacity

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        value, size, capacity = read_data(file_location)
        solution_value, solution_items = knapsack(value, size, capacity)
        output = open(file_location[:-4]+"_solution.txt", 'w+')
        output.write(str(solution_value)+'\n'+' '.join(map(str, solution_items)))

