/*
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the
remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109,
and you want to check one by one to see if t has its subsequence. In this scenario,
how would you change your code?

*/

function isSubsequence(s, t) {
  // pointer for s
  let sPointer = 0;
  // iterate thru string t
  for (const tChar of t) {
    // if pointer s > len s return true
    if (sPointer >= s.length) {
      return true;
    }
    // if char at string t === char at pointer s
    if (tChar === s[sPointer]) {
      // increment pointer for s
      sPointer++;
    }
  }
  // return false
  return sPointer >= s.length;
}

console.log(isSubsequence("abc", "ahbgdc") === true);
console.log(isSubsequence("axc", "ahbgdc") === false);
console.log(isSubsequence("", "ahbgdc") === true);
