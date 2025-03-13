import math
import itertools
import random
from multiprocessing import Process, cpu_count, Value, Array
import time
def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
def setup():
    global percentage
    percentage = 0
    f = open("Advanced_Programming/demofile.txt", "w")
    f.write('1000000000000000')
    t = open("Advanced_Programming/database.txt")
    b = t.read().split("\n")
    start = (int(b[0].split(" ")[1]),int(b[0].split(" ")[2]))
    points = []
    for i in range(len(b)-1):
       points.append((int(b[i+1].split(" ")[1]),int(b[i+1].split(" ")[2])))
    points = points[0:(int(input("how many datapoints")))]
    
    return (points,start)

def getdistance(point1, point2):
    return math.sqrt(((point1[0]-point2[0])**2)+(point1[1]-point2[1])**2)
def logan(points, n, start,num,array):
    points1 = list(points)
    shortest = 1000000000000000000
    shortest_order = None
    for i in points1:
        i1 = list(i)
        i1.insert(0,start)
        i1.insert(len(i1),start)
        distance = 0
        for f in range(len(i)-2):
            distance += getdistance(i1[f],i1[f+1])
        if shortest>distance:
            shortest = distance
            shortest_order = i1
    if num.value>shortest:
        num.value = shortest
        listb = []
        for i in shortest_order:
            listb.append(i[0])
            listb.append(i[1])
        for i in range(len(array)):
            array[i] = listb[i]

        array = listb
    print(f"{n}/{cpu_count()} completed")




if __name__ == '__main__':
    global permu
    num = Value('d',1000000000.0)
    array = Array('i', 12)
    thread_count = cpu_count()
    l = setup()
    points = l[0]
    start = l[1]
    print(f"CPU Count: {thread_count}")
    print("Calculating all permutations:")
    permu = itertools.permutations(points, len(points))
    permu = list(permu)
    print("Permutations Done!")
    print("Splitting List:")
    splits = list(split(permu, thread_count))
    print("Done!")
    print(f"{len(permu)} Permutations to calculate")
    print(f"Est. Time = {52.35404658317566*len(permu)/39916800} secs")
    #logan(splits[1],1)
    threads = [Process(target=logan, args=(splits[y],y,start, num, array)) for y in range(thread_count)]
    start_time =time.time()
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print(f"Shortest distance: {num.value}")
    print(f"Solution: {str(list(array))}")

    end_time = time.time()
    print("Done! Time to calculate: " + str(end_time-start_time))
    for i in threads:
        i.terminate()