# -*- coding: utf-8 -*-
# @Author hymzoque 2017.12.6
import timeit

import Initer
import Evolution

def GA():
    initer = Initer.Initer()
    points = initer.points
    distances = initer.distances
    
    e = Evolution.Evolution(distances, points)
    #best = e.evolution_mu(50, 10)
    best = e.evolution_cro(65, 550, doprint=0, tourna_size=11)
    #best = e.evolution_mix(10, 10, 35, 300)
    
    with open("log", "a") as f:
        best[0].writein(f)
        f.write("crossover times : ")
        f.write(str(e.crossover.count))
        f.write("\n")
#    best[0].printout()
#    best[0].drawout(points)
    
def runGA():
    t1 = timeit.Timer("GA()", "from main import GA")
    for i in range(25):
        time = t1.timeit(number=1)
        with open("log", "a") as f:
            f.write("use time : ")
            f.write(str(time))
            f.write("\n\n")
        
    
runGA()

