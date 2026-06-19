class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operands = []

        for char in tokens:
            if char.lstrip('-').isdigit():
                operands.append(int(char))
            else:
                val2 = operands.pop()
                val1 = operands.pop()
                if char == '+':
                    operands.append(val1 + val2)
                elif char == '-':
                    operands.append(val1 - val2)
                elif char == '*':
                    operands.append(val1 * val2)
                elif char == '/':
                    operands.append(int(val1 / val2))

        return operands[0]