# -*- coding: utf-8 -*-
# @Author hymzoque 2017.12.6
import random
import Gene

class Mutation:
    def __init__(self, distances):
        self.__distances = distances

    # single point mutation
    def mutation_single(self, gene):
        path = list(gene.path)
        distance = gene.distance
        length = len(path)
        # make p1 not equal p2
        p1 = random.randint(0, length - 1)
        p2 = random.randint(0, length - 2)
        if (p2 >= p1):
            p2 += 1
        # calculate new distance
        # neighbor
        if (p1 - p2 == 1 or p2 - p1 == length - 1):
            p1_r = p1 + 1 if p1 != length - 1 else 0
            p2_l = p2 - 1 if p2 != 0 else length - 1
            distance -= self.__distances[path[p2]][path[p2_l]]
            distance -= self.__distances[path[p1]][path[p1_r]]
            distance += self.__distances[path[p1]][path[p2_l]]
            distance += self.__distances[path[p2]][path[p1_r]]
        # neighbor
        elif (p1 - p2 == -1 or p2 - p1 == -length + 1):
            p2_r = p2 + 1 if p2 != length - 1 else 0
            p1_l = p1 - 1 if p1 != 0 else length - 1
            distance -= self.__distances[path[p1]][path[p1_l]]
            distance -= self.__distances[path[p2]][path[p2_r]]
            distance += self.__distances[path[p1]][path[p2_r]]
            distance += self.__distances[path[p2]][path[p1_l]]
        else:
            p1_l = p1 - 1 if p1 != 0 else length - 1
            p1_r = p1 + 1 if p1 != length - 1 else 0
            p2_l = p2 - 1 if p2 != 0 else length - 1
            p2_r = p2 + 1 if p2 != length - 1 else 0
            distance -= self.__distances[path[p1]][path[p1_l]]
            distance -= self.__distances[path[p1]][path[p1_r]]
            distance -= self.__distances[path[p2]][path[p2_l]]
            distance -= self.__distances[path[p2]][path[p2_r]]
            distance += self.__distances[path[p1]][path[p2_r]]
            distance += self.__distances[path[p1]][path[p2_l]]
            distance += self.__distances[path[p2]][path[p1_r]]
            distance += self.__distances[path[p2]][path[p1_l]]
        # then swap
        temp = path[p1]
        path[p1] = path[p2]
        path[p2] = temp
        # construct new gene
        new_gene = Gene.Gene(path, self.__distances, 0)
        new_gene.distance = distance
        new_gene.calculate_fitness()
        
        return new_gene
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    