/*
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

    Constraints:
    * 1 <= s.length <= 105
    * s[i] is either 'A', 'C', 'G', or 'T'.
*/

function findRepeatedDnaSequences(string) {
    // two sets one for seenSubs and one for repeatSubs
    const seenSubs = new Set();
    const repeatSubs = new Set();

    for(let i = 0; i < string.length - 9; i++) {
        // get the substring
        const subString = string.slice(i, i + 10);
        if (seenSubs.has(subString)) {
            repeatSubs.add(subString);
        } else {
            seenSubs.add(subString)
        }
    }

    return [...repeatSubs];
}

console.log(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) // ["AAAAACCCCC","CCCCCAAAAA"]
console.log(findRepeatedDnaSequences("AAAAAAAAAAAAA")) // ["AAAAAAAAAA"]
