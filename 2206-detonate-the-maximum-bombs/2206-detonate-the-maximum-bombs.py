class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph = defaultdict(set)

        for (i, bomb1) in enumerate(bombs):
            for (j, bomb2) in enumerate(bombs):
                if i!=j:
                    if self.areConnected(bomb1, bomb2):
                        graph[i].add(j)


        max_bombs = float('-inf')
        def dfs(bomb, detonated):
            if bomb in detonated:
                return
            detonated.add(bomb)
            for n_bomb in graph[bomb]:
                dfs(n_bomb, detonated)
       
        for bomb in range(len(bombs)):
            detonated = set()
            dfs(bomb, detonated)
            max_bombs = max(max_bombs, len(detonated))

        return max_bombs






    def areConnected(self, bomb1, bomb2):
        return (bomb1[0] - bomb2[0]) ** 2 + (bomb1[1] - bomb2[1]) **2 <= (bomb1[2]) ** 2

        