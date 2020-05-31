import numpy as np
import matplotlib.pyplot as plt
import csv
import AreaDaySales as ads
# set width of bar
barWidth = 0.25

# set height of bar
bars1 = [120, 160, 135, 114, 122, 146, 155]
bars2 = [96, 116, 128, 153, 150, 134, 147]
bars3 = [106, 132, 124, 165, 117, 125, 112]

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, bars1, width=barWidth, edgecolor='white', label='Coffee')
plt.bar(r2, bars2, width=barWidth, edgecolor='white', label='Milkshake')
plt.bar(r3, bars3, width=barWidth, edgecolor='white', label='Cake')

# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E'])

# Create legend & Show graphic
plt.legend()
plt.show()
