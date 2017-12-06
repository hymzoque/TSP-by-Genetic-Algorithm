# -*- coding: utf-8 -*-
# @Author hymzoque 2017.12.6
import random
from operator import attrgetter

import Gene
import Mutation
import Selection
import Crossover

class Evolution:
    
    def __init__(self, distances, points):
        self.distances = distances
        self.points = points
        self.mutation = Mutation.Mutation(distances)
        self.selector = Selection.Selection()
        self.crossover = Crossover.Crossover(distances)
    
    # only mutation
    # perform not good
    def evolution_mu(self, loop_time, population, doprint=1):
        # init by randomly
        group = []
        for i in range(population):
            group.append(Gene.random_gene(self.distances))
            
        # loop
        for i in range(loop_time):
            new_generation = set()
            for individual in group:
                # do the mutation
                for j in range(individual.fitness):
                    newone = self.mutation.mutation_single(individual)
                    new_generation.add(newone)
            # append alive individuals
            for old in group:
                new_generation.add(old)
            if doprint:
                print("generation - " + str(i) + " : " + str(len(new_generation)))
            group = self.selector.select_tourna(new_generation, population)
        
        return sorted(group, key=attrgetter('distance'))
    
    # only crossover
    # perform very good
    __CRO_TOURNA_SIZE = 10
    def evolution_cro(self, loop_time, population, group=None, tourna_size=__CRO_TOURNA_SIZE, doprint=1):
        if (group == None):
            # init by randomly
            group = []
            for i in range(population):
                group.append(Gene.random_gene(self.distances))
        else:
            population = len(group)
        
        # loop
        for i in range(loop_time):
            new_generation = set()
            for individual in group:
                # do the crossover
                for j in range(individual.fitness):
                    reciever = random.choice(group)
                    newone = self.crossover.crossover_insert(reciever, individual)
                    if newone != None:
                        new_generation.add(newone)
            # append alive individuals
            for old in group:
                new_generation.add(old)
            if doprint:
                print("generation - " + str(i) + " : " + str(len(new_generation)))
            # here use size 10 tournament
            group = self.selector.select_tourna(new_generation, population, tourna_size)
        if doprint:
            print(self.crossover.count)
        return sorted(group, key=attrgetter('distance'))
    
    # mix mutation and crossover
    # first use mutation to create many small group
    # then crossover and merge
    # perform not good
    def evolution_mix(self, loop_time_1, population_1, loop_time_2, population_2):
        gnum = int(population_2 / population_1)
        group = []
        for i in range(gnum):
            result = self.evolution_mu(loop_time_1, population_1, 0)
            group.extend(result[0])
        
        return self.evolution_cro(loop_time_2, population_2, group)
        