class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        hash_map = {}

        for strings in strs:

            key = "".join(sorted(strings))

            if key not in hash_map:

                hash_map[key] = []

            hash_map[key].append(strings)

        return sorted(hash_map.values(), key = len)
