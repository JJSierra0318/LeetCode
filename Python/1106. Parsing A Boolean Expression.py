'''
We keep a stack for the operands and another for the operations, whenever we reach
a ")" we save in a list all the operands inside the parenthesis and apply the 
corresponding operation and then save the result in the initial operands stack
'''

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operands = []
        operations = []
        for char in expression:
            if char in ["(", "t", "f"]:
                operands.append(char)
            elif char in ["&", "|", "!"]:
                operations.append(char)
            if char == ')':
                temp = []
                while operands[-1] != "(":
                    temp.append(True if operands.pop() in ["t", True] else False)
                operands.pop()
                if operations[-1] == "|":
                    operands.append(any(temp))
                elif operations[-1] == "&":
                    operands.append(all(temp))
                else:
                    operands.append(not temp[-1])
                operations.pop()
        return operands[0]
        