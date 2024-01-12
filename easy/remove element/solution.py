from typing import List

def removeElement(nums: List[int], val: int) -> int:
    res = []
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            if len(res):
                index = res.pop(0)
                if index < i-count:
                    nums[index] = nums[i]
                else:
                    nums[i-count] = nums[i]
            else:
                nums[i-count] = nums[i]
        else:
            res.append(i)
            count += 1
    return count, nums


print(removeElement([0,4,4,0,4,4,4,0,2], 4))