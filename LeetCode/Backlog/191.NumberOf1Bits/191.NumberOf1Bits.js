/*
Write a function that takes the binary representation of an unsigned integer and returns the
number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type.
In this case, the input will be given as a signed integer type. It should not affect your
implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.

In Java, the compiler represents the signed integers using 2's complement notation. Therefore,
in Example 3, the input represents the signed integer. -3.
*/

// const hammingWeight = (n) => {
//   n = n.toString();
//   count = 0;
//   for (let i = 0; i < n.length; ++i) {
//     if (n[i] === "1") count++;
//   }
//   return count;
// };

const hammingWeight = (n) => {
  count = 0;
  while (n) {
    n = n & (n - 1);
    count++;
  }

  return count;
};

module.exports.hammingWeight = hammingWeight;
