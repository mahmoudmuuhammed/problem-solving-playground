# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: list):
        my_hash = {};
        for i in nums:
            if i in my_hash:
                return True;
            my_hash[i] = True;
        return False;

nums = list(map(int, input().strip().split(' ')));

sol = Solution();

result = sol.containsDuplicate(nums);
print(result);