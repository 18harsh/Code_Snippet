import matplotlib.pyplot as plt 
import numpy as np 
x = np.linspace (0,10,20) # generate 20 points between 0 and 10' 
y = x ** 2 #generate array 'y' from the square of 2 
plt.title ("MY FIRST PLOT") 
plt.xlabel("This is X-axis") 
plt.ylabel("This is Y-axis") 
plt.plot(x,y) 
plt.show



import matplotlib.pyplot as plt 
import numpy as np 
x = np.linspace (0,10,20) # generate 20 points between 0 and 10' 
y = x ** 2 #generate array 'y' from the square of 2 #we will create a plot that has 2 rows and 2 columns and then place 4 plots in the grid . There positions will be numbered as 1,2,3,4. 
plt.subplot(2,2,1) 
plt.plot(x,y,'red') 
plt.subplot(2,2,2) 
plt.plot(x,y,'green') 
plt.subplot(2,2,3)
plt.plot(x,y,'blue') 
plt.subplot(2,2,4) 
plt.plot(x,y,'yellow') 
plt.show




import matplotlib.pyplot as plt
import numpy as np
x = np.linspace (0,5,5)
y = x**2
fig = plt.figure()
a = fig.add_axes([1,2,3,4])
a.set_xlabel("VALUES OF X")
a.set_ylabel("VALUES OF Y")
a.set_title("KHATEEB CLASSES")
a.plot(x,y,'black')
plt.show


import matplotlib.pyplot as plt 
import numpy as np 
x = np.linspace (0,5,5) 
y = x**2 
fig = plt.figure() 
a = fig.add_axes([0.1,0.2,0.9,0.9]) 
b = fig.add_axes([0.2,0.5,0.4,0.3]) 
a.set_xlabel("VALUES OF X") 
a.set_ylabel("VALUES OF Y") 
a.set_title("KHATEEB CLASSES") 
a.plot(x,y,'black') 
b.plot(y,x,'red') 
plt.show

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace (0,5,5)
y = x**2
fig = plt.figure()
a = fig.add_axes([0.1,0.2,0.7,0.8])
a.plot(x,x**2,'black',label = "Square plot")
a.plot(x,x**3,'red',label = "Cube plot")
a.legend() # it shows the labels on top
plt.show


import matplotlib.pyplot as plt
import numpy as np
x = np.random.random_integers(1, 100, 10) # if this function doesn’t work, call randint function
plt.hist(x, bins=30) #
plt.ylabel('No of times')
plt.title("Plotting Random Numbers")
plt.show()


import matplotlib.pyplot as plt
import pandas as pd
a = pd.read_excel ('C:\\Users\\GANDHI\\Desktop\\code\\python\\time series\\daily-total-female-births-in-cal.xlsx',header = 0) # header indicates the row number from where the data needs to be displayed.
print(a.head())
x = a[['Date']]
datatoplot= a[['Daily total female births in California 1959']] #column names
plt.plot(x,datatoplot )


import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 30) # 30 is the number of points
y = np.sin(x)
plt.plot(x, y, 'o', color='blue');


import matplotlib.pyplot as plt
import numpy as np
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
    label="marker='{0}'".format(marker))
    plt.legend(numpoints=1)
    plt.xlim(0, 1.8);


import matplotlib.pyplot as plt
import numpy as np
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,cmap='viridis')#viridis is type of color map, you can use 'Gray' too
plt.colorbar();


import matplotlib.pyplot as plt
import numpy as np
# The slice names of a population distribution pie chart
pieLabels = ['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Australia']
# Population data
populationShare = [59.69, 16, 9.94, 7.79, 5.68, 0.54]
figureObject, axesObject = plt.subplots()
# Draw the pie chart
axesObject.pie(populationShare,labels=pieLabels,autopct='%1.2f',startangle=90)
# Aspect ratio - equal means pie is a circle
axesObject.axis('equal')
plt.show()

