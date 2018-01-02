# -*- coding: utf-8 -*-
# @Author hymzoque 2017.12.6
import timeit

import Initer
import Evolution

def GA(dataset=52):
    initer = Initer.Initer(dataset)
    points = initer.points
    distances = initer.distances
    e = Evolution.Evolution(distances, points)
    
    with open("log_ga_" + str(dataset), "a") as f:
        # about 11 seconds
        if (dataset == 52):
            best_cro = e.evolution_cro(65, 550, 100000.0, 3000.0, 11, 1, f)
        # about 85 seconds
        elif (dataset == 130):
            best_cro = e.evolution_cro(200, 900, 100000.0, 3000.0, 10, 1, f)
        # parameters have not adjusted
        elif (dataset == 150):
            best_cro = e.evolution_cro(65, 550, 100000.0, 3000.0, 11, 1, f)
        # parameters have not adjusted
        elif (dataset == 280):
            best_cro = e.evolution_cro(65, 550, 100000.0, 3000.0, 11, 1, f)
            
        best_cro[0].writein(f)
        best_cro[0].printout()
#        best_cro[0].drawout(points)
    
def GA_benchline(dataset=52):
    initer = Initer.Initer(dataset)
    points = initer.points
    distances = initer.distances
    e = Evolution.Evolution(distances, points)
    
    with open("log_benchline_" + str(dataset), "a") as f:
        # about 60 seconds
        if (dataset == 52):
            best_benchline = e.evolution_benchline(130, 700, 100000.0, 3000.0, 11, 1, f)
        # about 10 mins
        elif (dataset == 130):
            best_benchline = e.evolution_benchline(300, 1500, 100000.0, 3000.0, 11, 1, f)
        # parameters have not adjusted
        elif (dataset == 150):
            best_benchline = e.evolution_benchline(65, 550, 100000.0, 3000.0, 11, 1, f)
        # parameters have not adjusted
        elif (dataset == 280):
            best_benchline = e.evolution_benchline(65, 550, 100000.0, 3000.0, 11, 1, f)
            
        best_benchline[0].writein(f)
        best_benchline[0].printout()
#        best_benchline[0].drawout(points)

# test for 10 times
def test_GA(dataset):
    open("log_ga_" + str(dataset), "w").close()
        
    t1 = timeit.Timer("GA(" + str(dataset) + ")", "from main import GA")
    for i in range(5):
        time = t1.timeit(number=1)
        with open("log_ga_" + str(dataset), "a") as f:
            f.write("use time : ")
            f.write(str(time))
            f.write("\n\n")

# test benchline for 10 times
def test_GA_benchline(dataset):
    open("log_benchline_" + str(dataset), "w").close()
    
    t1 = timeit.Timer("GA_benchline(" + str(dataset) + ")", "from main import GA_benchline")
    for i in range(5):
        time = t1.timeit(number=1)
        with open("log_benchline_" + str(dataset), "a") as f:
            f.write("use time : ")
            f.write(str(time))
            f.write("\n\n")
        
#GA_benchline(130)
#GA(130)
#test_GA_benchline(130)
#test_GA(130)
            
# =============================================================================
# 130tsp global best distance 6110.86094968039
#
# initer = Initer.Initer(130)
# distances = initer.distances
# path = [1,41,39,117,112,115,28,62,105,128,16,45,5,11,76,109,61,129,124,64,69,86,88,26,7,97,70,107,127,104,43,34,17,31,27,19,100,15,29,24,116,95,79,87,12,81,103,77,94,89,110,98,68,63,48,25,113,32,36,84,119,111,123,101,82,57,9,56,65,52,75,74,99,73,92,38,106,53,120,58,49,72,91,6,102,10,14,67,13,96,122,55,60,51,42,44,93,37,22,47,40,23,33,21,126,121,78,66,85,125,90,59,30,83,3,114,108,8,18,46,80,118,20,4,35,54,2,50,130,71]
# for i in range(130):
#     path[i] = path[i] - 1
# import Gene
# g = Gene.Gene(path, distances)
# g.printout()
# g.drawout(initer.points, 130)
# =============================================================================
            
            
            