class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """ 
        n = start ^ goal  
        count = 0
        while n != 0: 
            count += 1 
            n = n & (n-1) 
        return count
            
        