def generateParenthesis(n) :
    sol, result = [], []
    def backtrack_para(open_para, close_para) :
        print(f"entered backtracking function with open : {open_para} and close : {close_para}")
        if open_para == close_para == n :
            sol.append("".join(result))
            return
        if open_para < n :
            result.append('(')
            backtrack_para(open_para+1, close_para)
            result.pop()
        if close_para < open_para :
            result.append(')')
            backtrack_para(open_para, close_para+1)
            result.pop()
    backtrack_para(0,0)
    return sol
number = 3
print(generateParenthesis(number))