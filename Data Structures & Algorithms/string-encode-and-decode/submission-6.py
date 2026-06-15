class Solution:

    def encode(self, strs: List[str]) -> str:

        holder = ""

        for i in range(len(strs)):
            reverse = ""
            temp = strs[i]
            length = str(len(temp))
            holder = holder + length + '#'
            for c in temp:
                reverse = c + reverse
            holder = holder + reverse


        return holder

    def decode(self, s: str) -> List[str]:

        result = []

        normal = ""

        i = 0

        while i < len(s):
            if s[i].isdigit():
                j = i
                while s[j].isdigit():
                    j += 1
                length = int(s[i:j])
                normal = s[j + 1 : j + 1 + length][::-1]
                result.append(normal)
                normal = ""
                i = j + 1 + length

            else:
                i += 1

        return result
            
        



