"""
t = 10
pos [1, 4]
speed [3, 2]

pos_left_for_last = 10 - 4 = 6
time_left_for_prev_to_catchup = time_left_for_last_to_finish = 6 / 2 = 3

3 * (3 - 2) = 3 (positions will prev be able to catch up within time left)
if 3 >= 4 - 1, (if it is larger than distance between cars, then it will catch up)



t = 11
pos [1, 2, 5]
speed [10, 3, 2]

pos_left_for_last = 11 - 5 = 6
time_left_for_prev_to_catchup = time_left_for_last_to_finish = 6 / 2 = 3

3 * (3 - 2) = 3 (positions will prev be able to catch up within time left)
if 3 >= 4 - 1, (if it is larger than distance between cars, then it will catch up)

ok, we know that 2nd will catch up 3rd.

now, will 1st car be able to catch up 2nd?
time_left_for_1st_to_catchup = time_left_for_2nd_to_finish = 3

3 * (10 - 3) = 21 (positions will 1st be able to catch up within time left)
if 21 => 3, then it will catch up

i'm thinking about a stack, where stack contains everything 

"""

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
        
            
            
            

        