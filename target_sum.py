def min_target_sum(nums,target) :
    result = float('inf')
    j = 0
    numSum = 0
    for i in range(len(nums)) :
        numSum += nums[i]
        while numSum >= target :
            subNums = i - j + 1
            result = min(result,subNums)
            numSum -= nums[j]
            j += 1
    return result if result < float('inf') else 0
nums = [2,3,1,2,4,3]
target = 7
print(f"The minimum subarray length = {min_target_sum(nums,target)}")