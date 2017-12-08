# -*- coding: utf-8 -*-
# @Author hymzoque 2017.12.6
import random
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

class Gene:
    
    # init by path points
    # @path points list 
    # @distances distances table
    # @precalculate flag whether do the pre calculate
    def __init__(self, path, distances, precalculate=1):
        self.path = path
        self.__distances = distances
        if (precalculate) :
            self.__pre_calculate()
    
    # do pre calculate
    def __pre_calculate(self):
        self.calculate_distance()
        self.calculate_fitness()
        
    # calculate path distance of gene
    def calculate_distance(self):
        self.distance = 0.0
        for index in range(len(self.path) - 1):
            p1 = self.path[index]
            p2 = self.path[index + 1]
            self.distance += self.__distances[p1][p2]
        self.distance += self.__distances[self.path[len(self.path) - 1]][self.path[0]]
        return self.distance
    
    __A = 100000.0
    __B = 3000
    # calculate fitness
    def calculate_fitness(self):
        self.fitness = int(self.__A/(self.distance - self.__B))
        return self.fitness
    
    # print out infomation of this gene
    def printout(self):
        print(self.path)
        print("distance : " + str(self.distance))
        
    # draw out this gene
    def drawout(self, points):
        ax = plt.subplot()
        ax.set_xlim(left=0, right=1800)
        ax.set_ylim(bottom=0, top=1400)
        for i in range(len(self.path)):
            p1 = self.path[i]
            p2 = self.path[i + 1] if i != len(self.path) - 1 else self.path[0]
            (x, y) = zip(*[points[p1], points[p2]])
            ax.add_line(Line2D(x, y, lineWidth=1, color='black'))
        plt.plot()
        plt.show()
        self.printout()
    
    def writein(self, file):
        file.write(str(self.path))
        file.write("\ndistance : ")
        file.write(str(self.distance))
        file.write("\n")
    
    def __eq__(self, other):
        return other != None and self.distance == other.distance
    def __gt__(self, other):
        return self.distance < other.distance
    def __hash__(self):
        return hash(self.distance)
    
# generate path by random
def random_gene(distances):
    l = list(range(len(distances)))
    random.shuffle(l)
    return Gene(l, distances)





