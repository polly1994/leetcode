class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(1, n+1):
            if (i%3 == 0 and i%5!=0):
                tmp = 'Fizz'
            elif (i%5 == 0 and i%3!=0):
                tmp = 'Buzz'
            elif (i%3 == 0 and i%5==0):
                tmp = 'FizzBuzz'
            else:
                tmp = str(i)
            l.append(tmp)
        return l

# 1. list.append() instead of list[i] = 5
  2. str(i)
