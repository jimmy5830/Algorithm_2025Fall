class Solution(object):
    def exchangesort(S):
        n = len(S)

        for i in range(n):
            for j in range(n):
                if (S[i] < S[j]):
                    temp = S[i]
                    S[i] = S[j]
                    S[j] = temp
        return S
        
        