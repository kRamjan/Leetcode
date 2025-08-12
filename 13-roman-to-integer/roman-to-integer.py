class Solution(object):
    def romanToInt(self, s):
        dict_1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} 
        count = 0 
        i = 0 
        while i < len(s):
            if i+1 < len(s) and dict_1[s[i]] < dict_1[s[i+1]]:
                count += dict_1[s[i+1]] - dict_1[s[i]] 
                i+=2 
            else:
                count += dict_1[s[i]] 
                i+=1 
        return count