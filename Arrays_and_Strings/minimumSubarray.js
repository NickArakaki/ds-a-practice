/*
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
*/


function minSubArrayLen(target, nums) {
    // initialize a left pointer at 0
    let leftPointer = 0;
    // initialize total sum to 0
    let totalSum = 0;
    // initialize minLength to infinity
    let minLength = Infinity;

    // use iterator in for loop as the right pointer
    for (let rightPointer = 0; rightPointer < nums.length; rightPointer++) {
        // add value at right pointer to total sum
        totalSum += nums[rightPointer];
        // if total sum >= target
        while (totalSum >= target) {
            // set the minLength to the minimum between currentLength (r - 1 + 1) and minLength
            minLength = Math.min((rightPointer - leftPointer + 1), minLength);
            // subtract l pointer value from totalSum
            totalSum -= nums[leftPointer];
            // increment l pointer
            leftPointer++;
        }
    }
    // if the minLength is infinity then return 0
    // else return minLength
    return minLength === Infinity ? 0 : minLength;
}


console.log(minSubArrayLen(7, [2,3,1,2,4,3])) // 2
console.log(minSubArrayLen(4, [1,4,4])) // 1
console.log(minSubArrayLen(11, [1,1,1,1,1,1,1,1])) // 0

// Follow Up: try doing this in O(n log n) time
