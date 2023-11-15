/*
    You are given an array of positive integers arr. Perform some operations (possibly none) on
    arr so that it satisfies these conditions:

    - The value of the first element in arr must be 1.
    - The absolute difference between any 2 adjacent elements must be less than or equal to 1.

    In other words, abs(arr[i] - arr[i - 1]) <= 1 for each i where 1 <= i < arr.length (0-indexed).
    abs(x) is the absolute value of x.


    There are 2 types of operations that you can perform any number of times:

    1. Decrease the value of any element of arr to a smaller positive integer.
    2. Rearrange the elements of arr to be in any order.

    Return the maximum possible value of an element in arr after performing the operations to
    satisfy the conditions.
*/

const maxElementAfterDecrementAndRearrange = (arr) => {
  // sort the input arr
  arr.sort((a, b) => a - b);
  if (arr[0] !== 1) arr[0] = 1;

  // iterate over input arr from 1 -> n
  for (let i = 1; i < arr.length; i++) {
    // if abs diff between cur and prev > 1:
    const cur = arr[i];
    const prev = arr[i - 1];
    const diff = Math.abs(cur - prev);

    if (diff > 1) arr[i] = prev + 1;
  }
  return arr[arr.length - 1];
};

module.exports.maxElementAfterDecrementAndRearrange =
  maxElementAfterDecrementAndRearrange;
