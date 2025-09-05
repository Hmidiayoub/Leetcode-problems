def combinationSum(nums, target) :
        sol, res = [], []
        n = len(nums)
        def backtracking(i, sumation) :
            if  sumation == target :
                res.append(sol[:])
                return
            if sumation > target or i == n :
                return
            backtracking(i+1, sumation)
            print(f" <empty backtracking> sum at {i} = {sol}")
            sol.append(nums[i])
            backtracking(i, sumation + nums[i])
            print(f"sum at {i} = {sol}")
            sol.pop()
        backtracking(0, 0)
        return res
nums = [2,5,6,9]
target = 9
print(f"the final result = {combinationSum(nums, target)}")