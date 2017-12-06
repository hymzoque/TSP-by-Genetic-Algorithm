# -*- coding: utf-8 -*-
# @Author hymzoque 2017.12.6
import random
import Gene

class Mutation:
    def __init__(self, distances):
        self.__distances = distances

    # single point mutation
    def mutation_single(self, gene):
        road = list(gene.road)
        distance = gene.distance
        length = len(road)
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
            distance -= self.__distances[road[p2]][road[p2_l]]
            distance -= self.__distances[road[p1]][road[p1_r]]
            distance += self.__distances[road[p1]][road[p2_l]]
            distance += self.__distances[road[p2]][road[p1_r]]
        # neighbor
        elif (p1 - p2 == -1 or p2 - p1 == -length + 1):
            p2_r = p2 + 1 if p2 != length - 1 else 0
            p1_l = p1 - 1 if p1 != 0 else length - 1
            distance -= self.__distances[road[p1]][road[p1_l]]
            distance -= self.__distances[road[p2]][road[p2_r]]
            distance += self.__distances[road[p1]][road[p2_r]]
            distance += self.__distances[road[p2]][road[p1_l]]
        else:
            p1_l = p1 - 1 if p1 != 0 else length - 1
            p1_r = p1 + 1 if p1 != length - 1 else 0
            p2_l = p2 - 1 if p2 != 0 else length - 1
            p2_r = p2 + 1 if p2 != length - 1 else 0
            distance -= self.__distances[road[p1]][road[p1_l]]
            distance -= self.__distances[road[p1]][road[p1_r]]
            distance -= self.__distances[road[p2]][road[p2_l]]
            distance -= self.__distances[road[p2]][road[p2_r]]
            distance += self.__distances[road[p1]][road[p2_r]]
            distance += self.__distances[road[p1]][road[p2_l]]
            distance += self.__distances[road[p2]][road[p1_r]]
            distance += self.__distances[road[p2]][road[p1_l]]
        # then swap
        temp = road[p1]
        road[p1] = road[p2]
        road[p2] = temp
        # construct new gene
        new_gene = Gene.Gene(road, self.__distances, 0)
        new_gene.distance = distance
        new_gene.calculate_fitness()
        
        return new_gene
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    