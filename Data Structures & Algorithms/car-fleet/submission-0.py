class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        # in my head what needs to be done is to compare hours to each other

        # 1 + (3 miles * 3 hours), 4 + ( 2 miles * 3 hours), both equal 10 so 1 fleet

        # array will store the hours, from there we can just find the number of ones that match (1), don't + 1

        
        cars = sorted(zip(position, speed), reverse = True)

        stack = []

        for pos, spd in cars:

            hours_needed = (target - pos) / spd
            stack.append(hours_needed)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:

                stack.pop()

        return len(stack)