def remove_duplicates(nums):
    if not nums:
        return 0

    nums.sort()

    slow = 0
    fast = 1

                                                                  
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow += 1
                       
            nums[slow] = nums[fast]
        fast += 1

                                              
    nums[:] = nums[:slow + 1]

    return nums


nums = [1, 2, 2, 3, 4, 4, 4, 5]
nums = remove_duplicates(nums)
print(nums)