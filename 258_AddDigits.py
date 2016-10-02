class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        i=0
        sum = 0
        if num<10:
            return num
        else:
            for i in str(num):
                print str(num)
                print i,
                sum += int(i)
            return Solution.addDigits(self, int(sum))

# 1. it is important to have a sum to record of the i
# 2. str() to convert an interger to the string in order to get the index
