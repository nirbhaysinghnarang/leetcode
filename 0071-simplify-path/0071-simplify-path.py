class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//","/")

        dirs = path.split("/")
        dirs = list(filter(lambda x: x!="", dirs))

        st = []

        for _dir in dirs:
            if _dir == ".":
                continue
            elif st and _dir == "..":
                st.pop()
            else:
                st.append(_dir)
            

        st = list(filter(lambda x: x!="" and x!='.' and x!='..', st))
        return '/'+'/'.join(st)
            