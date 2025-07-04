class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a = []
        for x in nums:
            for y in str(x):
                a.append(int(y))
        return a