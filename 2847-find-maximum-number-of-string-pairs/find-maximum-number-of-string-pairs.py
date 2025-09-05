class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        # num = [w.strip() for w in words.spilt(",")] 
        length = len(words) 

        count = 0 
        for i in range(length):
            for j in range(i+1,length):
                if words[i] == words[j][::-1]:
                    count += 1 
        return count
        