class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        dol5 = dol10 = 0

        for bill in bills:
            if bill == 5:
                dol5 += 1

            elif bill == 10:
                dol10 += 1
                dol5 -= 1

            elif dol10 > 0:
                dol10 -= 1
                dol5 -= 1
            
            else:
                dol5 -= 3

            if dol5 < 0:
                return False

        return True