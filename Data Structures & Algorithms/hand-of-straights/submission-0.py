class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
           return False 

        hashCnt = {}
        for i in hand:
            hashCnt[i] = hashCnt.get(i, 0) + 1 
        
        minH = list(hashCnt.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first+groupSize):
                if i not in hashCnt:
                    return False
                hashCnt[i] -= 1
                if hashCnt[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
                
