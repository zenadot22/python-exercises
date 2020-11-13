
import matplotlib.pyplot as plt
import numpy as np
test_scores = [12,99,65,85,42]
test_names=["Andy" , "Martin" , "Zahara" ,"Vuyo" , "Ziyaad"]
x_position = [i for i, _ in enumerate(test_scores)]

plt.bar(x_position,test_names,color='blue')
plt.xlabel("marks(%)")
plt.ylabel("names")
plt.title("python marks for 5 students")
plt.xticks(x_position ,test_scores)
plt.show()

