/*
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

    * Each element of nums is in exactly one pair, and
    * The maximum pair sum is minimized.

Return the minimized maximum pair sum after optimally pairing up the elements.
*/

const minPairSum = (nums) => {
  // sort nums
  nums.sort((a, b) => a - b);
  // track cur max
  let curMax = -Infinity;
  // l = 0, r = -1
  let l = 0;
  let r = nums.length - 1;

  while (l < r) {
    curMax = Math.max(curMax, nums[l] + nums[r]);
    l++;
    r--;
  }

  return curMax;
  // iterate while l and r are not the same
  // curMax = max(curMax, nums[l] + nums[r])
  // return curMax
};

module.exports.minPairSum = minPairSum;
