class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return sorted(list(set(Counter(arr).values()))) == sorted(list(Counter(arr).values()))