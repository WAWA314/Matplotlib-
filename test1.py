import matplotlib.pyplot as plt
import numpy as np

# ช่อง 1: Scatter
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black",
                   "orange","purple","beige","brown","gray","cyan","magenta"])

plt.subplot(3, 3, 1)
plt.scatter(x, y, c=colors,)
plt.title("1: Scatter Plot")

# ช่อง 2: Bar
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.subplot(3, 3, 2)
plt.bar(x, y)
plt.title("2: Bar Chart")

# ช่อง 3: Pie
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.subplot(3, 3, 3)
plt.pie(y, labels=mylabels)
plt.title("3: Pie Chart")

# ช่อง 4: Pie + Legend
# ช่อง 4: Pie + Legend
plt.subplot(3, 3, 4)
plt.pie(y, labels=mylabels)
plt.legend(title="Four Fruits:", loc="center left", bbox_to_anchor=(1, 0.5))
plt.title("4: Pie + Legend")

# ช่อง 5: Line (ไม่มี x)
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.subplot(3, 3, 5)
plt.plot(ypoints)
plt.title("5: Line Plot")

# ช่อง 6: Line + Marker
ypoints = np.array([3, 8, 1, 10])

plt.subplot(3, 3, 6)
plt.plot(ypoints, marker='*')
plt.title("6: Line + Marker")

# ช่อง 7: 2 เส้น
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.subplot(3, 3, 7)
plt.plot(x1, y1, x2, y2)
plt.title("7: Two Lines")

# ช่อง 8: Bar สีแดง
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.subplot(3, 3, 8)
plt.bar(x, y, color="red")
plt.title("8: Red Bar")

# ช่อง 9: Horizontal Bar
plt.subplot(3, 3, 9)
plt.barh(x, y, height=0.1)
plt.title("9: Horizontal Bar")

plt.tight_layout()
plt.show()