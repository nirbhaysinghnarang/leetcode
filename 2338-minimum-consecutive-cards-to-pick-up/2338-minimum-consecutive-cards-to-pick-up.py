class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_count = float('inf')
        L = 0
        win_set = set()
        for R in range(len(cards)):
            new_card = cards[R]
            while new_card in win_set:
                count = R-L+1
                min_count = min(min_count, count)
                win_set.remove(cards[L])
                L+=1
            win_set.add(new_card)
        return -1 if min_count == float('inf') else min_count