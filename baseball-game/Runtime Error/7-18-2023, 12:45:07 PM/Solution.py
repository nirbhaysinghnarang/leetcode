// https://leetcode.com/problems/baseball-game

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for o in operations:
            if o == '+':
                records.append(records[-1] + records[-2])
            elif o == 'D':
                records.append(records[-1]*2)
            elif o == 'C':
                records.pop()
            else:
                records.append(o)
        print(records)
        return sum(records)