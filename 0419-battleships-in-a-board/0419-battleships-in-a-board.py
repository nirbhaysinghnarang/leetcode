class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        battleships = 0

        m = len(board)
        n = len(board[0])

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(x,y,vis):
            print(x,y,vis)
            if not(0<=x<m and 0<=y<n):
                return
            if board[x][y]!="X":
                return
            vis.add((x,y))
            board[x][y] = "."
            for del_x, del_y in dirs:
                n_x, n_y = x+del_x, y+del_y
                if ((n_x, n_y)) not in vis:
                    dfs(n_x, n_y, vis)



            

        for x in range(m):
            for y in range(n):
                if board[x][y] == "X":
                    vis = set()
                    battleships+=1
                    dfs(x,y, vis)
                    

        return battleships

        