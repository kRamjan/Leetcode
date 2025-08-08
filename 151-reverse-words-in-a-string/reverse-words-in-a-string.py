class Solution(object):
    def reverseWords(self, s):
        string = s.strip() 
        splitted = " ".join(string.split()[::-1]) 
        return splitted