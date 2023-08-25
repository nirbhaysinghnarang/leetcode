class Solution:
    def expand(self, s: str) -> List[str]:
        if not s:
            return
        words = []

        def _getOptions(s):
            options = []
            toIgnore = set({'{','}',','})
            optionsOpen = s[0] == "{"
            for char in s:
                if char == "{":
                    nestedOptions = []
                    optionsOpen = True
                elif optionsOpen and char not in toIgnore:
                    nestedOptions.append(char)
                elif char == "}":
                    options.append(nestedOptions)
                    optionsOpen = False
                else:
                    if char not in toIgnore:
                        options.append(char)
            return options


        options = _getOptions(s)
        
        paths = []
        def _dfs(i, path):
            nonlocal options
            nonlocal paths
            if i >= len(options):
                paths.append(path)
                return
            if type(options[i]) is list:
                for char in options[i]:
                    _dfs(i+1, path+char)
            else:
                _dfs(i+1, path+options[i])
                
        _dfs(0, "")
        return sorted(paths)