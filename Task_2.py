# Generated array using numpy
# Calculated the time taken for generation

import numpy as np
import time
start = time.time()
arr = np.random.rand(1000,1000)
end = time.time()
time_taken = end - start
print(arr)
print("Total Time Taken For Generating Array: ",time_taken)

# Converting array to bytes
to_bytes = arr.tobytes()

# Converting back to array
to_array = np.frombuffer(to_bytes, dtype = arr.dtype).reshape(arr.shape)
