import matplotlib.pyplot as plt
import csv
x = []
y = []

with open('test1.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        x.append(str(row[1]))
        y.append(float(row[0]))

plt.plot(x,y, label='Loaded from file "file1.txt"')
plt.xlabel('value of k')
plt.ylabel('accuracy')
plt.title('K vs Accuracy Graph')
plt.legend()
plt.show()
