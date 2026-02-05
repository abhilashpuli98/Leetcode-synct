# Last updated: 2/5/2026, 7:40:12 AM
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        isBulky=max(length,width,height)>=10**4 or (length*width*height)>=10**9
        isHeavy=mass>=100
        return ("Neither",'Heavy','Bulky','Both')[isBulky*2+isHeavy]