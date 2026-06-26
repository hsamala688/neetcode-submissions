class Solution:

    def encode(self, strs: List[str]) -> str:
        
        holder = ""
        for strings in strs:
            word_reversed = strings[::-1]

            holder += f"{len(strings)}#{word_reversed}"

        return holder



    def decode(self, s: str) -> List[str]:
        
        result = []

        normal = ""

        i = 0

        while i < len(s):
            if s[i].isdigit():
                j = s.find('#', i)
                length = int(s[i:j])
                normal = s[j + 1 : j + 1 + length][::-1]
                result.append(normal)
                normal = ""
                i = j + 1 + length
            else:
                i += 1

        return result
            
        



