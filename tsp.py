import math
import itertools
import random
from multiprocessing import Process, cpu_count

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
def setup():
    global distancedict
    distancedict = {}
    points = []
    empty_list = [None] * 10
    for i in range(int(input("num of points?"))):
        points.append((random.randint(1,500),random.randint(1,500)))
    return points

def getdistance(point1, point2):
    return math.sqrt(((point1[0]-point2[0])**2)+((point1[0]-point2[0])**2))
def logan(points, n):
    shortest = 1000000000000000000
    shortest_order = None
    for i in points:
        print(i)
        distance = 0
        for f in range(len(points)-2):
            print(f)
            distance += getdistance(i[f],i[f+1])
        if shortest>distance:
            shortest = distance
            shortest_order = i
    
    


if __name__ == '__main__':
    thread_count = cpu_count()
    points = setup()
    permu = itertools.permutations(points, len(points))
    splits = list(split(list(permu), thread_count))
    logan(splits[1],1)
    #threads = [Process(target=logan, args=(splits[y],y)) for y in range(thread_count)]
    #for i in threads:
        #i.start()
    #for i in threads:
        #i.join()
    #for i in threads:
        #i.terminate()