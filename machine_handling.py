#challenge1
import numpy as np
x = np.arange(20)
my_mean = np.mean(x)
print("mean :" ,my_mean)
my_standardDev = np.std(x)
print("standard deviation :",my_standardDev)
my_variance = np.var(x)
print("variance:",my_variance)


#challenge2
import matplotlib.pyplot as plt
import numpy as np
nums=[0.5,0.7,1.0,1.2,1.3,2.1]
bins = [0 ,1, 2 ,3,4,5]
nums = np.array([0.5,0.7,1.0,1.2,1.3,2.1])
plt.hist(nums, bins=[0,1,2,3,5])
plt.xlabel("nums")
plt.ylabel("bins")
plt.title("Histogram of nums against bins")
plt.show()