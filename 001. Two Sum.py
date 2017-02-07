"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(0, len(nums)):
            #print i
            for j in range(i + 1, len(nums)):
                #print j
                if nums[i] + nums[j] == target:
                   #print 'Found a solution'
                   result.append(i)
                   result.append(j)
                   return result
				   
				   
#for loop, indexing lists, adding to a list