



# recursion with memo, O(len(s1)*len(s2))
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # memo is to save failure matches
        # when s1[:i], s2[:j] matches with s3[:i+j], 
        # but s1[i:], s2[j:] don't match with s3[i+j:], then save (i, j)
        # so that we don't check this pair again
        self.memo = set()  
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        return self.isInterleaveHelper(s1, s2, s3, 0, 0, 0)
    
    def isInterleaveHelper(self, s1, s2, s3, i, j, k):
        if i >= len(s1):
            return s2[j:] == s3[k:]
        if j >= len(s2):
            return s1[i:] == s3[k:]
        if k >= len(s3):
            return False
        
        if (i,j) in self.memo:
            return False
        
        if s1[i] == s3[k]:
            if self.isInterleaveHelper(s1, s2, s3, i+1, j, k+1):
                return True
        if s2[j] == s3[k]:
            if self.isInterleaveHelper(s1, s2, s3, i, j+1, k+1):
                return True
        
        self.memo.add((i,j))
        return False
    
