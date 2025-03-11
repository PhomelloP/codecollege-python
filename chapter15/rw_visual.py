# import matplotlib.pyplot as plt

# from random_walk import RandomWalk

# while True:
# #RW = randomWalk
#  rw = RandomWalk(50_000)
#  rw.fill_walk()

# #plot the points in the walk
#  plt.style.use('classic')
#  fig, ax= plt.subplots()
#  point_numbers = range(rw.num_points)
#  ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
#     edgecolors='none', s=1)
 
#  ax.set_aspect('equal')

# # Emphasize the first and last points.
#  ax.scatter(0, 0, c='green', edgecolors='none', s=100)
#  ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)
 
#  # Remove the axes.
#  ax.get_xaxis().set_visible(False)
#  ax.get_yaxis().set_visible(False)

#  plt.show()

import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
# Make a random walk, and plot the points.
 rw = RandomWalk(5000)  # Use 5,000 points instead of 50,000
 rw.fill_walk()

# Plot the points in the walk.
 plt.style.use('classic')
 fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

 ax.plot(rw.x_values, rw.y_values, linewidth=8)

# Set chart title and label axes.
 ax.set_title("Random Walk", fontsize=24)
 ax.set_xlabel('X-Value', fontsize=14)
 ax.set_ylabel('Y-Value', fontsize=14)

# Set size of tick labels.
 ax.tick_params(axis='both', which='major', labelsize=14)

 plt.show()


  
 keep_running= input("Make another walk? (y/n): ")
 if keep_running =='n':
   break