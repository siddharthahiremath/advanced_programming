import math
import itertools
import random
import time
start_time = time.time()
points = [(6734,1453),(2233,10),(5530,1424),(401,841),(3082,1644)]
#for i in range(int(input("num of points?"))):
    #points.append((random.randint(1,500),random.randint(1,500)))
def getdistance(point1, point2):
    return math.sqrt(((point1[0]-point2[0])**2)+((point1[0]-point2[0])**2))

shortest = 1000000000000000000
shortest_order = None
for i in itertools.permutations(points, len(points)):
    distance = 0
    for f in range(len(points)-1):
        distance += getdistance(i[f],i[f+1])
    if shortest>distance:
        shortest = distance
        shortest_order = i
end_time = time.time()
print(distance)
print(end_time-start_time)