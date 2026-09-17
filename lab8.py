#LAB 8: QUICKSORT ALGORITHM

def quick_sort(arr:list):
    nums = arr.copy()
    if len(nums)<=1:
        return nums
    low = 0 
    high = len(nums)-1
    i = low
    j = high
    pivot = nums[low]
    while i<j:
        while nums[i]<=pivot and i<high:
            i+=1
        while nums[j]>=pivot and j>low:
            j-=1
        if i<j:
            nums[i],nums[j] = nums[j],nums[i]
    nums[low] , nums[j] = nums[j] , nums[low]
    print(nums)
    if low<high:
        nums[low:j] = quick_sort(nums[low:j])
        nums[j+1:]=quick_sort(nums[j+1:])
        low+=1
        high-=1
    return nums

print(quick_sort([20, 3, 14, 1, 5]))