a = ["Saleo", "demo", "two"];
function returnLongestString(a) {
  // Write a function that takes an array of strings as argument
  // Return the longest string
  // If multiple matches, return them all
  // Example: returnLongestString({'Saleo', 'demo', 'two'}) returns 'Saleo'
  let maxLength = 0;
  a.forEach((el) => {
    if (el.length > maxLength) maxLength = el.length;
  });

  const substrings = a.filter((el) => el.length === maxLength);
  return substrings.length > 1 ? substrings : substrings[0];
}
console.log(returnLongestString(a));
