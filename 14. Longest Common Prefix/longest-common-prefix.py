class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ""
        n = len(strs)
        if( n == 1 ):
            return strs[0]

        if( "" in strs):
            return ""
            
        n = len(strs[1]) 
        m = len(strs[0])
        
        v2 = strs[1]
        v1 = strs[0]
        j=0
        while(j < min(m, n)):
            if v1[j] == v2[j]:
                common += v1[j]
                j +=1
            else:
                break
        
        for i in range (1, len(strs)):
            temp = ""
            n = len(strs[i]) 
            v = strs[i]
            j=0
            while(j < min (len(common), n)):
                if v[j] == common[j]:
                    temp += v[j]
                    j +=1
                else:
                    break
            common = temp
        return common