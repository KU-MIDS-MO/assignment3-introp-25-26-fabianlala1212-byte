import numpy as np

def count_values_in_bins(data, bin_edges):
    B= len(bin_edges) -1
    counts =np.zeros(B, dtype=int)
    
    for value in data:
        if value < bin_edges[0] or value > bin_edges[-1]:
            continue
        for i in range(B):
            if i == B-1:
                if bin_edges[i] <= value <= bin_edges[i +1]:
                    counts[i] += 1
                    break
            else :
                if bin_edges[i] <= value < bin_edges[i +1]:
                    counts[i] += 1
                    break
    return counts
   
data = np.array([2.5,3.0,3.5,4.1,4.9,5.0,5.1,6.0,6.5,7.2])
bin_edges = np.array([3.0,4.0,5.0,6.0,7.0])
print(count_values_in_bins(data,bin_edges))