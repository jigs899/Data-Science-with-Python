# Exercise 1: Line Plot

# create an array of numbers for x
import numpy as np
x = np.linspace(0, 10, 20)
print(x)

# create y
y = x**3
print(y)

# create the plot
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()

# add x-axis label
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.show()

# add y-label
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.show()

# add title
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed') # add title
plt.show()

# change line color
import matplotlib.pyplot as plt
plt.plot(x, y, 'k') # change color to black
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed') # add title
plt.show()

# make markers into diamonds
import matplotlib.pyplot as plt
plt.plot(x, y, 'Dk') # make markers into diamonds
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed') # add title
plt.show()

# connect markers with a solid line
import matplotlib.pyplot as plt
plt.plot(x, y, 'D-k') # connect markers with a solid line
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed') # add title
plt.show()

# increase title font size
import matplotlib.pyplot as plt
plt.plot(x, y, 'D-k') # connect markers with a solid line
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed', fontsize=22) # increase font size
plt.show()

# create another line for which to plot
y2 = x**2
print(y2)

# add a line for y2
import matplotlib.pyplot as plt
plt.plot(x, y, 'D-k') # connect markers with a solid line
plt.plot(x, y2) # add a line for y2
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed', fontsize=22) # increase font size
plt.show()

# change color and style of y2
import matplotlib.pyplot as plt
plt.plot(x, y, 'D-k') # connect markers with a solid line
plt.plot(x, y2, '--r') # make y2 a red, dotted line
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed', fontsize=22) # increase font size
plt.show()

# create a legend
import matplotlib.pyplot as plt
plt.plot(x, y, 'D-k', label='x cubed') # label as x cubed
plt.plot(x, y2, '--r', label='x squared') # label as x squared
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed', fontsize=22) # increase font size
plt.legend(loc='upper left') # create a plot legend and place it in the upper left
plt.show()

# add multi-line, descriptive title
import matplotlib.pyplot as plt
plt.plot(x, y, 'D-k', label='x cubed') # label as x cubed
plt.plot(x, y2, '--r', label='x squared') # label as x squared
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('As x increases, \nx Cubed (black) increases \nat a Greater Rate than \nx Squared (red)', fontsize=22) # make a multi-line title
plt.legend(loc='upper left') # create a plot legend and place it in the upper left
plt.show()

# change dimensions of plot
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5)) # increase plot size
plt.plot(x, y, 'D-k', label='x cubed') # label as x cubed
plt.plot(x, y2, '--r', label='x squared') # label as x squared
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value')
plt.title('As x increases, \nx Cubed (black) increases \nat a Greater Rate than \nx Squared (red)', fontsize=22) # make a multi-line title
plt.legend(loc='upper left') # create a plot legend and place it in the upper left
plt.show()