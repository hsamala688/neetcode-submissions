class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> holder;

        for ( int i = 0 ; i < nums.size() ; i++ ) {
            int complement = target - nums[i];

            if ( holder.find(complement) != holder.end() ) {
                return {holder[complement], i};
            }

            holder[nums[i]] = i;

        }
        return {};
    }
};
