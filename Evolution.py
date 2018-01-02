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
      
    # my crossover
    __CRO_TOURNA_SIZE = 20
    def evolution_cro(self, loop_time, population, a, b, tourna_size=__CRO_TOURNA_SIZE, doprint=1, file=None):
        return self.__evolution_base(loop_time, population, 0, a, b, tourna_size, 0, doprint, file)

    # order1 benchline crossover
    __BEN_TOURNA_SIZE = 20
    def evolution_benchline_1(self, loop_time, population, a, b, tourna_size=__BEN_TOURNA_SIZE, doprint=1, file=None):
        return self.__evolution_base(loop_time, population, 1, a, b, tourna_size, 0, doprint, file)
    
    # my crossover + mutation
    def evolution_benchline_2(self, loop_time, population, a, b, tourna_size=__BEN_TOURNA_SIZE, doprint=1, mutation_rate=0.1, file=None):
        return self.__evolution_base(loop_time, population, 1, a, b, tourna_size, mutation_rate, doprint, file)
    
    def __evolution_base(self, loop_time, population, isbenchline, a, b, tourna_size, mutation_rate, doprint, file):
        Gene.Gene.setAB(a, b)
        # init by randomly
        group = []
        for i in range(population):
            group.append(Gene.random_gene(self.distances))
        
        # loop
        for i in range(loop_time):
            new_generation = set()
            for individual in group:
                # do the crossover
                for j in range(individual.fitness):
                    reciever = random.choice(group)
                    newone = None
                    if (isbenchline):
                        newone = self.crossover.crossover_benchline(reciever, individual)
                    else:
                        newone = self.crossover.crossover(reciever, individual)
                    if newone != None:
                        new_generation.add(newone)
            # append old individuals
            for old in group:
                new_generation.add(old)
                
            # do the mutation    
            if (mutation_rate != 0):
                for old in group:
                    mutation_time = int(mutation_rate * old.fitness)
                    for k in range(mutation_time):
                        new_generation.add(self.mutation.mutation_single(old))
            
            if doprint:
                best = max(new_generation)
                print("generation - " + str(i) + " : " + str(best.distance))
            if (file != None):
                file.write("generation-")
                file.write(str(i))
                file.write(":")
                file.write(str(best.distance))
                file.write("\n")
            
            group = self.selector.select_tourna(new_generation, population, tourna_size)

        return sorted(group, key=attrgetter('distance'))
        