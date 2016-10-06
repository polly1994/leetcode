class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


        """
	set is a list without any duplicate element
        if nums == []:
            return False
        a = collections.Counter(nums)
        print a
        count = 0
        for i, value in enumerate(a):
            print i,value
            if value > 1:
                count +=1
        if count == 0:
            return False
        """
