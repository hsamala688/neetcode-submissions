class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for op in operations:

            if op == '+' :

                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1)
                stack.append(val2)
                stack.append(val2 + val1)

            elif op == 'C':

                stack.pop()

            elif op == 'D':

                val1 = stack.pop()

                stack.append(val1)

                stack.append(2 * val1)

            else:

                stack.append(int(op))

        
        return sum(stack)