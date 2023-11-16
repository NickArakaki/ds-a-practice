/*
    Given an array of strings nums containing n unique binary strings
    each of length n, return a binary string of length n that does not
    appear in nums. If there are multiple answers, you may return any of them.
*/

// const findDifferentBinString = (nums) => {
//   // get max of possible nums, 2**(nums[0].length - 1)
//   const numBits = nums[0].length;
//   // convert each num to int and store in set
//   const numSet = new Set(nums.map((num) => parseInt(num, 2)));
//   const max = 2 ** numBits - 1;

//   for (let curNum = 0; curNum <= max; curNum++) {
//     if (!numSet.has(curNum)) {
//       let binString = curNum.toString(2);
//       return "0".repeat(numBits - binString.length) + binString;
//     }
//   }
// };

const findDifferentBinString = (nums) => {
  // get opposite of bit at index i for nums[i]
  // return built up string
};

module.exports.findDifferentBinString = findDifferentBinString;
