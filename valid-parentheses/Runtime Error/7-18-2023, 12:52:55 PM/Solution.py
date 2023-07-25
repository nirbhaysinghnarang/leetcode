// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 !=0:
            return False

        
        hm = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        right_ends = set(hm.keys())
        left_ends = set(hm.values())


        st = []
        for char in s:
            if char in left_ends:
                st.append(char)
            else:
                corr_left = hm.get(char)
                if st[-1]==corr_left:
                    st.pop()

        return st == []
