def rotate_arr(nums, rotate_by):
    if not nums:
        return nums
    
    rotate_by = rotate_by % len(nums) 
    
    if rotate_by == 0:
        return nums[:]
    
    return nums[-rotate_by:] + nums[:-rotate_by]

print(rotate_arr([1,2,3,4,5],1))