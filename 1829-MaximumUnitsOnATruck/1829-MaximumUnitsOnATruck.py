# Last updated: 2/5/2026, 7:40:38 AM
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x : -x[1])
        maxUnits=0
        for btype,units in boxTypes:
            if truckSize==0:
                return maxUnits
            take=min(truckSize,btype)
            maxUnits+=(take*units)
            truckSize-=take
        return maxUnits