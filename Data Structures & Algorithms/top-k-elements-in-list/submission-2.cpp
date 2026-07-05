class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;

        for (int num : nums) {
            freq[num]++;
        }

        vector<pair<int, int>> arr;

        for (auto it = freq.begin(); it != freq.end(); ++it) {
            arr.push_back(make_pair(it->second, it->first));
        }

        sort(arr.begin(), arr.end());

        vector<int> result;

        for (int i = arr.size() - 1; i >= 0 && k > 0; --i, --k) {
            result.push_back(arr[i].second);
        }

        return result;
    }
};