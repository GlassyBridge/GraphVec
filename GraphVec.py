## GraphVec
# Importing the necessary libraries for the functioning of the code.
import matplotlib.pyplot as plt
import math
from numpy import arange
from random import random

class Vector:
    # Defining an instance method called __init__ that takes in two points as an argument.
    def __init__(self, p1=(0, 0), p2=(0, 0)):
        
        # Defining the points for the vector.
        self.p1, self.p2 = p1, p2

        # Defining the x and y components for the points of the vector.
        self.p1x, self.p1y = self.p1
        self.p2x, self.p2y = self.p2

        # Defining the x and y compnents of the vector.
        self.x, self.y = self.p2x - self.p1x, self.p2y - self.p1y
        self.u, self.v = self.x, self.y

        # Defining the magnitude of the vector.
        self.mag = math.sqrt(self.x ** 2 + self.y ** 2)
        
        # Calculation for vector direction.
        if self.x != 0:
            self.dir = (math.atan(self.y / self.x)) * 180 / math.pi
        else:
            if self.y != 0:
                self.dir = 90.0 if self.y > 0 else 270.0
            else:
                self.dir = 0

        # Adjusting angle to be from the horizontal axis.
        if self.x < 0:
            self.dir += 180
        elif self.y < 0:
            self.dir += 360

        # Rounding the points of the vector for easier calculation and visualization.
        self.p1 = (round(self.p1x, 2), round(self.p1y, 2))
        self.p2 = (round(self.p2x, 2), round(self.p2y, 2))
    
    def __str__(self):
        # Defining the representation of the instance of the class when outputted.
        return f'{self.p1} ––> {self.p2}\n {round(self.mag, 3)} units {round(self.dir, 2)}º'
    
    def __eq__(self, other):
        # Defining the method used for determining if two vectors are equal.
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __lt__(self, other):
        # Defining the method used for checking if this vector is less than the other vector.
        return self.mag < other.mag

    def __gt__(self, other):
        # Defining the method used for checking if this vector is greater than the other vector.
        return self.mag > other.mag

    @staticmethod
    def max_vector(vectors):
        #Defining the static method used for checking the max vector.
        return max(vectors, key=lambda v: v.mag)

    @staticmethod
    def min_vector(vectors):
        return min(vectors, key=lambda v: v.mag)


    def __add__(self, other):
        #Defining a method for adding vectors with other vectors or numbers.
        if isinstance(other, Vector):
            #Checking if the other variable is a vector, performing and returning the needed calculations.
            return Vector(self.p1, (self.p2x + other.u, self.p2y + other.v))
        
        elif isinstance(other, int):
            #Checking if the other variable is a integer, performing and returning the needed calculations.
            return Vector(self.p1, (self.p2x + other, self.p2y + other))
        
    def __sub__(self, other):
        #Defining a method for subtracting vectors with other vectors or numbers.
        if isinstance(other, Vector):
            #Checking if the other variable is a vector, performing and returning the needed calculations.
            return Vector(self.p1, (self.p2x - other.u, self.p2y - other.v))
        
        elif isinstance(other, int):
            #Checking if the other variable is a integer, performing and returning the needed calculations.
            return Vector(self.p1, (self.p2x - other, self.p2y - other))
        
    def __mul__(self, scalar):
        return Vector(self.p1, (self.p2x * scalar, self.p2y * scalar))
        
    def __truediv__(self, scalar):
        return Vector(self.p1, (self.p2x / scalar, self.p2y / scalar))

    def __neg__(self):
        return Vector(self.p2,self.p1)

class Mvector:
    #This class is used to convert vectors described interms of magnitude and direction to the vector class we have declared before.
    def __init__(self, mag=0, dir=0):
        self.dir = math.radians(dir)  # Convert degrees to radians
        self.mag = mag
        self.x = math.cos(self.dir) * self.mag
        self.y = math.sin(self.dir) * self.mag
        self.p1, self.p2 = (0, 0), ( self.x , self.y )
        
    def to_vector(self):
        return Vector(self.p1, self.p2)


class Graphvector:
    def __init__(self, vectors = [], dict = {}, size = (6, 6), title = "Vector Visualization", buffer = 1):
        fig, ax = plt.subplots(figsize = size)

        if len(vectors) != 0:#Checking if the variable vectors is not empty.
            # Calculating the limits based on vector endpoints for vectors that are presented with dictionaries.
            all_x = [v.p1x for v in vectors] + [v.p2x for v in vectors]
            all_y = [v.p1y for v in vectors] + [v.p2y for v in vectors]
            
        if len(dict) != 0: #Checking if the variable dict is not empty.
            # Calculating the limits based on vector endpoints for vectors that are presented with dictionaries.
            dict_all_x = [v.p1x for v in dict.values()] + [v.p2x for v in dict.values()]
            dict_all_y = [v.p1y for v in dict.values()] + [v.p2y for v in dict.values()]

        #Error handling based on the state of the two variables (vector containers).
        if len(vectors) and len(dict) != 0:
            #Finding the maximum and minimum points of x and y.
            min_x, max_x = min(min(all_x) , min(dict_all_x)) , max(max(all_x) , max(dict_all_x))
            min_y, max_y = min(min(all_y) , min(dict_all_y)) , max(max(all_y) , max(dict_all_y))

        elif (len(vectors) != 0) and (len(dict) == 0):
            #Finding the maximum and minimum points of x and y.
            min_x, max_x = min(all_x) , max(all_x)
            min_y, max_y = min(all_y) , max(all_y)

        elif (len(vectors) == 0) and (len(dict) != 0):
            #Finding the maximum and minimum points of x and y.
            min_x, max_x = min(dict_all_x) , max(dict_all_x)
            min_y, max_y = min(dict_all_y) , max(dict_all_y)

        #Finding the graph's maximum and minimum point.
        min_ = min(min_x,min_y)
        max_ = max(max_x,max_y)
        
        # Extending the limits for x and y for better visualization.
        ax.set_xlim(min_ - buffer , max_ + buffer)
        ax.set_ylim(min_ - buffer , max_ + buffer)

        # Drawing method.
        # Drawing the central axes.
        ax.axhline(0, color='black', linewidth= 1.2, linestyle='-')  # X-axis
        ax.axvline(0, color='black', linewidth= 1.2, linestyle='-')  # Y-axis
        
        # Plotting each vector with a random color for vectors with no notations
        for i,V in enumerate(vectors):
            color = (random(), random(), random())
            ax.quiver(V.p1x, V.p1y, V.u, V.v, angles='xy', scale_units='xy', scale=1, color=color, label=str(f'Vector {i}: {V}'))

        # Plotting each vector with a random color for vectors with notations.
        for V in dict:
            color = (random(), random(), random())
            ax.quiver(dict[V].p1x, dict[V].p1y, dict[V].u, dict[V].v, angles='xy', scale_units='xy', scale=1, color=color, label=str(f'Vector {V}: {dict[V]}'))


        # Drawing the graph.
        plt.axis('equal')  # Keep the aspect ratio square
        
        ax.set_xticks(arange(min_ - buffer , max_ + buffer + 1),minor= True)
        ax.set_yticks(arange(min_ - buffer , max_ + buffer + 1),minor= True)

        # Showing major tick labels only.
        ax.tick_params(axis='x', which='minor', labelbottom=False)  # Hide minor tick labels
        ax.tick_params(axis='y', which='minor', labelleft=False)   # Hide minor tick labels

        # Enabling grid for both major and minor ticks.
        ax.grid(which = 'minor', linestyle = '--', linewidth = 0.5, color = 'lightgray')
        ax.grid(which = 'major', linestyle = '-', linewidth = 1, color = 'darkgray')
        
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.title(title)
        plt.show()


#Conversion function to take a vector interms of magnitude and direction and convert it into the regular vector.
def mvector(mag, dir):
    mvec = Mvector(mag, dir)
    return mvec.to_vector()