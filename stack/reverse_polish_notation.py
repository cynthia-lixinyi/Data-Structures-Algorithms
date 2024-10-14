from typing import List
from collections import deque
from operator import add, sub, mul

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def div(x, y):
            return int(x / y)
        operators_map = {'+': add, '-': sub, '*': mul, '/': div}

        stack = deque()
        # process each token from left to right
        # if the current token is opration, pop two elements from the stack, and compute the result and put the result back to the stack
        for token in tokens:
            if token not in operators_map.keys():
                stack.append(token)
            else:
                oprand_2 = int(stack.pop())
                oprand_1 = int(stack.pop())
                operator = operators_map[token]
                cur_res = operator(oprand_1, oprand_2)
                stack.append(cur_res)
        res = stack.pop() # the stack contains only one element
        return res
    
solution = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(solution.evalRPN(tokens))