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

        if not s[0] in left_ends:
            return False
        st = []
        for char in s:
            print(char)
            if char in left_ends:
                st.append(char)
            else:
                corr_left = hm.get(char)
                if st and st[-1] == corr_left:
                    st.pop()
                else:
                    return False

        return st == []
