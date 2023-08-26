class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if len(pairs) == 1:
            return 1
        
        pairs.sort(key=lambda pair: pair[1])  # Sort pairs based on the second element
        
        memo = {}  # Memoization dictionary
        
        def dfs(i):
            if i in memo:
                return memo[i]
            
            longest_chain = 1 
            
            for j in range(i + 1, len(pairs)):
                if pairs[j][0] > pairs[i][1]:
                    longest_chain = max(longest_chain, 1 + dfs(j))
            
            memo[i] = longest_chain
            return longest_chain
        
        maxChain = 0
        for i in range(len(pairs)):
            maxChain = max(maxChain, dfs(i))
        
        return maxChain
