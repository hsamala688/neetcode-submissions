class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort() # nlogn

        left = 0
        right = len(people) - 1

        amount = 0

        while left <= right:
            remain = limit - people[right]
            right -= 1
            amount += 1
            if left <= right and remain >= people[left]:
                left += 1

        return amount
            

            
