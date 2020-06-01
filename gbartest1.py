import csv
with open('C:\\Users\\admin\\PycharmProjects\\gm\\res\\data\\sales.csv') as fd:
    reader=csv.reader(fd)
    r=[row for idx, row in enumerate(reader) if idx in (1,2,3)]
import numpy as np
import matplotlib.pyplot as plt
import sqltestdb as sdb

def getBars(area):
    maxWindowSize=0
    coffeeBar = sdb.getData('Coffee', area)
    milkshakeBar = sdb.getData('Milkshake',area )
    cakeBar = sdb.getData('Cake', area)
    #bars1 = list(map(int,r[0][1:8]))
    #bars2 = list(map(int,r[1][1:8]))
    #bars3 = list(map(int,r[2][1:8]))
    print("bar1--> ", coffeeBar)
    print(milkshakeBar)
    print(cakeBar)
    barWidth = 0.25

    r1 = np.arange((len(coffeeBar)))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    # Make the plot
    if len(coffeeBar) > 0:
        maxWindowSize = max(maxWindowSize,max(coffeeBar))
        plt.bar(r1, coffeeBar, width=barWidth, edgecolor='white', label='Coffee')
    else:
        print("No values for Coffee in area ",area)
    if  len(milkshakeBar) > 0:
        maxWindowSize = max(maxWindowSize,max(milkshakeBar))
        plt.bar(r2, milkshakeBar, width=barWidth, edgecolor='white', label='Milkshake')
    else:
        print("No values for Milkshake in area ",area)
    if  len(cakeBar) > 0:
        maxWindowSize = max(maxWindowSize,max(cakeBar))
        plt.bar(r3, cakeBar, width=barWidth, edgecolor='white', label='Cake')
    else:
        print("No values for Cake in area ",area)

    # Add xticks on the middle of the group bars
    plt.ylim(0, maxWindowSize+(30*maxWindowSize/100))
    plt.xlabel('Days', fontweight='bold')
    plt.ylabel('Sales', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(coffeeBar))], ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    # Create legend & Show graphic
    plt.legend()
    #plt.show()

    return plt