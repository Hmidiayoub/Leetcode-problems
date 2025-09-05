
def peak_int(arr: list, left, right) -> int:
    if left == right :
        return arr[left]
    mid = (left + right) // 2
    if arr[mid] > arr[mid+1] :
        return peak_int(arr, left, mid)
    elif arr[mid] < arr[mid+1] :
        return peak_int(arr, mid+1, right)
    else :
        left_peak = peak_int(arr, left, mid)
        right_peak = peak_int(arr, mid+1, right)
        return max(right_peak, left_peak)

nums = [1, 4, 5, 7, 8, 14, 16, 17, 17, 17, 19, 16, 16, 16, 13, 11, 7, 6, 5, 4, 3, 2]
print(f"That's the Peak Number : {peak_int(nums, 0, len(nums)-1)}")