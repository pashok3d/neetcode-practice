class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleets = 0
        pos_speed = list(zip(position, speed))
        pos_speed = sorted(pos_speed, key=lambda x: x[0])
        for pos, speed in reversed(pos_speed): # 0, 1
            if stack:
                car_ahead = stack[0] # (7, 1)
                time_to_finish_car_ahead = (target - car_ahead[0]) / car_ahead[1] # 3
                time_to_finish = (target - pos) / speed # 10 / 1 = 10
                if time_to_finish_car_ahead < time_to_finish: # true
                    # wont catch up
                    stack.pop()
                    fleets += 1
                    stack.append((pos, speed))
            else:
                stack.append((pos, speed)) # [(7, 1)]
        for i in stack:
            fleets += 1
        return fleets
        
            
            
            

        