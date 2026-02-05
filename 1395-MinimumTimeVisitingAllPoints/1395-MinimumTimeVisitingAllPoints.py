# Last updated: 2/5/2026, 7:41:04 AM
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(p[0]-q[0]),abs(p[1]-q[1])) for p,q in pairwise(points))
        