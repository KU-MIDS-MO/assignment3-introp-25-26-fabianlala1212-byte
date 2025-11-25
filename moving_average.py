import numpy as np

def moving_average(signal, window_size):
    n = len(signal)
    k = (window_size -1) // 2
    smothed = np.zeros(n, dtype =float)
    
    for i in range(n):
        start = max(0,i-k)
        end = min(n-1 , i+k)
        smothed[i] = np.mean(signal[start:end+ 1])
    return smothed
    
signal = np.array([10,20,30,40,50])
window_size= 3
result = moving_average(signal,window_size)
print(result)