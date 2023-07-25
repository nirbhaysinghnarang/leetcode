// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token == '-':
                op_1 = st.pop()
                op_2 = st.pop()
                st.append(op_1 - op_2)

            elif token == '+':
                op_1 = st.pop()
                op_2 = st.pop()
                st.append(op_1 + op_2)
            
            elif token == '*':
                op_1 = st.pop()
                op_2 = st.pop()
                st.append(op_1 + op_2)

            elif token == '/':
                op_1 = st.pop()
                op_2 = st.pop()
                st.append(op_1 // op_2)

            else:
                st.append(int(token))
            
            print(st)
        return st[0]