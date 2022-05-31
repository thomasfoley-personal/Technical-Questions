# Given an array of integers arr and an integer k, find the kth largest element

# Initial thoughts: sort arr, somehow remove duplicates, then index

# Video thoughts 1: Use a set and remove max element each iteration until reaching k
# Video thoughts 2: Use sorted array and then arr[n-k], *assumes no duplicated... should be a question to ask*
# Video thoughts 3: Use a heapsort (priority queue)... *DEEP SIGHS*
import heapq


# Video thoughts 3: Use a heapsort (priority queue)... *DEEP SIGHS*
def usingHeap(arr,k):
    # Need to use -elem because default coding of heap is min, not max which is what we need
    arr = [-elem for elem in arr]
    # Must re-heapify our list/priority queue
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)

if __name__ == '__main__':
    arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
    target = 4
    arr.sort()
    print(target, " largest element = ", indexPosition(arr, target))
