from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums_m = nums1[:m]
        checkpoint_1 = 0
        checkpoint_2 = 0
        for i in range(len(nums1)):
            print(i)
            num_1 = nums_m[checkpoint_1] if (checkpoint_1 is not None and checkpoint_1 <= m-1) else None
            num_2 = nums2[checkpoint_2] if (checkpoint_2 is not None and checkpoint_2 <= n-1) else None
            if num_1 is None and num_2 is None:
                break
            elif (num_1 is None):
                nums1[i] = num_2
                checkpoint_2 += 1
            elif (num_2 is None):
                nums1[i] = num_1
                checkpoint_1 += 1
            elif num_1 >= num_2:
                nums1[i] = num_2
                checkpoint_2 += 1
            elif num_1 < num_2:
                nums1[i] = num_1
                checkpoint_1 += 1