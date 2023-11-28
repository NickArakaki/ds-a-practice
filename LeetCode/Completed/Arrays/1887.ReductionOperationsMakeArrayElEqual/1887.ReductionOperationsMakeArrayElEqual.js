/*
Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

1. Find the largest value in nums. Let its index be i (0-indexed) and its value be largest.
   If there are multiple elements with the largest value, pick the smallest i.

2. Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.

3. Reduce nums[i] to nextLargest.

Return the number of operations to make all elements in nums equal.
*/

// const reductionOperations = (nums) => {
//   // count number of each element in nums
//   const count = {};
//   smallestNum = Infinity;
//   nums.forEach((num) => {
//     if (!(num in count)) count[num] = 0;
//     count[num]++;

//     // while couting determine the smallest number
//     if (num < smallestNum) smallestNum = num;
//   });

//   let res = 0;
//   // iterate over count
//   Object.keys(count).forEach((num) => {
//     res += count[num] * (num - smallestNum);
//   });
//   // res +=  count * (num - smallestNum)
//   // return res
//   return res;
// };

const reductionOperations = (nums) => {
  // sort input in reverse
  nums.sort((a, b) => b - a);
  let operations = 0;
  let prevUnique = nums[0];

  for (let i = 1; i < nums.length; ++i) {
    if (nums[i] === prevUnique) continue;

    if (nums[i] < prevUnique) operations += i;

    prevUnique = nums[i];
  }

  return operations;
};

module.exports.reductionOperations = reductionOperations;
