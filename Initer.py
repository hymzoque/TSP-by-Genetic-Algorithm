# -*- coding: utf-8 -*-
import re
import math

class Initer:
    def __init__(self):
        self.__read_points()
        self.__calculate_distances()
    
    # read points
    def __read_points(self):
        self.points = []
        data_file = open("berlin52.tsp", "r")
        for line in data_file.readlines():
            matchobj = re.match("\d+ (\d+.0) (\d+.0)",line)
            if matchobj:
                self.points.append([float(matchobj.group(1)), float(matchobj.group(2))])
        data_file.close()
        return self.points
    
    # calculate all point-to-point distances
    def __calculate_distances(self):
        self.distances = []
        for index_1 in range(len(self.points)):
            point_1 = self.points[index_1]
            distance_temp = []
            for index_2 in range(len(self.points)):
                point_2 = self.points[index_2]
                distance_temp.append(math.sqrt(
                        (point_1[0] - point_2[0])*(point_1[0] - point_2[0]) +
                        (point_1[1] - point_2[1])*(point_1[1] - point_2[1])))
            self.distances.append(distance_temp)
        return self.distances

