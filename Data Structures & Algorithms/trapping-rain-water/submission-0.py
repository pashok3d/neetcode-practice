class Solution:
    def trap(self, height: List[int]) -> int:
        active_threads = {}
        area = 0
        for h in height:
            # release threads into area
            released_threads_areas = [active_threads.pop(h_i, 0) for h_i in range(1, h+1)]
            area += sum(released_threads_areas)

            # propagate active threads
            for k in active_threads.keys():
                active_threads[k] += 1
            
            # start new threads for h
            for h_i in range(1, h+1):
                active_threads[h_i] = 0
        return area

            

        