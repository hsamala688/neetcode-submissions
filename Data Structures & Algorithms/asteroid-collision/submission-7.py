class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for asteroid in asteroids:

            if asteroid > 0:

                stack.append(asteroid)

            else:
                
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                    continue


                val = stack.pop()

                if abs(val) > abs(asteroid):
                    
                    stack.append(val)
                    continue
                
                elif abs(val) == abs(asteroid):

                    continue

                else:

                    while stack and stack[-1] > 0 and abs(asteroid) > abs(stack[-1]):
                        stack.pop()

                    if stack and stack[-1] > 0:
                        if abs(asteroid) < abs(stack[-1]):
                            continue 
                        elif abs(asteroid) == abs(stack[-1]):
                            stack.pop()
                            continue

                    
                    stack.append(asteroid)
        

        return stack