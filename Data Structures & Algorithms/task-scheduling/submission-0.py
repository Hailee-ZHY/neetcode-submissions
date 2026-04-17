class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # create a hash map for count
        HashCnt = {}
        for i in tasks:
            if i in HashCnt.keys():
                HashCnt[i] += 1 
            else:
                HashCnt[i] = 1

        # put the dic result into heap
        MaxHeap = [ -cnt for cnt in HashCnt.values()]
        heapq.heapify(MaxHeap)
        
        # process the most frequent task first
        time = 0 
        q = deque() #[-cnt, idelTime]

        while MaxHeap or q:
            time += 1 
            if MaxHeap:
                cnt = 1 + heapq.heappop(MaxHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(MaxHeap, q.popleft()[0])
        return time        

