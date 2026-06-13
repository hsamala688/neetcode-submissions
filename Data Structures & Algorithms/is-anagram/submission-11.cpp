class Solution {
public:
    bool isAnagram(string s, string t) {

        if ( s.length() != t.length() ) {
            return false;
        }

        unordered_map<char, int> seen;

        for ( const char w : s) {
            seen[w]++;
        }

        for ( const char w : t) {
            if ( seen.find(w) == seen.end() || seen[w] == 0) {
                return false;
            }
            seen[w]--;
        }
        return true;
    }
};
