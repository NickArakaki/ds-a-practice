/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
*/

function twoSum(nums, target) {
    // use a hashmap to store the ele visited along with idx
    const visitedNums = {};

    // iterate through nums
    for(let i = 0; i < nums.length; i++) {
        const currentNum = nums[i];
        const difference = target - currentNum;
        if (difference in visitedNums) {
            // if difference is in the hash map then we have our two indices
            return [visitedNums[difference], i]
        } else {
            // if the difference between target and current num is not in the hashmap add it to the hash map
            visitedNums[currentNum] = i;
        }
    }
}




console.log(twoSum([2, 7, 11, 15], 9)); // [0, 1]
console.log(twoSum([3, 2, 4], 6)); // [1, 2]
console.log(twoSum([3, 3], 6)); // [0, 1]
