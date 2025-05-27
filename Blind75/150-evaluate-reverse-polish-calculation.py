class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # build a stack to calculate
        for num in tokens:
            if num == "+":
                stack.append(stack.pop() + stack.pop())
            elif num == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif num == "*":
                stack.append(stack.pop() * stack.pop())
            elif num == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(num))
        return stack[0]
