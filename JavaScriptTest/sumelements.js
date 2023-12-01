a = [1, 2, 5, 10];
b = 9;
function sumSomeArrayElements(a, b) {
  // Write a function that takes an array (a) and a number (b) as arguments
  // Sum up all array elements with a value less than b + 1
  // Example: sumSomeArrayElements( {1,2,5,10}, 9) returns 8
  return a.reduce((acc, cur) => (cur < b + 1 ? acc + cur : acc), 0);
}
console.log(sumSomeArrayElements(a, b) === 8);
