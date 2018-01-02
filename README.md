# TSP-by-Genetic-Algorithm  
solve the TSP-52 problem by GA  
  
language: python(without pypy)  
  
benchline: order1 crossover  
more about order1 crossover, see http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/Order1CrossoverOperator.aspx  
  
my method: origin crossover  
example:  
parent1 : 7 1 6 2 12 5 8 11 3 9 4 10  (good performance one)  
parent2 : 1 2 3 4 5 6 7 8 9 10 11 12  (random one)  
  
step 1: randomly choose 2 neighbor point of parent2(random one), and find the two points in parent1  
parent1 : 7 1 6 2 12 5 **8** 11 3 **9** 4 10  (good performance one)  
parent2 : 1 2 <del>3</del> 4 5 6 7 **8** **9** 10 <del>11</del> 12  (random one)  
  
step 2: insert the segment 8 11 3 9 into parent2  
new one : 1 2 4 5 6 7 **8** **11** **3** **9** 10 12  
  
performance:  
52 points tsp  

    my method:  
        about 10-12 second time used  
        28% global best result probability(in 50 test)  
    benchline:  
        about 1 min time used  
        7601.660212972372 best result(in 10 test) (global best 7544)  
        
130 points tsp  

    my method:  
        about 90 seconds time used  
        7601.660212972372 best result(in 10 test) (global best 6110.86094968039)  
    benchline:  
        about 10 min time used  
        8466.846934247065 (1 test)  

