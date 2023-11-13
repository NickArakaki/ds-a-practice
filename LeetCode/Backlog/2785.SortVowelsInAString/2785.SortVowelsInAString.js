/*
Given a 0-indexed string s, permute s to get a new string t such that:

All consonants remain in their original places. More formally,
if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
The vowels must be sorted in the nondecreasing order of their ASCII values.
More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j]
are vowels, then t[i] must not have a higher ASCII value than t[j].
Return the resulting string.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in
lowercase or uppercase. Consonants comprise all letters that are not vowels.
*/

const sortVowels = (s) => {
  // list of vowels 'a', 'e', 'i', 'o', 'u' can be upper or lower case
  const vowels = new Set(["a", "e", "i", "o", "u"]);
  const chars = s.split("");
  // iterate over s and extract vowels into array
  const sVowels = chars.filter((char) => vowels.has(char.toLowerCase()));
  // sort vowels array
  sVowels.sort();
  let vowelPointer = 0;
  // iterate over s, if current char is a vowel, replace with the first char in the sorted vowel array
  chars.forEach((char, i) => {
    if (vowels.has(char.toLowerCase())) {
      chars[i] = sVowels[vowelPointer];
      vowelPointer++;
    }
  });
  // retrun the new joined s
  return chars.join("");
};

module.exports.sortVowels = sortVowels;
