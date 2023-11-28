/*
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input
character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
*/

const compress = (chars) => {
  let lastUpdatedIdx = 0;
  let prev = chars[0];
  let count = 1;

  for (let i = 1; i < chars.length; ++i) {
    if (chars[i] === prev) count++;
    else {
      const s = count > 1 ? `${prev}${count}` : prev;
      for (let j = 0; j < s.length; ++j) {
        chars[lastUpdatedIdx] = s[j];
        lastUpdatedIdx++;
      }
      count = 1;
    }
    prev = chars[i];
  }

  const s = count > 1 ? `${prev}${count}` : prev;
  for (let j = 0; j < s.length; ++j) {
    chars[lastUpdatedIdx] = s[j];
    lastUpdatedIdx++;
  }
  return lastUpdatedIdx;
};

module.exports.compress = compress;
