class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def maxConsecutiveXs(answer, k, param):
            max_cnt = 0
            L = 0
            win_F_cnt = 0
            for R in range(len(answer)):
                if answer[R]==param:
                    win_F_cnt+=1
                while win_F_cnt > k:
                    if answer[L]==param:
                        win_F_cnt-=1
                    L+=1
                max_cnt = max(max_cnt, R-L+1)
            return max_cnt
        return max(maxConsecutiveXs(answerKey, k, 'T'), maxConsecutiveXs(answerKey, k, 'F'))

