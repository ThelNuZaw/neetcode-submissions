class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []

        pair = list(sorted(zip(position,speed), reverse = True))
        #print(pair)
        for p, s in pair:
            times = round((target - p) / s, 1)
            time.append(times)
            #print(times)
            if len(time) >= 2:
                if(time[-1] <= time[-2]):
                    time.pop()
    
        fleet = len(time)
        return fleet
