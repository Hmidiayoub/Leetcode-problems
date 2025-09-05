def item_removal_from_list(nums, item) :
    slow = 0
    for fast in range(len(nums)) :
        if nums[fast] != item :
           nums[slow] = nums[fast]
           slow += 1 
    return slow
nums = [0,3,5,13,67,32,83,45,68]
item = 5
print(item_removal_from_list(nums,item))
    