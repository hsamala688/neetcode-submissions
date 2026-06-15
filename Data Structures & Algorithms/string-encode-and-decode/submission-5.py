class Solution:

    def encode(self, strs: List[str]) -> str:

        reversed_strs = []
        
        for i in range(len(strs)):
            reverse = ""
            temp = strs[i]
            for c in temp:
                reverse = c + reverse
            reversed_strs.append(reverse)

        holder = ""
        for i in range(len(strs)):
            holder = holder + str(len(strs[i])) + '#' + reversed_strs[i]

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
            
        



