import numpy as np
import heapq
import random

DATA = [random.randint(1, 10) for _ in range(10)]

# DATA = [1, 10, 5, 4]

K1 = 3

#   flag's of deleted nums: 0 - still in window, 1 - not in window, but still in heaps, 2 - not in window and deleted of heaps
DELETED_MAX = {}
DELETED_MIN = {}

print(DATA)

MEDIANS = []

minHeap = []
maxHeap = []

heapq.heapify(minHeap)
heapq.heapify(maxHeap)

evenFlag = 1 if K1 % 2 == 0 else 0

def balance_heaps(min_heap, max_heap, deleted_min, deleted_max):

    lazy_clean(min_heap, deleted_min)
    lazy_clean(max_heap, deleted_max) 

    if len(max_heap) > len(min_heap) + 1:
        tmp = heapq.heappop(max_heap)
        val = abs(tmp)
        if val in deleted_max and deleted_max[val] > 0:
            deleted_max[val] -= 1
            if deleted_max[val] == 0:
                del deleted_max[val]
        heapq.heappush(min_heap, val)

    elif len(min_heap) > len(max_heap) + 1:
        tmp = heapq.heappop(min_heap)
        val = tmp
        if val in deleted_min and deleted_min[val] > 0:
            deleted_min[val] -= 1
            if deleted_min[val] == 0:
                del deleted_min[val]
        heapq.heappush(max_heap, -val)
    
    lazy_clean(min_heap, deleted_min)
    lazy_clean(max_heap, deleted_max)

def lazy_clean(heap, deleted_dict):

    while heap and abs(heap[0]) in deleted_dict and deleted_dict[abs(heap[0])] > 0:
        val_to_clean = abs(heap[0]) 
        heapq.heappop(heap)
        
        deleted_dict[val_to_clean] -= 1
        if deleted_dict[val_to_clean] == 0:
            del deleted_dict[val_to_clean]

def addElemToMinMaxHeaps(element : int, min_heap : heapq, max_heap :heapq):

    if len(max_heap) == 0 or element <= abs(max_heap[0]):
        heapq.heappush(max_heap, -element)
    else:
        heapq.heappush(min_heap, element)


def findMediansOfHeaps(min_heap : heapq, max_heap : heapq, EvenFlag : int, deleted_dict_min, deleted_dict_max) -> float:

    lazy_clean(min_heap, deleted_dict_min)
    lazy_clean(max_heap, deleted_dict_max)

    if EvenFlag:
        median = (min_heap[0] + abs(max_heap[0])) / 2
    elif len(min_heap) > len(max_heap):
        median = min_heap[0]
    else:
        median = abs(max_heap[0])
    
    return median

iter = 0

while iter < len(DATA):
    
    addElemToMinMaxHeaps(DATA[iter], minHeap, maxHeap) 
    
    if iter >= K1:

        E_old = DATA[iter - K1]

        lazy_clean(maxHeap, DELETED_MAX) 

        if E_old <= abs(maxHeap[0]): 
            DELETED_MAX[E_old] = DELETED_MAX.get(E_old, 0) + 1
        else:
            DELETED_MIN[E_old] = DELETED_MIN.get(E_old, 0) + 1
    
    balance_heaps(minHeap, maxHeap, DELETED_MIN, DELETED_MAX)
    
    if iter >= K1 - 1:
        median = findMediansOfHeaps(minHeap, maxHeap, evenFlag, DELETED_MIN, DELETED_MAX)
        MEDIANS.append(median)

    iter += 1

print(MEDIANS)
