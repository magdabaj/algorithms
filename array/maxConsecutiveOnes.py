nums = [1, 1, 0, 1, 1, 1]


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number = 0
        currentLength = 0
        for i in nums:
            if i == 1:

                currentLength = currentLength + 1
                print(currentLength)
                if currentLength > number:
                    number = currentLength
            else:

                currentLength = 0
        return number
