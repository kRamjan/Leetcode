class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        char_set = set()
        maximum = 0 
        left = 0 
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left]) 
                left += 1 
            char_set.add(s[right]) 
            maximum = max(maximum,right - left + 1) 
        return maximum
         