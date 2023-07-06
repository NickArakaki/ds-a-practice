/**
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
*/

function minSumArray(target, nums) {
  let l = 0;
  let r = 0;

  minLength = Infinity;
  currSum = 0;

  while (r < nums.length) {
    currSum += nums[r];

    while (currSum >= target) {
      minLength = Math.min(minLength, r - l + 1);
      currSum -= nums[l];
      l++;
    }

    r++;
  }
}

console.log(minSumArray(7, [2, 3, 1, 2, 4, 3]) == 2);
console.log(minSumArray(4, [1, 4, 4]) == 1);
console.log(minSumArray(11, [1, 1, 1, 1, 1]) == 0);
