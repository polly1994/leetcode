class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num > 0 and num&(num-1) == 0 and num&0x55555555!=0)
        
        #use '0x55555555' to check if the '1' bit is in the right place
        # 0101 0101 0101 0101 0101 0101 0101 0101
        
        
