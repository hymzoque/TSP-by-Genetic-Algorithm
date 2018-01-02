# -*- coding: utf-8 -*-
# @Author hymzoque 2017.12.6
import random

class Selection:
    # tournament select
    def select_tourna(self, gener_set, population, tourna_size):
        new_group = []
        for i in range(population):
            sam = random.sample(gener_set, tourna_size)
            champion = max(sam)
            new_group.append(champion)
            gener_set.remove(champion)
        return new_group
    
    
    
    