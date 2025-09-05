def findMin(nums) -> int:
    left, right = 0, len(nums)-1
    while left < right :
        mid = left + (right - left) // 2
        if nums[mid] < nums[right] :
            right = mid
            print(f"right changed ! {right} and middle = {mid}")
        else :
            left = mid + 1
        print(f"left = {left} , right = {right} , middle = {mid}")
    return nums[left]
nums = [3,4,5,6,7,1,2,3]
print(f"min number = {findMin(nums)}")