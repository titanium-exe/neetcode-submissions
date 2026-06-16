class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using dictionary (O(1))
        index_dict = {}

        for i in range(len(nums)):
            # find the 2nd number
            second = target - nums[i]

            if second in index_dict:
                return [index_dict[second], i]
            
            index_dict[nums[i]] = i
            
        return False
        