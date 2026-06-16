class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isThere = []

        for i in nums:
            if i in isThere:
                return True 
            else:
                isThere.append(i)
        return False

        