class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a count list
        cnt = [0]*26
        for i in tasks:
            cnt[ord(i) - ord("A")] += 1 
        
        # get time
        time = 0
        waiting_queue = deque() # rest_task, next_available_time
        tasks_revert = [-i for i in cnt if i != 0]
        heapq.heapify(tasks_revert)

        while waiting_queue or tasks_revert:
            time += 1
            if tasks_revert: 
                task = heapq.heappop(tasks_revert)
                if task != -1:
                    waiting_queue.append((task+1, time + n))

            while waiting_queue and time >= waiting_queue[0][1]:
                cooldown = waiting_queue.popleft()
                heapq.heappush(tasks_revert, cooldown[0])
                
        return time