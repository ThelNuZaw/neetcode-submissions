class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        people.sort()
        left = 0
        right = len(people) - 1
        while left < right:
            if people[left] + people[right] > limit:
                if people[right] <= limit:
                    right -= 1
                    boat += 1
                elif people[left] == limit:
                    left += 1
                    boat += 1
                else:
                    right -= 1
            else:
                left += 1
                right -= 1
                boat += 1
        if left == right:
            if people[left] <= limit:
                boat += 1
        return boat


                
