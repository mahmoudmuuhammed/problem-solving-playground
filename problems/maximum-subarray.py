def maxSubArray(nums: list):
    curSum = maxSum = nums[0];
    for num in nums[1:]:
        curSum = max(num, curSum + num);
        print(curSum);
        maxSum = max(maxSum, curSum);

    return maxSum


data = maxSubArray([2, 2, -4, 5, 3]);