class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for i in range(len(details)):
            starter = 11
            cur = int("" + details[i][11] + details[i][12])
            
            if cur > 60:
                res += 1
        
        return res

                
