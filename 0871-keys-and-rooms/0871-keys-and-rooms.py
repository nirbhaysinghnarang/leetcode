class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            for portal in rooms[room]:
                dfs(portal)


        dfs(0)
        return len(visited) == len(rooms)