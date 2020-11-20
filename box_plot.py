import matplotlib.pyplot as plt
a=[1.3,3.4,2.3,9.8,10.4]
b=[3.5,4.9,1.3,2.2]
c=[9.7,1.5,4.3,0.9,11.2]
data1=[a,b,c]

plt.boxplot(data1)
plt.xlabel("colleges")
plt.ylabel("scores")
plt.title("Boxplot for colleges")

plt.show()