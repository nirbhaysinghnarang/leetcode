class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []

        st = []

        for curr in asteroids:
            while st and st[-1] > 0 and curr < 0:
                prev = st.pop()
                if abs(prev) == abs(curr):
                    curr = 0  # Both asteroids annihilate each other
                elif abs(prev) > abs(curr):
                    curr = prev  # Prev asteroid survives
            if curr != 0:
                st.append(curr)

        return st
