'''
Binary Search
Returns the index for the target element. If target element is not found, returns index of where it would be in sorted array.

Time: O(n)
Space: O(1)
'''
def binarySearch(nums: [int], target: int) -> int:
  if len(nums) == 1:
    return 0 if target <= nums[0] else 1
  
  left, right = 0, len(nums) - 1

  while(left <= right):
    mid = (left + right) // 2
    
    if target == nums[mid]:
      return mid
    elif target > nums[mid]:
      left = mid + 1
    else:
      right = mid - 1
    
  return left

nums = [1, 2, 3, 4]
target = 0
print(binarySearch(nums, target))
