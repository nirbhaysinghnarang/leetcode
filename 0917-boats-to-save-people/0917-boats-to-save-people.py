class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        L = 0
        R = len(people)-1

        cnt = 0
        while L<=R:
            s = people[L] + people[R]
            if s <= limit:
                L+=1
                R-=1
            else:
                R-=1
            cnt+=1


        return cnt