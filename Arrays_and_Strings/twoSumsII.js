/*
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Constraints
    2 <= numbers.length <= 3 * 104

    -1000 <= numbers[i] <= 1000

    numbers is sorted in non-decreasing order.

    -1000 <= target <= 1000

    The tests are generated such that there is exactly one solution.
*/

function twoSums(numbers, target) {
    let left = 0;
    let right = numbers.length - 1;

    while (left < right) {
        if (numbers[left] + numbers[right] < target) left++;
        else if (numbers[left] + numbers[right] > target) right--;
        else return [left + 1, right + 1]
    }
}


console.log(twoSums([2,7,11,15], 9)) // [1,2]
console.log(twoSums([2,3,4], 6)) // [1,3]
console.log(twoSums([-1,0], -1)) // [1,2]
