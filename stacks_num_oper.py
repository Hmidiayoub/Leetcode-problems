import math
def evalRPN(tokens) :
        current_nums = []
        for i in range(len(tokens)) :
            if tokens[i] == "+" :
                current_nums.append(current_nums.pop() + current_nums.pop())
            elif tokens[i] == "-" :
                a, b = current_nums.pop(), current_nums.pop()
                current_nums.append(b - a)
            elif tokens[i] == "*" :
                current_nums.append( current_nums.pop() * current_nums.pop())
            elif tokens[i] == "/" :
                a, b = current_nums.pop(), current_nums.pop()
                current_nums.append(math.floor(b / a))
            else :
                current_nums.append(int(tokens[i]))
            print(current_nums)
        return current_nums[-1]
tokens = ["4", "13", "5", "/", "+"]
print(f"final result = {evalRPN(tokens)}")